"""Ricerca nelle guide Palitalsoft (BM25, solo libreria standard).

Le guide Markdown vengono divise in sezioni (titoli ## e ###). Ogni sezione
diventa un "brano" indicizzato. La ricerca e' per parole chiave con una
normalizzazione leggera per l'italiano (minuscole, accenti, radice troncata).
"""
import math
import os
import re
import unicodedata
from collections import Counter, defaultdict

STOPWORDS = set("""
a ad al allo ai agli all alla alle con col coi da dal dallo dai dagli dall dalla dalle di del dello dei degli
dell della delle in nel nello nei negli nell nella nelle su sul sullo sui sugli sull sulla sulle per tra fra
il lo la i gli le l un uno una e ed o od ma se che chi cui non piu come dove quando anche perche quindi poi
mi ti si ci vi ne io tu lui lei noi voi loro mio mia miei mie tuo tua suo sua nostro vostro questo questa
questi queste quello quella quelli quelle essere e sono sei siamo siete era erano stato stata stati ho hai ha
abbiamo avete hanno avere fare fa faccio posso puo possono devo deve devono viene vengono cosa molto tutto
tutti tutte ogni nessun alcuni alcune sempre gia ancora solo dopo prima mai oppure ovvero cioe tramite
buongiorno salve grazie ciao riesco riesce
""".split())

MODULE_LABELS = {
    "01 - Informazioni Generali": "Informazioni Generali",
    "04 - Protocollo": "Protocollo",
    "03 - SERVIZI DEMOGRAFICI": "Servizi Demografici",
    "Normativa": "Normativa",
}
NORMATIVA = "Normativa"
# domande che riguardano la legge (obblighi, termini, fondamento giuridico)
LEGAL_RX = re.compile(r"\blegg[ei]\b|decret|normativ|\bnorm[ae]\b|articol|\bart\.|d\.?\s?p\.?\s?r|d\.?\s?lgs|\bcad\b|"
                      r"obblig|\btermin[ei]\b|scadenz|entro quant|quanti giorni|per quanto tempo|sanzion|imposta di bollo|esenzion|"
                      r"e.? previsto|e.? consentito|si puo.? per legge|riferimento")


def is_legal(text):
    return bool(LEGAL_RX.search(strip_accents((text or "").lower())))


def strip_accents(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


def stem(tok):
    # radice grezza: tronca a 6 caratteri, sufficiente per l'italiano in una demo
    return tok[:6] if len(tok) > 6 else tok


def tokenize(text):
    text = strip_accents(text.lower())
    toks = re.findall(r"[a-z0-9@]+", text)
    return [stem(t) for t in toks if t not in STOPWORDS and len(t) > 1]


def slugify(s):
    s = strip_accents(s.lower())
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


class Chunk:
    __slots__ = ("id", "path", "module", "doc_title", "section", "anchor", "text", "tf", "length")

    def __init__(self, cid, path, module, doc_title, section, anchor, text):
        self.id = cid
        self.path = path
        self.module = module
        self.doc_title = doc_title
        self.section = section
        self.anchor = anchor
        self.text = text
        toks = tokenize(doc_title + " " + section) * 2 + tokenize(text)  # titolo pesa doppio
        self.tf = Counter(toks)
        self.length = len(toks)

    def ref(self, max_chars=None):
        txt = self.text if not max_chars else self.text[:max_chars]
        return {
            "id": self.id, "path": self.path, "modulo": self.module,
            "guida": self.doc_title, "sezione": self.section, "anchor": self.anchor, "testo": txt,
        }


class GuideIndex:
    def __init__(self, root):
        self.root = root
        self.chunks = []
        self.docs = []  # {path, module, title}
        self.df = Counter()
        self.avglen = 1
        self._build()

    def _build(self):
        for dirpath, _, files in os.walk(self.root):
            for fn in sorted(files):
                if not fn.endswith(".md"):
                    continue
                full = os.path.join(dirpath, fn)
                rel = os.path.relpath(full, self.root).replace(os.sep, "/")
                top = rel.split("/")[0]
                module = MODULE_LABELS.get(top, top)
                with open(full, encoding="utf-8", errors="replace") as f:
                    md = f.read()
                title = self._title(md, fn)
                kind = "video" if "/video/" in rel else ("allegato" if "/allegati/" in rel else "guida")
                self.docs.append({"path": rel, "modulo": module, "titolo": title, "tipo": kind})
                for section, text in self._sections(md, title):
                    if len(text.strip()) < 40:
                        continue
                    c = Chunk(len(self.chunks), rel, module, title, section, slugify(section), text.strip())
                    self.chunks.append(c)
        self.postings = defaultdict(list)
        for c in self.chunks:
            for t in c.tf:
                self.df[t] += 1
                self.postings[t].append(c.id)
        self.avglen = sum(c.length for c in self.chunks) / max(1, len(self.chunks))
        self.docs.sort(key=lambda d: (d["modulo"], d["path"]))

    @staticmethod
    def _title(md, fn):
        m = re.search(r"^#\s+(.+)$", md, re.M)
        if m:
            return m.group(1).strip()
        return re.sub(r"^\d+\s*-\s*", "", fn[:-3])

    @staticmethod
    def _sections(md, title):
        """Divide per titoli ## e ###. Il testo prima del primo titolo e' la sezione introduttiva."""
        parts = re.split(r"^(#{2,3}\s+.+)$", md, flags=re.M)
        intro = re.sub(r"^#\s+.+$", "", parts[0], count=1, flags=re.M)
        yield title, intro
        parent = None
        for i in range(1, len(parts), 2):
            head = parts[i]
            body = parts[i + 1] if i + 1 < len(parts) else ""
            name = head.lstrip("#").strip()
            if head.startswith("## "):
                parent = name
                yield name, body
            else:
                yield (f"{parent} › {name}" if parent else name), body

    def search(self, query, k=6, modules=None, boost_modules=None, k1=1.4, b=0.75):
        q = tokenize(query)
        if not q:
            return []
        N = len(self.chunks)
        scores = defaultdict(float)
        for t in set(q):
            df = self.df.get(t)
            if not df:
                continue
            idf = math.log(1 + (N - df + 0.5) / (df + 0.5))
            for cid in self.postings[t]:
                c = self.chunks[cid]
                f = c.tf[t]
                if f:
                    scores[c.id] += idf * f * (k1 + 1) / (f + k1 * (1 - b + b * c.length / self.avglen))
        for cid in scores:
            c = self.chunks[cid]
            if boost_modules and c.module in boost_modules:
                scores[cid] *= 1.6
            if c.doc_title.upper().startswith("FAQ"):
                scores[cid] *= 1.15
        ranked = sorted(scores.items(), key=lambda x: -x[1])
        out = []
        for cid, s in ranked:
            c = self.chunks[cid]
            if modules and c.module not in modules:
                continue
            out.append((c, s))
            if len(out) >= k:
                break
        return out

    def read(self, rel):
        full = os.path.normpath(os.path.join(self.root, rel))
        if not full.startswith(os.path.normpath(self.root)) or not os.path.isfile(full):
            return None
        with open(full, encoding="utf-8", errors="replace") as f:
            return f.read()

    def doc(self, rel):
        for d in self.docs:
            if d["path"] == rel:
                return d
        return None


MODULE_HINTS = {
    "Protocollo": r"protocoll|pec\b|e-?mail|segnatura|titolario|fascicol|fattur|mittent|destinatar|assegnat",
    "Servizi Demografici": r"certificat|anagraf|anpr|stato civile|elettoral|carta d.identit|cie\b|residenz|aire",
}


def detect_modules(text):
    t = strip_accents(text.lower())
    return [m for m, rx in MODULE_HINTS.items() if re.search(rx, t)]


def extract_section(md, anchor):
    """Restituisce il testo della sezione con lo slug indicato (con le sue sottosezioni)."""
    if not anchor:
        return md
    lines = md.split("\n")
    start, level = None, None
    for i, line in enumerate(lines):
        m = re.match(r"^(#{1,4})\s+(.+)$", line)
        if not m:
            continue
        lv = len(m.group(1))
        if start is None:
            if slugify(m.group(2)) == anchor:
                start, level = i, lv
        elif lv <= level:
            return "\n".join(lines[start:i]).strip()
    return "\n".join(lines[start:]).strip() if start is not None else None
