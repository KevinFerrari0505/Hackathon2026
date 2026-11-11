"""Importa la normativa (XML Akoma Ntoso di Normattiva) nelle fonti dell'assistente.

Legge direttamente lo zip scaricato da Normattiva, SENZA scompattarlo, prende solo gli atti
elencati in SELEZIONE, li converte in Markdown (un titolo per ogni articolo) e li salva in
data/guide/Normativa/. Poi basta riavviare `python app.py`.

USO
  python importa_normativa.py "C:\\percorso\\Normativa.zip"
        importa gli atti della SELEZIONE qui sotto

  python importa_normativa.py "C:\\percorso\\Normativa.zip" --cerca protocollo
        elenca gli atti il cui titolo contiene "protocollo" (per trovarne di nuovi da aggiungere)

Funziona anche con una cartella gia' scompattata al posto dello zip, e con zip dentro lo zip.
Solo libreria standard di Python 3.9+.
"""
import io
import os
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

# ---------------------------------------------------------------------------------------------
# ATTI DA IMPORTARE  (tipo, data AAAAMMGG, numero, nome breve)
# Il tipo e' quello del nome cartella di Normattiva, es. "DECRETO LEGISLATIVO_20050307_82".
# Per aggiungere un atto: cercalo con --cerca e copia qui la riga che viene stampata.
# ---------------------------------------------------------------------------------------------
SELEZIONE = [
    ("DECRETO DEL PRESIDENTE DELLA REPUBBLICA", "20001228", "445",
     "DPR 445/2000 – Testo unico sulla documentazione amministrativa"),
    ("DECRETO LEGISLATIVO", "20050307", "82",
     "D.Lgs. 82/2005 – Codice dell'amministrazione digitale (CAD)"),
    ("DECRETO DEL PRESIDENTE DELLA REPUBBLICA", "19890530", "223",
     "DPR 223/1989 – Regolamento anagrafico"),
    ("DECRETO DEL PRESIDENTE DELLA REPUBBLICA", "19721026", "642",
     "DPR 642/1972 – Disciplina dell'imposta di bollo"),
    ("LEGGE", "19900807", "241",
     "L. 241/1990 – Procedimento amministrativo e accesso ai documenti"),
]

QUI = os.path.dirname(os.path.abspath(__file__))
DEST = os.path.join(QUI, "data", "guide", "Normativa")
CARTELLA_ATTO = re.compile(r"(?:^|/)([^/]+?)_(\d{8})_([^/_]+)/[^/]+\.xml$", re.I)


# ------------------------------------------------------------------ lettura dello zip
def elenca_xml(sorgente):
    """Restituisce coppie (percorso, funzione_che_legge_i_byte) per ogni XML, anche in zip annidati."""
    if os.path.isdir(sorgente):
        for d, _, files in os.walk(sorgente):
            for f in files:
                p = os.path.join(d, f)
                rel = os.path.relpath(p, sorgente).replace(os.sep, "/")
                if f.lower().endswith(".xml"):
                    yield rel, (lambda p=p: open(p, "rb").read())
                elif f.lower().endswith(".zip"):
                    yield from _da_zip(zipfile.ZipFile(p), rel + "!")
        return
    yield from _da_zip(zipfile.ZipFile(sorgente), "")


def _da_zip(zf, prefisso):
    for info in zf.infolist():
        nome = info.filename
        if info.is_dir():
            continue
        if nome.lower().endswith(".xml"):
            yield prefisso + nome, (lambda zf=zf, nome=nome: zf.read(nome))
        elif nome.lower().endswith(".zip"):
            interno = zipfile.ZipFile(io.BytesIO(zf.read(nome)))
            yield from _da_zip(interno, prefisso + nome + "!")


def chiave_atto(percorso):
    m = CARTELLA_ATTO.search(percorso.replace("\\", "/").replace("!", "/"))
    if not m:
        return None
    return (m.group(1).strip().upper(), m.group(2), m.group(3).strip().upper())


def priorita_versione(percorso):
    """Preferisce le raccolte VIGENTI e, a parita', la versione piu' recente."""
    p = percorso.upper()
    vig = 2 if "VIGENTE" in p and "MULTIVIGENTE" not in p else (1 if "MULTIVIGENTE" in p else 0)
    non_orig = 0 if "ORIGINALE" in os.path.basename(p) else 1
    v = re.search(r"_V(\d+)\.XML$", p)
    data = re.search(r"/(\d{4}-\d{2}-\d{2})_[^/]*\.XML$", p)
    return (vig, non_orig, int(v.group(1)) if v else 0, data.group(1) if data else "")


# ------------------------------------------------------------------ conversione AKN -> Markdown
def loc(tag):
    return tag.split("}", 1)[-1]


SALTA = {"authorialNote", "noteRef", "eol"}


def testo(el):
    """Testo di un elemento, senza le note redazionali."""
    parti = [el.text or ""]
    for c in el:
        if loc(c.tag) not in SALTA:
            parti.append(testo(c))
        parti.append(c.tail or "")
    return re.sub(r"\s+", " ", "".join(parti)).strip()


def figlio(el, nome):
    for c in el:
        if loc(c.tag) == nome:
            return c
    return None


CONTENITORI = {"book", "part", "title", "chapter", "section", "subsection"}
NOMI_CONT = {"book": "Libro", "part": "Parte", "title": "Titolo", "chapter": "Capo", "section": "Sezione", "subsection": "Sottosezione"}


def nc(num_t):
    """Numero del comma in grassetto (non come elenco numerato, che verrebbe rinumerato)."""
    return f"**{num_t}** " if num_t else ""


def blocco(el, rientro=0):
    """Converte comma, liste e punti in righe Markdown."""
    righe = []
    nome = loc(el.tag)
    num = figlio(el, "num")
    num_t = testo(num) if num is not None else ""
    pref = "  " * rientro
    if nome in ("paragraph",):
        corpo = []
        for c in el:
            t = loc(c.tag)
            if t in ("content", "intro", "chapeau"):
                s = testo(c)
                if s:
                    corpo.append(s)
            elif t in ("list", "point", "paragraph", "subparagraph"):
                if corpo:
                    righe.append(f"{pref}{nc(num_t)}{' '.join(corpo)}".strip())
                    corpo, num_t = [], ""
                sub = blocco(c, rientro + (0 if t == "list" else 1))
                if num_t and sub and not sub[0].lstrip().startswith("- "):
                    sub[0] = f"{pref}{nc(num_t)}{sub[0].lstrip()}"
                    num_t = ""
                righe.extend(sub)
            elif t in ("wrapUp",):
                s = testo(c)
                if s:
                    righe.append(f"{pref}{s}")
        if corpo:
            righe.append(f"{pref}{nc(num_t)}{' '.join(corpo)}".strip())
        return righe
    if nome == "list":
        for c in el:
            t = loc(c.tag)
            if t in ("intro", "chapeau"):
                s = testo(c)
                if s:
                    righe.append(f"{pref}{s}")
            elif t in ("point", "indent", "paragraph"):
                righe.extend(blocco(c, rientro))
            elif t == "wrapUp":
                s = testo(c)
                if s:
                    righe.append(f"{pref}{s}")
        return righe
    if nome in ("point", "indent", "subparagraph"):
        corpo, sotto = [], []
        for c in el:
            t = loc(c.tag)
            if t in ("content", "intro", "chapeau"):
                corpo.append(testo(c))
            elif t in ("list", "point", "indent"):
                sotto.extend(blocco(c, rientro + 1))
        righe.append(f"{pref}- {num_t} {' '.join(x for x in corpo if x)}".replace("  ", " ").rstrip())
        return righe + sotto
    s = testo(el)
    return [pref + s] if s else []


def articolo(el, percorso_cont):
    num = testo(figlio(el, "num")) if figlio(el, "num") is not None else "Articolo"
    head = figlio(el, "heading")
    titolo = testo(head) if head is not None else ""
    num = num.rstrip(".")
    righe = [f"## {num}" + (f" – {titolo}" if titolo else ""), ""]
    if percorso_cont:
        righe += [f"*{' › '.join(percorso_cont)}*", ""]
    corpo = []
    for c in el:
        t = loc(c.tag)
        if t in ("num", "heading", "subheading"):
            continue
        if t == "section":            # in Normattiva contiene solo le note redazionali
            continue
        if t in ("paragraph", "list", "point"):
            corpo.extend(blocco(c))
        elif t == "content":
            s = testo(c)
            if s:
                corpo.append(s)
    righe += [r for r in corpo if r.strip()] if corpo else ["*(testo non disponibile nella raccolta)*"]
    # separa i commi con una riga vuota (ma lascia unite le liste)
    out = []
    for r in righe:
        if out and r and not r.lstrip().startswith("- ") and out[-1] and not out[-1].startswith("#"):
            out.append("")
        out.append(r)
    return out + [""]


def contenitore(el, percorso):
    righe = []
    num = figlio(el, "num")
    head = figlio(el, "heading")
    etichetta = " ".join(x for x in [testo(num) if num is not None else "", testo(head) if head is not None else ""] if x)
    if not etichetta:
        etichetta = NOMI_CONT.get(loc(el.tag), "")
    nuovo = percorso + ([etichetta] if etichetta else [])
    for c in el:
        t = loc(c.tag)
        if t == "article":
            righe += articolo(c, nuovo)
        elif t in CONTENITORI:
            righe += contenitore(c, nuovo)
    return righe


def converti(xml_bytes, nome_breve):
    root = ET.fromstring(xml_bytes)
    act = next((e for e in root.iter() if loc(e.tag) in ("act", "decree", "bill", "doc")), root)
    doc_type = doc_date = doc_num = doc_title = ""
    vigore = ""
    for e in act.iter():
        t = loc(e.tag)
        if t == "docType" and not doc_type:
            doc_type = testo(e)
        elif t == "docDate" and not doc_date:
            doc_date = testo(e)
        elif t == "docNumber" and not doc_num:
            doc_num = testo(e)
        elif t == "docTitle" and not doc_title:
            doc_title = testo(e)
        elif t == "FRBRalias" and e.get("name") == "urn:nir" and not vigore:
            vigore = e.get("value", "")
    entrata = ""
    pref = figlio(act, "preface")
    if pref is not None:
        for n in pref.iter():
            if loc(n.tag) == "authorialNote":
                s = re.sub(r"\s+", " ", "".join(n.itertext())).strip()
                if "vigore" in s.lower():
                    entrata = s
                    break
    righe = [f"# {nome_breve}", "",
             f"{doc_type.capitalize()} {doc_date}{', n. ' + doc_num if doc_num else ''}: *{doc_title.strip()}*", "",
             "Fonte: Normattiva (formato Akoma Ntoso), testo importato automaticamente senza note redazionali."
             + (f" {entrata}." if entrata else "") + (f" URN: `{vigore}`" if vigore else ""), ""]
    body = figlio(act, "body")
    if body is None:
        return None
    n_art = 0
    for c in body:
        t = loc(c.tag)
        if t == "article":
            righe += articolo(c, [])
            n_art += 1
        elif t in CONTENITORI:
            blocco_c = contenitore(c, [])
            n_art += sum(1 for r in blocco_c if r.startswith("## "))
            righe += blocco_c
    return "\n".join(righe).rstrip() + "\n", n_art


def nome_file(nome_breve):
    s = re.sub(r"[^\w\s.-]", "", nome_breve.split("–")[0].replace("/", "-")).strip()
    return re.sub(r"\s+", " ", s).replace("/", "-") + ".md"


# ------------------------------------------------------------------ comandi
def importa(sorgente):
    voluti = {(t.upper(), d, n.upper()): breve for t, d, n, breve in SELEZIONE}
    trovati = {}
    print("Lettura dell'archivio (può richiedere qualche minuto)…")
    for percorso, leggi in elenca_xml(sorgente):
        k = chiave_atto(percorso)
        if k in voluti:
            prio = priorita_versione(percorso)
            if k not in trovati or prio > trovati[k][0]:
                trovati[k] = (prio, percorso, leggi)
    os.makedirs(DEST, exist_ok=True)
    for k, breve in voluti.items():
        if k not in trovati:
            print(f"  NON TROVATO  {breve}  (cartella attesa: {k[0]}_{k[1]}_{k[2]})")
            continue
        _, percorso, leggi = trovati[k]
        try:
            ris = converti(leggi(), breve)
        except ET.ParseError as e:
            print(f"  ERRORE XML   {breve}: {e}")
            continue
        if not ris:
            print(f"  VUOTO        {breve}: nessun articolo nel file")
            continue
        md, n_art = ris
        with open(os.path.join(DEST, nome_file(breve)), "w", encoding="utf-8") as f:
            f.write(md)
        print(f"  OK           {breve}: {n_art} articoli  ←  {percorso}")
    print(f"\nFile salvati in {DEST}\nRiavvia `python app.py` per usarli.")


def cerca(sorgente, parola):
    parola_l = parola.lower()
    visti = set()
    for percorso, leggi in elenca_xml(sorgente):
        k = chiave_atto(percorso)
        if not k or k in visti:
            continue
        visti.add(k)
        try:
            inizio = leggi()[:200000].decode("utf-8", "replace")
        except Exception:
            continue
        m = re.search(r"<docTitle[^>]*>(.*?)</docTitle>", inizio, re.S)
        titolo = re.sub(r"<[^>]+>|\s+", " ", m.group(1)).strip() if m else ""
        if parola_l in titolo.lower() or parola_l in percorso.lower():
            print(f'    ("{k[0]}", "{k[1]}", "{k[2]}", "{titolo[:70]}"),')
    print(f"\n{len(visti)} atti esaminati. Copia nella SELEZIONE le righe che ti interessano.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    src = sys.argv[1]
    if not os.path.exists(src):
        print(f"Non trovo: {src}")
        sys.exit(1)
    if len(sys.argv) >= 4 and sys.argv[2] == "--cerca":
        cerca(src, " ".join(sys.argv[3:]))
    else:
        importa(src)
