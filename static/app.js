/* ORIENTA – demo hackathon Palitalsoft × UNICAM. JavaScript senza dipendenze. */
"use strict";

const S = {
  who: localGet("who") || "op1",
  ops: [], stato: {}, argomenti: {},
  chat: {},          // per operatore: { convId, msgs: [] }
  busy: false,
};
const $ = (sel, el = document) => el.querySelector(sel);
const $$ = (sel, el = document) => [...el.querySelectorAll(sel)];

function localGet(k) { try { return localStorage.getItem(k); } catch { return null; } }
function localSet(k, v) { try { localStorage.setItem(k, v); } catch { /* storage non disponibile */ } }

async function api(path, body) {
  const opt = body === undefined ? {} : { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(body) };
  const r = await fetch(path, opt);
  const j = await r.json().catch(() => ({}));
  if (!r.ok) throw new Error(j.errore || `Errore ${r.status}`);
  return j;
}

/* ------------------------------------------------------------------ utilità */
const esc = (s) => String(s ?? "").replace(/[&<>"']/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
const slug = (s) => String(s).toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "");
const fmtDate = (s) => s ? new Date(s).toLocaleDateString("it-IT", { day: "2-digit", month: "2-digit", year: "numeric" }) : "";
const fmtDT = (s) => s ? new Date(s).toLocaleString("it-IT", { day: "2-digit", month: "2-digit", hour: "2-digit", minute: "2-digit" }) : "";
const me = () => S.ops.find((o) => o.id === S.who) || {};
const role = () => me().ruolo || "operatore";
const firstName = (n) => (n || "").split(" ")[0];

function toast(msg) {
  const t = $("#toast"); t.textContent = msg; t.hidden = false;
  clearTimeout(toast._t); toast._t = setTimeout(() => (t.hidden = true), 3200);
}
function modal(html) { $("#modal-body").innerHTML = html; $("#modal").hidden = false; $(".modal-close").focus(); }
function closeModal() { $("#modal").hidden = true; }
$("#modal").addEventListener("click", (e) => { if (e.target.id === "modal" || e.target.classList.contains("modal-close")) closeModal(); });
document.addEventListener("keydown", (e) => { if (e.key === "Escape") closeModal(); });

const STATO_LABEL = { lacuna: "Lacuna confermata", da_verificare: "Possibile lacuna", in_crescita: "In consolidamento", competente: "Competente", segnale_debole: "Segnale debole" };
const TIPO_LABEL = { supporto_operativo: "Supporto operativo", anomalia: "Anomalia software", formazione: "Formazione", da_classificare: "Da classificare" };
const ESITO_LABEL = { risolta_ai: ["Risolta dall'assistente", "b-green"], escalation: ["Inoltrata al tecnico", "b-violet"], risolta_manuale: ["Risolta dal tecnico", "b-blue"], ticket_manuale: ["Ticket manuale", "b-grey"] };
const badge = (stato) => `<span class="badge b-${stato}">${STATO_LABEL[stato] || stato}</span>`;

/* ------------------------------------------------------------------ markdown */
function inline(s) {
  s = esc(s);
  s = s.replace(/`([^`]+)`/g, "<code>$1</code>");
  s = s.replace(/\*\*([^*]+)\*\*/g, "<b>$1</b>");
  s = s.replace(/(^|[^*\w])\*([^*\s][^*]*?)\*(?!\w)/g, "$1<i>$2</i>");
  s = s.replace(/\[([^\]]+)\]\((https?:\/\/[^)\s]+)\)/g, '<a href="$2" target="_blank" rel="noopener">$1</a>');
  return s;
}
const SHOT_ICON = '<svg width="18" height="18" viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="9" cy="10" r="2" fill="currentColor"/><path d="M5 17l5-5 3 3 3-2 3 4" fill="none" stroke="currentColor" stroke-width="2"/></svg>';

function md(src) {
  const lines = String(src || "").replace(/\r/g, "").split("\n");
  let html = "", para = [], i = 0;
  const flush = () => { if (para.length) { html += `<p>${inline(para.join(" "))}</p>`; para = []; } };
  while (i < lines.length) {
    const line = lines[i];
    if (!line.trim()) { flush(); i++; continue; }
    let m;
    if ((m = line.match(/^(#{1,6})\s+(.*)$/))) {
      flush(); const lv = Math.min(4, m[1].length + 1);
      html += `<h${lv} id="h-${slug(m[2])}">${inline(m[2])}</h${lv}>`; i++; continue;
    }
    if (/^\s*(-{3,}|\*{3,})\s*$/.test(line)) { flush(); html += "<hr>"; i++; continue; }
    if (/^\s*\[[^\]]{8,}\]\s*:?\s*$/.test(line) || /^\s*\[(Schermata|Finestra|Finella|Immagine)/i.test(line)) {
      flush(); let t = line.trim();
      while (!t.includes("]") && i + 1 < lines.length) { i++; t += " " + lines[i].trim(); }
      html += `<div class="shot">${SHOT_ICON}<span>${esc(t.replace(/^\[|\]\s*:?$/g, ""))}</span></div>`; i++; continue;
    }
    if (/^\s*>/.test(line)) {
      flush(); const buf = [];
      while (i < lines.length && /^\s*>/.test(lines[i])) { buf.push(lines[i].replace(/^\s*>\s?/, "")); i++; }
      html += `<blockquote>${md(buf.join("\n"))}</blockquote>`; continue;
    }
    if (/^\s*\|/.test(line) && i + 1 < lines.length && /^\s*\|?\s*:?-{2,}/.test(lines[i + 1])) {
      flush(); const cells = (l) => l.trim().replace(/^\||\|$/g, "").split("|").map((c) => inline(c.trim()));
      let t = `<table><thead><tr>${cells(line).map((c) => `<th>${c}</th>`).join("")}</tr></thead><tbody>`; i += 2;
      while (i < lines.length && /^\s*\|/.test(lines[i])) { t += `<tr>${cells(lines[i]).map((c) => `<td>${c}</td>`).join("")}</tr>`; i++; }
      html += t + "</tbody></table>"; continue;
    }
    if (/^\s*([-*+]|\d+[.)])\s+/.test(line)) {
      flush();
      const stack = [];
      while (i < lines.length && (/^\s*([-*+]|\d+[.)])\s+/.test(lines[i]) || (lines[i].trim() && /^\s{2,}/.test(lines[i]) && stack.length))) {
        const l = lines[i];
        const mm = l.match(/^(\s*)([-*+]|\d+[.)])\s+(.*)$/);
        if (!mm) { html += " " + inline(l.trim()); i++; continue; }
        const ind = mm[1].length, tag = /\d/.test(mm[2]) ? "ol" : "ul";
        if (!stack.length || ind > stack[stack.length - 1].ind) { html += `<${tag}>`; stack.push({ ind, tag }); }
        else {
          while (stack.length > 1 && ind < stack[stack.length - 1].ind) { html += `</li></${stack.pop().tag}>`; }
          html += "</li>";
        }
        html += `<li>${inline(mm[3])}`; i++;
      }
      while (stack.length) html += `</li></${stack.pop().tag}>`;
      continue;
    }
    para.push(line.trim()); i++;
  }
  flush();
  return `<div class="md">${html}</div>`;
}

/* ------------------------------------------------------------------ navigazione */
const NAV = {
  operatore: [
    ["Il mio lavoro", null], ["#/home", "Home"], ["#/assistente", "Assistente"], ["#/formazione", "Formazione"], ["#/profilo", "Il mio profilo"],
    ["Sempre disponibili", null], ["#/manuali", "Manuali"], ["#/ticket", "Apri un ticket"],
  ],
  tecnico: [
    ["Help desk", null], ["#/tecnico/coda", "Coda di emergenza"], ["#/tecnico/ticket", "Ticket ricevuti"],
    ["Documentazione", null], ["#/manuali", "Manuali"],
  ],
  responsabile: [
    ["Formazione", null], ["#/dashboard", "Dashboard"], ["#/catalogo", "Corsi e quiz"],
    ["Documentazione", null], ["#/manuali", "Manuali"],
  ],
};
const HOME = { operatore: "#/home", tecnico: "#/tecnico/coda", responsabile: "#/dashboard" };

function renderNav() {
  const r = location.hash.split("?")[0];
  $("#nav").innerHTML = '<div class="nav-inner">' + NAV[role()].map(([h, l]) => l === null ? `<div class="group">${h}</div>`
    : `<a href="${h}" class="${r === h || (h !== "#/home" && r.startsWith(h + "/")) ? "active" : ""}">${l}${h === "#/tecnico/coda" && S.stato.coda_in_attesa ? `<span class="count">${S.stato.coda_in_attesa}</span>` : ""}</a>`).join("") + "</div>";
}

function renderWho() {
  const groups = { operatore: "Operatori comunali", tecnico: "Help desk", responsabile: "Responsabile formazione" };
  $("#who").innerHTML = Object.entries(groups).map(([r, g]) => `<optgroup label="${g}">${S.ops.filter((o) => o.ruolo === r)
    .map((o) => `<option value="${o.id}" ${o.id === S.who ? "selected" : ""}>${esc(o.nome)}${r === "operatore" ? " · " + esc(o.ufficio) : ""}</option>`).join("")}</optgroup>`).join("");
}
$("#who").addEventListener("change", (e) => { S.who = e.target.value; localSet("who", S.who); location.hash = HOME[role()]; route(); });

function renderStatus() {
  const s = S.stato, p = $("#ai-pill");
  p.className = "pill " + (s.motore === "down" ? "down" : s.motore === "offline" ? "offline" : "");
  p.textContent = s.motore === "down" ? "AI non disponibile" : s.motore === "offline" ? "AI: modalità offline" : `AI attiva · ${s.modello}`;
  const b = $("#banner");
  if (s.motore === "down") {
    b.innerHTML = `<div class="bar">Servizio AI non disponibile: le richieste vengono salvate nella coda di emergenza (${s.coda_in_attesa} in attesa).
      Manuali, ticket e formazione restano utilizzabili. <a href="#/manuali">Consulta i manuali</a> <a href="#/ticket">Apri un ticket</a></div>`;
  } else if (s.job_coda && (s.job_coda.attivo || (s.job_coda.totale && Date.now() - (S.jobSeen || 0) < 15000))) {
    if (s.job_coda.attivo) S.jobSeen = Date.now();
    b.innerHTML = `<div class="bar ok">Servizio AI ripristinato: elaborazione della coda di emergenza ${s.job_coda.attivo ? "in corso" : "completata"} (${s.job_coda.elaborate}/${s.job_coda.totale}).</div>`;
  } else b.innerHTML = "";
  renderNav();
}

async function poll() {
  try {
    const prev = S.stato.motore;
    S.stato = await api("/api/stato");
    renderStatus();
    if (prev && prev !== S.stato.motore && location.hash.startsWith("#/tecnico/coda")) route();
    if (S.stato.job_coda?.attivo && location.hash.startsWith("#/tecnico/coda")) route();
  } catch { /* server momentaneamente non raggiungibile */ }
}

/* ------------------------------------------------------------------ router */
async function route() {
  const [path, qs] = (location.hash || HOME[role()]).split("?");
  const params = new URLSearchParams(qs || "");
  const parts = path.replace(/^#\//, "").split("/");
  renderNav();
  const v = $("#view");
  const allowed = { operatore: ["home", "assistente", "formazione", "corso", "profilo", "manuali", "ticket"], tecnico: ["tecnico", "manuali"], responsabile: ["dashboard", "catalogo", "corso", "profilo", "manuali"] };
  if (!allowed[role()].includes(parts[0])) { location.hash = HOME[role()]; return; }
  try {
    switch (parts[0]) {
      case "home": await viewHome(v); break;
      case "assistente": await viewAssistant(v, params); break;
      case "formazione": await viewCatalog(v, true); break;
      case "catalogo": await viewCatalog(v, false); break;
      case "corso": await viewCourse(v, parts[1]); break;
      case "profilo": await viewProfile(v, parts[1] || S.who); break;
      case "manuali": await viewManuals(v, params); break;
      case "ticket": viewTicketForm(v); break;
      case "tecnico": parts[1] === "ticket" ? await viewTickets(v) : await viewQueue(v); break;
      case "dashboard": await viewDashboard(v); break;
    }
  } catch (e) { v.innerHTML = `<div class="card">Errore: ${esc(e.message)}</div>`; }
}
window.addEventListener("hashchange", () => { route(); window.scrollTo(0, 0); });

/* ------------------------------------------------------------------ HOME operatore */
const DEMO_CHIPS = [
  "Le PEC arrivano ma gli allegati non finiscono nel protocollo",
  "Come protocollo una fattura elettronica in arrivo?",
  "Quando premo Registra su una partenza compare \"Errore interno: impossibile generare la segnatura XML\"",
  "Non vedo alcuni protocolli del mio ufficio nella ricerca",
  "Come rilascio un certificato ANPR a un non residente?",
];

async function viewHome(v) {
  const d = await api(`/api/home/${S.who}`);
  const op = d.operatore, prof = d.profilo;
  const ora = new Date().getHours();
  const saluto = ora < 13 ? "Buongiorno" : ora < 18 ? "Buon pomeriggio" : "Buonasera";
  v.innerHTML = `
  <section class="hero">
    <div><h1>${saluto}, ${esc(firstName(op.nome))}</h1><div>${esc(op.ufficio)} · ${esc(op.ente)}</div></div>
    <form class="ask" id="ask"><input type="text" id="ask-in" placeholder="Descrivi il problema con parole tue…" aria-label="Descrivi il problema"><button class="btn">Chiedi all'assistente</button></form>
    <div class="chips">${DEMO_CHIPS.slice(0, 4).map((c) => `<button class="chip" data-q="${esc(c)}">${esc(c)}</button>`).join("")}</div>
  </section>
  <div class="grid g2" style="margin-top:18px">
    <div class="card">
      <div class="row"><h2 style="margin:0">Formazione consigliata per te</h2><span class="spacer"></span><a href="#/profilo" class="small">Il mio profilo →</a></div>
      <p class="muted small" style="margin:4px 0 12px">Calcolata dalle tue richieste di assistenza e dai risultati dei quiz.</p>
      ${suggestionsHtml(prof)}
    </div>
    <div class="card">
      <h2>Le tue richieste</h2>
      ${d.conversazioni.length ? `<ul class="list">${d.conversazioni.map(convItem).join("")}</ul>` : `<p class="muted">Nessuna richiesta all'assistente in questa sessione.</p>`}
      ${d.storico.length ? `<h3 style="margin-top:18px">Storico richieste</h3><ul class="list small">${d.storico.map((r) => `<li><div class="row"><span>${esc(r.testo)}</span></div>
        <div class="row tiny muted">${fmtDate(r.creata)} · ${esc((S.argomenti[r.argomento] || {}).nome || "—")} · ${TIPO_LABEL[r.tipo] || "—"} ${ESITO_LABEL[r.esito] ? `<span class="badge ${ESITO_LABEL[r.esito][1]}">${ESITO_LABEL[r.esito][0]}</span>` : ""}</div></li>`).join("")}</ul>` : ""}
    </div>
  </div>
  <div class="card" style="margin-top:16px"><div class="row"><div><b>Se l'assistente non risponde</b> <span class="muted small">puoi sempre consultare i manuali o aprire un ticket tradizionale.</span></div><span class="spacer"></span>
    <a class="btn secondary sm" href="#/manuali">Manuali</a><a class="btn secondary sm" href="#/ticket">Apri un ticket</a></div></div>`;
  $("#ask").addEventListener("submit", (e) => { e.preventDefault(); const t = $("#ask-in").value.trim(); if (t) startChat(t); });
  $$(".chip", v).forEach((b) => b.addEventListener("click", () => startChat(b.dataset.q)));
  $$("[data-conv]", v).forEach((b) => b.addEventListener("click", () => openConversation(+b.dataset.conv)));
}

function suggestionsHtml(prof) {
  const items = [];
  prof.suggerimenti.forEach((s) => items.push(`<div class="card suggest ${s.stato}" style="box-shadow:none;margin-bottom:10px">
    <div class="row">${badge(s.stato)}<b>${esc(s.nome)}</b></div>
    <ul class="why muted">${s.motivo.map((m) => `<li>${esc(m)}</li>`).join("")}</ul>
    <div class="row" style="margin-top:8px"><a class="btn sm" href="#/corso/${s.corso}">${s.stato === "lacuna" ? "Ripassa" : "Ripasso + quiz di verifica"}</a><span class="small muted">${esc(s.corso_titolo)}</span></div></div>`));
  prof.verifiche.forEach((s) => items.push(`<div class="card suggest verifica" style="box-shadow:none;margin-bottom:10px">
    <div class="row"><span class="badge b-blue">Verifica periodica</span><b>${esc(s.nome)}</b></div>
    <p class="small muted" style="margin:4px 0 8px">Per controllare che le conoscenze restino nel tempo: ultimo quiz ${s.ultimo_quiz.punteggio}% il ${fmtDate(s.ultimo_quiz.data)}.</p>
    <a class="btn secondary sm" href="#/corso/${s.corso}#quiz">Fai il quiz (2 minuti)</a></div>`));
  return items.length ? items.join("") : `<p class="muted">Nessuna lacuna rilevata. Ottimo lavoro!</p>`;
}

function convItem(c) {
  const st = { risolta: ["Risolta", "b-green"], escalation: [`Ticket ${c.ticket || ""}`, "b-violet"], in_coda: ["In coda di emergenza", "b-red"], aperta: ["In attesa di una tua risposta", "b-orange"] }[c.stato] || [c.stato, "b-grey"];
  return `<li><div class="row"><b style="flex:1">${esc(c.testo)}</b><span class="badge ${st[1]}">${st[0]}</span></div>
  <div class="row small muted">${fmtDT(c.creata)}${c.differita ? ` · <span class="badge b-blue">Risposta arrivata dopo il ripristino del servizio AI</span>` : ""}
  <span class="spacer"></span><button class="btn ghost sm" data-conv="${c.id}">Apri</button></div></li>`;
}

/* ------------------------------------------------------------------ ASSISTENTE */
function chatState() { return (S.chat[S.who] ||= { convId: null, msgs: [], closed: false }); }
function startChat(text) { const c = chatState(); c.convId = null; c.msgs = []; c.closed = false; S.pending = text; location.hash = "#/assistente"; }
async function openConversation(id) {
  const conv = await api(`/api/conversazione/${id}`);
  const c = chatState(); c.convId = conv.id; c.msgs = conv.messaggi; c.closed = conv.stato !== "aperta";
  location.hash = "#/assistente";
  if (location.hash === "#/assistente") route();
}

async function viewAssistant(v) {
  const c = chatState();
  v.innerHTML = `
  <div class="chat-wrap">
    <section class="card chat">
      <div class="chat-head"><div><h2 style="margin:0">Assistente</h2><div class="small muted">Risponde solo sulla base della documentazione Palitalsoft. Se non trova la risposta, prepara il ticket per il tecnico.</div></div>
        <span class="spacer"></span><button class="btn ghost sm" id="new-conv">Nuova richiesta</button></div>
      <div class="msgs" id="msgs" aria-live="polite"></div>
      <div class="composer">
        <form id="chat-form"><input type="text" id="chat-in" placeholder="Scrivi qui…" autocomplete="off" aria-label="Messaggio"><button class="btn" id="send">Invia</button></form>
      </div>
    </section>
    <aside class="side">
      <div class="card"><h3>Stato della richiesta</h3><ul class="steps" id="steps"></ul></div>
      <div class="card"><h3>Guide consultate</h3><div id="side-fonti" class="small muted">Le guide usate per la risposta compariranno qui.</div></div>
      <div class="card small"><h3>Sempre disponibili</h3><p class="muted" style="margin:0 0 8px">Anche se l'assistente non risponde:</p>
        <div class="row"><a class="btn secondary sm" href="#/manuali">Manuali</a><a class="btn secondary sm" href="#/ticket">Ticket tradizionale</a></div></div>
    </aside>
  </div>`;
  $("#new-conv").addEventListener("click", () => { c.convId = null; c.msgs = []; c.closed = false; drawChat(); });
  $("#chat-form").addEventListener("submit", (e) => { e.preventDefault(); const t = $("#chat-in").value.trim(); if (t) send(t); });
  drawChat();
  if (S.pending) { const t = S.pending; S.pending = null; send(t); }
  else $("#chat-in").focus();
}

function drawChat() {
  const c = chatState(), box = $("#msgs");
  if (!box) return;
  if (!c.msgs.length) {
    box.innerHTML = `<div class="msg ai"><div class="who-l">Assistente</div>${md(`Ciao ${firstName(me().nome)}, descrivimi il problema con parole tue. Se serve ti farò qualche domanda; se la documentazione non copre il caso, preparo io il ticket per il tecnico.`)}</div>
      <div class="small muted" style="margin-top:6px">Esempi:</div><div class="chips" id="chips">${DEMO_CHIPS.map((q) => `<button class="chip" data-q="${esc(q)}">${esc(q)}</button>`).join("")}</div>`;
    $$("#chips .chip", box).forEach((b) => b.addEventListener("click", () => send(b.dataset.q)));
  } else box.innerHTML = c.msgs.map((m, i) => msgHtml(m, i === c.msgs.length - 1)).join("");
  if (S.busy) box.insertAdjacentHTML("beforeend", `<div class="msg ai"><div class="who-l">Assistente sta cercando nelle guide…</div><span class="typing"><i></i><i></i><i></i></span></div>`);
  box.scrollTop = box.scrollHeight;
  bindMsgActions(box);
  drawSide();
}

function msgHtml(m, isLast) {
  if (m.ruolo === "operatore") return `<div class="msg me">${esc(m.testo)}</div>`;
  const cls = { risolto: "ok", guida_suggerita: "ok", chiarimento: "ask", escalation: "esc", coda: "coda" }[m.esito] || "";
  const lab = { risolto: "Risposta dalla documentazione", guida_suggerita: "Guida suggerita", chiarimento: "Domanda di chiarimento", escalation: "Inoltrata al tecnico", coda: "Coda di emergenza" }[m.esito] || "";
  let h = `<div class="msg ai ${cls}"><div class="who-l">Assistente · ${lab}${m.differita ? ' <span class="badge b-blue">risposta differita</span>' : ""}</div>${md(m.testo)}`;
  if (m.fonti && m.fonti.length) h += fontiHtml(m.fonti);
  if (m.ticket) h += ticketHtml(m.ticket);
  if (m.formazione) h += bridgeHtml(m.formazione);
  if (m.nota_profilo) h += `<div class="note-prof">${esc(m.nota_profilo)}</div>`;
  if (isLast && ["risolto", "guida_suggerita"].includes(m.esito) && !m.differita && !m.feedback) {
    h += `<div class="feedback"><span class="small muted">Ha funzionato?</span><button class="btn success sm" data-fb="ok">Sì, problema risolto</button><button class="btn ghost sm" data-fb="ko">No, inoltra al tecnico</button></div>`;
  }
  if (m.feedback === "ok") h += `<div class="note-prof">Grazie! Nessun ticket necessario.</div>`;
  return h + "</div>";
}

function fonteBtn(f) {
  const norma = f.modulo === "Normativa" || String(f.path || "").startsWith("Normativa/");
  return `<button class="fonte${norma ? " norma" : ""}" data-path="${esc(f.path)}" data-anchor="${esc(f.anchor || "")}" title="${norma ? "Apri il testo della norma" : "Apri la guida"}">${norma ? "§ " : ""}<b>${esc(f.guida)}</b>${f.sezione && f.sezione !== f.guida ? " › " + esc(f.sezione) : ""}</button>`;
}

function isNorma(f) { return f.modulo === "Normativa" || String(f.path || "").startsWith("Normativa/"); }
function fontiHtml(fonti) {
  const g = fonti.filter((f) => !isNorma(f)), n = fonti.filter(isNorma);
  return (g.length ? `<div class="fonti">${g.map(fonteBtn).join("")}</div>` : "")
    + (n.length ? `<div class="fonti"><span class="tiny muted" style="align-self:center">Riferimenti normativi:</span>${n.map(fonteBtn).join("")}</div>` : "");
}

function bridgeHtml(f) {
  return `<div class="bridge ${f.stato}"><h4>${badge(f.stato)} Dall'assistenza alla formazione</h4>
    <div class="small">${f.nuovo ? "Il tuo profilo è stato aggiornato" : "Il tuo profilo segnala"} su <b>${esc(f.nome)}</b>:</div>
    <ul>${f.motivo.map((x) => `<li>${esc(x)}</li>`).join("")}</ul>
    <div class="row"><a class="btn sm" href="#/corso/${f.corso_id}">Ripasso di ${f.durata_min} minuti + quiz</a><span class="small muted">${esc(f.corso_titolo)} · ${f.n_domande} domande</span></div></div>`;
}

function ticketHtml(t, full = false) {
  const li = (a) => a && a.length ? `<ul>${a.map((x) => `<li>${esc(x)}</li>`).join("")}</ul>` : "<span class='muted'>—</span>";
  return `<div class="ticket"><div class="row"><span class="badge b-violet">${esc(t.codice || "Ticket")}</span><h4>${esc(t.oggetto)}</h4></div>
  <dl>
    <dt>Tipo</dt><dd>${esc(t.tipo_ticket)}</dd>
    <dt>Operatore</dt><dd>${esc(t.operatore.nome)} (${esc(t.operatore.id)}) · ${esc(t.operatore.ufficio)}<br><span class="small muted">${esc(t.operatore.ente)} · tel. ${esc(t.operatore.telefono)} · ${esc(t.operatore.email)}</span></dd>
    <dt>Modulo</dt><dd>${esc(t.modulo)} <span class="small muted">→ ${esc(t.destinatario)}</span></dd>
    <dt>Descrizione originale</dt><dd>“${esc(t.descrizione_originale)}”</dd>
    ${t.riassunto_tecnico ? `<dt>Riassunto tecnico (AI)</dt><dd>${esc(t.riassunto_tecnico)}</dd>` : ""}
    <dt>Diagnosi</dt><dd>${t.diagnosi && t.diagnosi.length ? t.diagnosi.map((d) => `<div><b>D:</b> ${esc(d.domanda)}<br><b>R:</b> ${esc(d.risposta)}</div>`).join("<br>") : "<span class='muted'>—</span>"}</dd>
    <dt>Tentativi già fatti</dt><dd>${li(t.tentativi)}</dd>
    <dt>Guide consultate</dt><dd>${t.guide_consultate && t.guide_consultate.length ? `<div class="fonti" style="margin:0">${t.guide_consultate.map(fonteBtn).join("")}</div>` : "<span class='muted'>—</span>"}</dd>
    ${"classificazione" in t ? `<dt>Classificazione</dt><dd>${classHtml(t.classificazione)}</dd>` : ""}
    <dt>Motivo dell'inoltro</dt><dd>${esc(t.motivo_escalation || "—")}</dd>
    <dt>Formato</dt><dd class="small">${(t.conformita || []).map((c) => `<span class="check">✓</span> ${esc(c)}`).join(" &nbsp; ")}<br><span class="muted">Requisiti della Comunicazione Palitalsoft 01/2024 sulle richieste di assistenza · ${esc(t.generato_da || "")}</span></dd>
  </dl></div>`;
}

function isClassified(c) { return c && c.argomento && c.argomento !== "ALTRO"; }
function classHtml(c) {
  if (!isClassified(c)) return `<span class="badge b-orange">Da classificare</span> <span class="small muted">${c ? "nessun argomento riconosciuto" : "servizio AI non disponibile all'invio"}: lo classificherà il tecnico</span>`;
  return `<span class="badge b-blue">${esc((S.argomenti[c.argomento] || {}).nome || c.argomento)}</span> <span class="badge ${c.tipo === "anomalia" ? "b-grey" : "b-orange"}">${TIPO_LABEL[c.tipo] || c.tipo}</span>
    <span class="small muted">· da ${esc(c.da)}${c.motivazione ? " – " + esc(c.motivazione) : ""}</span>`;
}

function drawSide() {
  const c = chatState(), steps = $("#steps");
  if (!steps) return;
  const last = [...c.msgs].reverse().find((m) => m.ruolo === "agente");
  const e = last?.esito;
  const S1 = [["Comprensione della richiesta", c.msgs.length ? "done" : "cur"],
    ["Ricerca nelle guide", e ? "done" : c.msgs.length ? "cur" : ""],
    [e === "chiarimento" ? "Domanda di chiarimento" : "Chiarimenti (se servono)", e === "chiarimento" ? "cur" : e ? "done" : ""],
    e === "escalation" ? ["Inoltro al tecnico con ticket", "esc"] : e === "coda" ? ["Coda di emergenza (AI non disponibile)", "coda"] : ["Risposta con le fonti", ["risolto", "guida_suggerita"].includes(e) ? "done" : ""]];
  steps.innerHTML = S1.map(([l, cl], i) => `<li class="${cl}"><span class="dot">${cl === "done" ? "✓" : i + 1}</span>${l}</li>`).join("");
  const fonti = [...c.msgs].reverse().find((m) => m.fonti && m.fonti.length)?.fonti || [];
  $("#side-fonti").innerHTML = fonti.length ? `<div class="fonti" style="margin:0">${fonti.map(fonteBtn).join("")}</div>` : "Le guide usate per la risposta compariranno qui.";
  bindMsgActions($("#side-fonti"));
}

function bindMsgActions(root) {
  $$(".fonte", root).forEach((b) => b.onclick = () => openGuide(b.dataset.path, b.dataset.anchor));
  $$("[data-fb]", root).forEach((b) => b.onclick = () => feedback(b.dataset.fb));
}

async function send(text) {
  const c = chatState();
  if (S.busy) return;
  if (c.closed) { c.convId = null; c.msgs = []; c.closed = false; }
  c.msgs.push({ ruolo: "operatore", testo: text });
  S.busy = true; drawChat();
  const inp = $("#chat-in"); if (inp) inp.value = "";
  try {
    const r = await api("/api/chat", { operatore_id: S.who, conversazione_id: c.convId, messaggio: text });
    c.convId = r.conversazione_id; c.closed = r.stato_conversazione !== "aperta";
    c.msgs.push({ ruolo: "agente", ...r });
    if (r.esito === "coda") poll();
  } catch (e) {
    c.msgs.push({ ruolo: "agente", esito: "coda", testo: `Errore di comunicazione con il server: ${e.message}. Puoi consultare i manuali o aprire un ticket.` });
  } finally { S.busy = false; drawChat(); $("#chat-in")?.focus(); }
}

async function feedback(kind) {
  const c = chatState(), last = c.msgs[c.msgs.length - 1];
  if (kind === "ok") { last.feedback = "ok"; drawChat(); return; }
  modal(`<h2>Inoltra al tecnico</h2><p class="muted">L'assistente preparerà il ticket includendo la soluzione già provata, così il tecnico non riparte da zero.</p>
    <form id="ko"><label class="field"><span>Cosa è successo quando hai provato?</span><textarea id="ko-t" rows="3" placeholder="Es. ho seguito i passi ma il problema si ripresenta…"></textarea></label>
    <button class="btn">Genera il ticket</button></form>`);
  $("#ko").addEventListener("submit", async (e) => {
    e.preventDefault(); closeModal();
    const motivo = $("#ko-t").value.trim() || "La soluzione proposta non ha risolto il problema";
    last.feedback = "ko"; c.msgs.push({ ruolo: "operatore", testo: `Non ha funzionato: ${motivo}` });
    S.busy = true; drawChat();
    try { const r = await api("/api/chat/escalation", { conversazione_id: c.convId, motivo }); c.msgs.push({ ruolo: "agente", ...r, fonti: [] }); c.closed = true; }
    catch (err) { toast(err.message); }
    finally { S.busy = false; drawChat(); }
  });
}

/* ------------------------------------------------------------------ guida in finestra */
async function openGuide(path, anchor) {
  const d = await api(`/api/guida?path=${encodeURIComponent(path)}`);
  modal(`<div class="tiny muted">${esc(d.doc?.modulo || "")} · ${esc(path)}</div>${md(d.testo)}
    <div class="row" style="margin-top:14px"><a class="btn secondary sm" href="#/manuali?path=${encodeURIComponent(path)}${anchor ? "&anchor=" + anchor : ""}" onclick="closeModal()">Apri nei manuali</a></div>`);
  if (anchor) { const h = $("#h-" + CSS.escape(anchor), $("#modal-body")); if (h) { h.classList.add("hl"); setTimeout(() => h.scrollIntoView({ block: "start" }), 30); } }
}

/* ------------------------------------------------------------------ MANUALI */
async function viewManuals(v, params) {
  S.docs ||= await api("/api/guide");
  v.innerHTML = `<h1>Manuali</h1><p class="lead">Consultazione diretta della documentazione: funziona sempre, anche senza l'assistente.</p>
  <div class="manuali">
    <div class="card" style="padding:12px"><input type="text" id="doc-q" placeholder="Cerca nelle guide (es. scartare una mail)" aria-label="Cerca nelle guide"><div class="doclist" id="doclist"></div></div>
    <div class="card docview" id="docview"><p class="muted">Seleziona una guida dall'elenco o cerca un argomento.</p></div>
  </div>`;
  const list = $("#doclist");
  const drawList = (filter = "") => {
    const f = filter.toLowerCase(); let mod = "", h = "";
    S.docs.filter((d) => d.tipo !== "allegato" && (!f || d.titolo.toLowerCase().includes(f))).forEach((d) => {
      if (d.modulo !== mod) { mod = d.modulo; h += `<div class="mod">${esc(mod)}</div>`; }
      h += `<button data-path="${esc(d.path)}">${d.tipo === "video" ? "▶ " : ""}${esc(d.titolo)}</button>`;
    });
    list.innerHTML = h || "<p class='muted small'>Nessun titolo corrisponde.</p>";
    bindList();
  };
  const bindList = () => $$("button[data-path]", list).forEach((b) => b.onclick = () => showDoc(b.dataset.path, b.dataset.anchor));
  const showDoc = async (path, anchor) => {
    $$("button", list).forEach((b) => b.classList.toggle("active", b.dataset.path === path && (b.dataset.anchor || "") === (anchor || "")));
    const d = await api(`/api/guida?path=${encodeURIComponent(path)}`);
    $("#docview").innerHTML = `<div class="tiny muted">${esc(d.doc?.modulo || "")} · ${esc(path)}</div>${md(d.testo)}`;
    if (anchor) { const h = $("#h-" + CSS.escape(anchor)); if (h) { h.classList.add("hl"); h.scrollIntoView({ block: "center" }); } }
    else $("#docview").scrollIntoView({ block: "start" });
  };
  let tmr;
  $("#doc-q").addEventListener("input", (e) => {
    clearTimeout(tmr); const val = e.target.value.trim();
    if (val.split(/\s+/).length < 2) return drawList(val);
    tmr = setTimeout(async () => {
      const res = await api(`/api/cerca?q=${encodeURIComponent(val)}`);
      list.innerHTML = `<div class="mod">Sezioni più pertinenti</div>` + res.map((r) => `<button class="res" data-path="${esc(r.path)}" data-anchor="${esc(r.anchor)}">${esc(r.sezione)}<small>${esc(r.modulo)} · ${esc(r.guida)}</small></button>`).join("");
      bindList();
    }, 250);
  });
  drawList();
  if (params.get("path")) showDoc(params.get("path"), params.get("anchor"));
}

/* ------------------------------------------------------------------ TICKET manuale */
function viewTicketForm(v) {
  const op = me();
  v.innerHTML = `<h1>Apri un ticket</h1><p class="lead">Il canale tradizionale resta sempre disponibile, anche quando l'assistente AI non risponde.</p>
  <div class="grid g2">
    <form class="card" id="tf">
      <label class="field"><span>Oggetto <span class="hint">– specifico, non “Richiesta assistenza” o “Aiuto”</span></span><input type="text" id="tf-o" required></label>
      <label class="field"><span>Modulo</span><select class="input" id="tf-m"><option>Protocollo</option><option>Servizi Demografici</option><option>Altro</option></select></label>
      <label class="field"><span>Tipo di richiesta</span><select class="input" id="tf-t">
        <option>Richiesta assistenza per errore/anomalia</option><option selected>Richiesta assistenza per supporto operativo</option><option>Richiesta formazione/consulenza</option></select></label>
      <label class="field"><span>Descrizione dettagliata</span><textarea id="tf-d" rows="6" required placeholder="Cosa stavi facendo, in quale funzione, quale messaggio è comparso…"></textarea></label>
      <div id="tf-sugg"></div>
      <p class="small muted">Firma e recapiti vengono aggiunti in automatico: ${esc(op.nome)} · ${esc(op.ufficio)} · tel. ${esc(op.telefono)}</p>
      <div class="row"><button class="btn">Invia il ticket</button><span id="tf-err" class="small" style="color:var(--red)"></span></div>
    </form>
    <div class="card explainer"><h3>Come scrivere un ticket efficace</h3>
      <p class="small">Dalla Comunicazione Palitalsoft 01/2024 sulle modalità di richiesta assistenza:</p>
      <ul class="small"><li>i ticket con oggetto vuoto o troppo generico non vengono presi in carico;</li><li>serve una spiegazione dettagliata, meglio con screenshot o allegati;</li>
      <li>vanno sempre indicati firma e recapiti di chi chiede assistenza;</li><li>un ticket per ogni problema, senza rispondere alla mail automatica di un altro ticket.</li></ul>
      <p class="small">Prima di aprirlo puoi provare l'<a href="#/assistente">assistente</a>: risolve i casi documentati e, se non ci riesce, compila il ticket per te.</p></div>
  </div><div id="tf-out"></div>`;
  let st, seq = 0;
  const suggest = () => {
    clearTimeout(st);
    st = setTimeout(async () => {
      const txt = `${$("#tf-o").value} ${$("#tf-d").value}`.trim(), my = ++seq;
      if (txt.length < 15) { $("#tf-sugg").innerHTML = ""; return; }
      let res = [];
      try { res = (await api(`/api/cerca?q=${encodeURIComponent(txt)}`)).filter((r) => r.punteggio >= 10).slice(0, 3); } catch { /* ricerca non disponibile */ }
      if (my !== seq) return;
      $("#tf-sugg").innerHTML = res.length ? `<div class="bridge" style="background:var(--blue-l);border-color:#bcd6f2;margin:0 0 14px">
        <h4>Prima di inviare: queste guide potrebbero esserti utili</h4>
        <div class="fonti">${res.map((r) => fonteBtn({ path: r.path, anchor: r.anchor, guida: r.guida, sezione: r.sezione })).join("")}</div>
        <div class="small muted" style="margin-top:6px">Se non risolvono, invia pure il ticket.</div></div>` : "";
      bindMsgActions($("#tf-sugg"));
    }, 500);
  };
  $("#tf-o").addEventListener("input", suggest);
  $("#tf-d").addEventListener("input", suggest);
  $("#tf").addEventListener("submit", async (e) => {
    e.preventDefault();
    const o = $("#tf-o").value.trim();
    if (/^(richiesta( di)? assistenza|aiuto!*|errore( cityware.*)?|problema|help)$/i.test(o)) { $("#tf-err").textContent = "Oggetto troppo generico: indica il problema (es. “PROTOCOLLO – PEC senza allegati”)."; return; }
    try {
      const t = await api("/api/ticket", { operatore_id: S.who, oggetto: o, modulo: $("#tf-m").value, tipo_ticket: $("#tf-t").value, descrizione: $("#tf-d").value });
      $("#tf-out").innerHTML = `<div class="card" style="margin-top:16px"><h2>Ticket inviato</h2>${ticketHtml(t)}${t.formazione ? bridgeHtml(t.formazione) : ""}</div>`;
      bindMsgActions($("#tf-out")); $("#tf").reset(); $("#tf-err").textContent = ""; $("#tf-sugg").innerHTML = "";
      $("#tf-out").scrollIntoView({ behavior: "smooth", block: "start" });
    } catch (err) { $("#tf-err").textContent = err.message; }
  });
}

/* ------------------------------------------------------------------ FORMAZIONE */
async function viewCatalog(v, personal) {
  const [corsi, prof] = await Promise.all([api("/api/corsi"), personal ? api(`/api/profilo/${S.who}`) : null]);
  const byArg = {}; (prof?.argomenti || []).forEach((a) => byArg[a.argomento] = a);
  const mods = [...new Set(corsi.map((c) => c.modulo))];
  v.innerHTML = `<h1>${personal ? "Formazione" : "Corsi e quiz"}</h1>
  <p class="lead">Brevi moduli tematici costruiti sulle guide e sulle videoguide Palitalsoft. Ogni domanda dei quiz cita la guida da cui è tratta.</p>
  ${mods.map((m) => `<div class="section-title"><h2>${esc(m)}</h2></div><div class="grid g3">${corsi.filter((c) => c.modulo === m).map((c) => {
    const a = byArg[c.argomento]; const rec = a && ["lacuna", "da_verificare"].includes(a.stato);
    return `<div class="card course ${rec ? "rec " + a.stato : ""}">
      <div class="top">${rec ? `<span class="badge b-${a.stato}">Consigliato per te</span>` : ""}${a?.corso_completato ? '<span class="badge b-green">Completato</span>' : ""}<span class="badge b-grey">${c.durata_min} min</span></div>
      <h3>${esc(c.titolo)}</h3><div class="small muted">${c.n_unita} unità · quiz di ${c.n_domande} domande${a?.ultimo_quiz ? ` · ultimo quiz ${a.ultimo_quiz.punteggio}%` : ""}</div>
      ${rec ? `<div class="small">${esc(a.motivo[0])}</div>` : ""}
      <div><a class="btn ${rec ? "" : "secondary"} sm" href="#/corso/${c.id}">${a?.corso_completato ? "Ripassa" : "Inizia"}</a></div></div>`;
  }).join("")}</div>`).join("")}`;
}

async function viewCourse(v, id) {
  id = (id || "").split("#")[0];
  const opId = role() === "operatore" ? S.who : "";
  const [c, prof] = await Promise.all([api(`/api/corso/${id}?op=${opId}`), opId ? api(`/api/profilo/${opId}`) : null]);
  const a = prof?.argomenti.find((x) => x.argomento === c.argomento);
  const vidCount = c.unita.filter((u) => u.tipo === "video").length;
  v.innerHTML = `<div class="small"><a href="#/${role() === "operatore" ? "formazione" : "catalogo"}">← Tutti i corsi</a></div>
  <h1 style="margin-top:6px">${esc(c.titolo)}</h1>
  <p class="lead">${esc(c.modulo)} · ${esc(c.argomento_nome)} · ${c.durata_min} minuti · ${c.unita.length} unità${vidCount ? ` (${vidCount} videoguide)` : ""} · quiz finale</p>
  ${a && ["lacuna", "da_verificare"].includes(a.stato) ? `<div class="bridge ${a.stato}" style="margin:0 0 18px"><h4>${badge(a.stato)} Perché ti proponiamo questo corso</h4><ul>${a.motivo.map((m) => `<li>${esc(m)}</li>`).join("")}</ul></div>` : ""}
  <div class="stack">${c.unita.map((u, i) => `<div class="unit"><div class="unit-head" data-u="${i}"><span class="n">${i + 1}</span><b style="flex:1">${esc(u.titolo)}</b>
      <span class="badge ${u.tipo === "video" ? "b-blue" : u.tipo === "faq" ? "b-orange" : "b-grey"}">${u.tipo === "video" ? "Videoguida" : u.tipo === "faq" ? "FAQ" : "Guida"}</span></div>
    <div class="unit-body" ${i ? "hidden" : ""}>${u.tipo === "video" ? `<div class="video"><div><div class="play"><svg width="22" height="22" viewBox="0 0 24 24"><path d="M8 5v14l11-7z" fill="#fff"/></svg></div>
      <b>Videoguida: ${esc(u.titolo)}</b><br><small>Segnaposto: nella versione reale qui viene riprodotto il video tutorial Palitalsoft. Sotto i passaggi descritti nel video.</small></div></div>` : ""}
      ${md(u.testo)}<div class="fonti">${fonteBtn({ path: u.path, anchor: u.anchor, guida: u.guida, sezione: u.titolo })}</div></div></div>`).join("")}</div>
  <div class="section-title" id="quiz"><h2>Quiz di verifica</h2><span class="muted small">${c.quiz.length} domande · superato dal 75%</span></div>
  ${c.storico.length ? `<p class="small muted">Tentativi precedenti: ${c.storico.map((s) => `${s.punteggio}% (${fmtDate(s.data)})`).join(" · ")}</p>` : ""}
  ${opId ? `<form id="quiz-f">${c.quiz.map((q, i) => `<div class="quiz-q"><fieldset><legend>${i + 1}. ${esc(q.domanda)}</legend>
    ${q.opzioni.map((o, j) => `<label class="opt" data-q="${i}" data-o="${j}"><input type="radio" name="q${i}" value="${j}" required> <span>${esc(o)}</span></label>`).join("")}</fieldset>
    <div class="qx small" data-qx="${i}"></div></div>`).join("")}
    <div class="row" style="margin-top:14px"><button class="btn" id="quiz-btn">Consegna il quiz</button></div></form><div id="quiz-res" style="margin-top:16px"></div>`
    : `<div class="card"><p class="muted" style="margin:0">Anteprima per il responsabile: il quiz si compila accedendo come operatore.</p><ol>${c.quiz.map((q) => `<li>${esc(q.domanda)}</li>`).join("")}</ol></div>`}`;
  $$(".unit-head", v).forEach((h) => h.addEventListener("click", () => { const b = h.nextElementSibling; b.hidden = !b.hidden; }));
  bindMsgActions(v);
  if (location.hash.endsWith("#quiz")) $("#quiz").scrollIntoView();
  const f = $("#quiz-f");
  if (!f) return;
  f.addEventListener("submit", async (e) => {
    e.preventDefault();
    const risposte = c.quiz.map((_, i) => +((f.querySelector(`input[name=q${i}]:checked`) || {}).value ?? -1));
    const r = await api(`/api/quiz/${id}`, { operatore_id: S.who, risposte });
    r.dettaglio.forEach((d, i) => {
      $$(`.opt[data-q="${i}"]`, f).forEach((l) => { const o = +l.dataset.o; l.classList.toggle("right", o === d.corretta); l.classList.toggle("wrong", o === d.data && !d.ok); });
      $(`[data-qx="${i}"]`, f).innerHTML = `<div style="margin-top:6px"><b style="color:${d.ok ? "var(--green)" : "var(--red)"}">${d.ok ? "Corretto." : "Non corretto."}</b> ${esc(d.spiegazione)}</div>
        <div class="fonti">${fonteBtn({ path: d.fonte.path, anchor: slug(d.fonte.sezione.split(" › ").pop()), guida: d.fonte.sezione, sezione: "" })}</div>`;
    });
    $$("input", f).forEach((i) => i.disabled = true); $("#quiz-btn").remove();
    const pr = r.prima, dp = r.dopo;
    $("#quiz-res").innerHTML = `<div class="result ${r.superato ? "ok" : "ko"}"><div class="row"><span class="score">${r.punteggio}%</span>
      <div><b>${r.superato ? "Quiz superato" : "Quiz non superato"}</b> · ${r.corrette} risposte corrette su ${r.totale}</div></div>
      <div>Profilo su <b>${esc(c.argomento_nome)}</b>: ${pr ? badge(pr.stato) : '<span class="badge b-grey">nessun dato</span>'} → ${dp ? badge(dp.stato) : ""}</div>
      ${dp?.verifica_periodica ? `<div class="small">${r.superato ? "Verifica periodica programmata" : "Ti riproporremo il quiz"} dal <b>${fmtDate(dp.verifica_periodica)}</b>, per controllare che le conoscenze restino nel tempo.</div>` : ""}
      <div class="row"><a class="btn secondary sm" href="#/profilo">Vai al mio profilo</a>${r.superato ? "" : `<button class="btn sm" onclick="location.reload()">Ripassa e riprova</button>`}</div></div>`;
    bindMsgActions(f);
    $("#quiz-res").scrollIntoView({ block: "center", behavior: "smooth" });
  });
}

/* ------------------------------------------------------------------ PROFILO */
async function viewProfile(v, opId) {
  const p = await api(`/api/profilo/${opId}`);
  const op = p.operatore, own = opId === S.who;
  const color = { lacuna: "var(--red)", da_verificare: "#e08e1a", in_crescita: "#5a9ae0", competente: "var(--green)", segnale_debole: "#a7b4c2" };
  const cnt = (s) => p.argomenti.filter((a) => a.stato === s).length;
  v.innerHTML = `${!own ? `<div class="small"><a href="#/dashboard">← Dashboard</a></div>` : ""}
  <h1>${own ? "Il mio profilo" : esc(op.nome)}</h1><p class="lead">${esc(op.nome)} · ${esc(op.ufficio)} · ${esc(op.ente)}</p>
  <div class="grid g4">
    <div class="card kpi"><div class="v" style="color:var(--red)">${cnt("lacuna")}</div><div class="l">Lacune confermate</div></div>
    <div class="card kpi"><div class="v" style="color:var(--orange)">${cnt("da_verificare")}</div><div class="l">Possibili lacune da verificare</div></div>
    <div class="card kpi"><div class="v" style="color:var(--green)">${cnt("competente")}</div><div class="l">Argomenti padroneggiati</div></div>
    <div class="card kpi"><div class="v">${p.argomenti.reduce((s, a) => s + a.n_supporto, 0)}</div><div class="l">Richieste di supporto (90 giorni)</div></div>
  </div>
  <div class="section-title"><h2>Competenze per argomento</h2></div>
  <div class="stack">${p.argomenti.length ? p.argomenti.map((a) => `<div class="card topic">
    <div><div class="row"><h3 style="margin:0">${esc(a.nome)}</h3>${badge(a.stato)}<span class="badge b-grey">${esc(a.modulo)}</span></div>
      <ul class="why">${a.motivo.map((m) => `<li>${esc(m)}</li>`).join("")}</ul>
      ${a.evidenze.length ? `<ul class="list evid">${a.evidenze.map((e) => `<li><span class="muted">${fmtDate(e.data)}</span><span style="flex:1">“${esc(e.testo)}”</span><span class="badge ${e.tipo === "anomalia" ? "b-grey" : "b-orange"}">${TIPO_LABEL[e.tipo] || e.tipo}</span></li>`).join("")}</ul>` : ""}
    </div>
    <div><div class="small muted">Competenza ${a.stimata ? "(stima dalle richieste)" : "(dal quiz)"}</div>
      <div class="row"><div class="bar" style="flex:1"><i style="width:${a.competenza}%;background:${color[a.stato]}"></i></div><b>${a.competenza}%</b></div>
      ${a.storico_quiz.length ? `<div class="small muted" style="margin-top:6px">Quiz: ${a.storico_quiz.map((s) => s.punteggio + "%").join(" → ")}</div>` : ""}
      ${a.verifica_periodica ? `<div class="small" style="margin-top:4px">${a.verifica_scaduta ? `<span class="badge b-blue">${a.stato === "lacuna" ? "Quiz da ripetere" : "Verifica periodica disponibile"}</span>` : "Prossima verifica: " + fmtDate(a.verifica_periodica)}</div>` : ""}
      ${a.corso && own ? `<div style="margin-top:10px"><a class="btn ${["lacuna", "da_verificare"].includes(a.stato) ? "" : "secondary"} sm" href="#/corso/${a.corso}${a.verifica_scaduta && a.stato === "competente" ? "#quiz" : ""}">${["lacuna", "da_verificare"].includes(a.stato) ? "Inizia il ripasso" : a.verifica_scaduta ? "Verifica" : "Ripassa"}</a></div>` : ""}
    </div></div>`).join("") : `<div class="card muted">Ancora nessun dato: il profilo si costruisce con le richieste all'assistente e i quiz.</div>`}</div>
  <div class="card explainer" style="margin-top:20px"><h3>Come viene calcolato il profilo</h3>
    <ul class="small">
      <li>Contano solo le richieste di <b>supporto operativo</b> (“come si fa”) degli ultimi 90 giorni. Le segnalazioni di <b>anomalie del software</b> non sono considerate lacune.</li>
      <li>Due o più richieste sullo stesso argomento indicano una <b>possibile lacuna</b>: un ticket da solo non dimostra che l'operatore non conosca la procedura, quindi la piattaforma propone un ripasso con quiz per <b>confermarla o escluderla</b>.</li>
      <li>Un quiz sotto il 60% conferma la <b>lacuna</b>; dal 75% l'argomento è <b>padroneggiato</b>, anche se le richieste erano frequenti (probabile caso raro o di configurazione).</li>
      <li>I quiz vengono riproposti nel tempo: dopo 2 giorni se non superati, poi dopo 7 e 30 giorni per verificare che le conoscenze restino.</li>
    </ul></div>`;
}

/* ------------------------------------------------------------------ HELP DESK */
async function viewQueue(v) {
  const d = await api("/api/coda");
  S.stato = d.stato; renderStatus();
  const down = d.stato.motore === "down", job = d.stato.job_coda;
  const att = d.elementi.filter((e) => e.stato === "in_attesa"), chiusi = d.elementi.filter((e) => e.stato !== "in_attesa");
  const opts = Object.entries(S.argomenti).map(([k, a]) => `<option value="${k}">${esc(a.nome)}</option>`).join("");
  v.innerHTML = `<h1>Coda di emergenza</h1>
  <p class="lead">Quando il servizio AI non è disponibile, ogni richiesta viene salvata qui. I tecnici possono risolverle manualmente; al ripristino l'AI riparte dalle richieste ancora aperte, saltando quelle già chiuse.</p>
  <div class="card row" style="margin-bottom:16px"><div><b>Stato del servizio AI:</b> ${down ? '<span class="badge b-red">Non disponibile</span>' : '<span class="badge b-green">Attivo</span>'}
    <span class="small muted"> · ${att.length} in attesa · ${chiusi.filter((e) => e.stato === "risolta_manuale").length} risolte dai tecnici · ${chiusi.filter((e) => e.stato === "elaborata_ai").length} elaborate dall'AI</span></div>
    <span class="spacer"></span><button class="btn ${down ? "success" : "danger"} sm" id="toggle">${down ? "Ripristina il servizio AI" : "Simula un guasto dell'AI"}</button></div>
  ${job && job.log && job.log.length ? `<div class="log" style="margin-bottom:16px">${job.log.map((l) => `<div>${esc(l)}</div>`).join("")}${job.attivo ? "<div>…</div>" : ""}</div>` : ""}
  <h2>In attesa (${att.length})</h2>
  ${att.length ? att.map((e) => `<div class="queue-item"><div class="row"><span class="badge b-red">#${e.id}</span><b>${esc(e.operatore_nome)}</b><span class="muted small">${esc(e.ufficio)} · ${fmtDT(e.creata)}</span></div>
    <p style="margin:8px 0">“${esc(e.testo)}”</p>
    <details><summary class="small" style="cursor:pointer;color:var(--blue)">Risolvi manualmente</summary>
      <form class="grid g3" data-res="${e.id}" style="margin-top:10px">
        <label class="field"><span>Argomento</span><select class="input" name="argomento">${opts}</select></label>
        <label class="field"><span>Tipo</span><select class="input" name="tipo"><option value="supporto_operativo">Supporto operativo</option><option value="anomalia">Anomalia software</option><option value="formazione">Formazione</option></select></label>
        <label class="field" style="grid-column:1/-1"><span>Risposta data all'operatore</span><textarea name="nota" rows="2" placeholder="Es. spiegato al telefono come caricare l'allegato con Da File"></textarea></label>
        <div><button class="btn sm">Segna come risolta</button></div></form></details></div>`).join("") : `<p class="muted">Nessuna richiesta in attesa.</p>`}
  ${chiusi.length ? `<h2 style="margin-top:24px">Chiuse</h2>${chiusi.map((e) => `<div class="queue-item done"><div class="row"><span class="badge b-grey">#${e.id}</span><b>${esc(e.operatore_nome)}</b>
    ${e.stato === "risolta_manuale" ? '<span class="badge b-blue">Risolta dal tecnico</span>' : `<span class="badge b-green">Elaborata dall'AI · ${e.esito_ai === "escalation" ? "ticket generato" : "risposta inviata"}</span>`}
    <span class="muted small">${fmtDT(e.chiusa)}</span></div><p class="small" style="margin:6px 0 0">“${esc(e.testo)}”${e.stato === "risolta_manuale" ? ` → ${esc(e.nota)}` : ""}</p></div>`).join("")}` : ""}`;
  $("#toggle").addEventListener("click", async () => {
    try { await api("/api/motore", { motore: down ? (S.stato.openai_disponibile ? "openai" : "offline") : "down" }); await poll(); route(); } catch (e) { toast(e.message); }
  });
  $$("form[data-res]", v).forEach((f) => f.addEventListener("submit", async (e) => {
    e.preventDefault(); const fd = new FormData(f);
    await api(`/api/coda/${f.dataset.res}/risolvi`, { argomento: fd.get("argomento"), tipo: fd.get("tipo"), nota: fd.get("nota"), tecnico: me().nome });
    toast("Richiesta segnata come risolta"); poll(); route();
  }));
}

async function viewTickets(v) {
  const ts = await api("/api/ticket");
  v.innerHTML = `<h1>Ticket ricevuti</h1><p class="lead">Ticket generati dall'assistente (con diagnosi e riepilogo) o aperti manualmente dagli operatori.</p>
  <div class="card">${ts.length ? `<table class="t"><thead><tr><th>Codice</th><th>Oggetto</th><th>Operatore</th><th>Tipo</th><th>Origine</th><th>Classificazione</th><th>Data</th></tr></thead><tbody>
  ${ts.map((t, i) => `<tr class="click" data-i="${i}"><td><b>${esc(t.codice)}</b></td><td>${esc(t.dati.oggetto)}</td><td>${esc(t.operatore_nome)}</td><td class="small">${esc(t.dati.tipo_ticket)}</td>
    <td>${t.origine === "agente" ? '<span class="badge b-violet">Assistente AI</span>' : '<span class="badge b-grey">Manuale</span>'}</td>
    <td>${!("classificazione" in t.dati) ? '<span class="small muted">dalla conversazione</span>' : isClassified(t.dati.classificazione) ? `<span class="badge b-blue">${esc((S.argomenti[t.dati.classificazione.argomento] || {}).nome)}</span>` : '<span class="badge b-orange">Da classificare</span>'}</td>
    <td class="small">${fmtDT(t.creato)}</td></tr>`).join("")}</tbody></table>`
    : `<p class="muted" style="margin:0">Nessun ticket ancora. Prova un caso di escalation dall'assistente (profilo operatore).</p>`}</div>`;
  const opts = Object.entries(S.argomenti).filter(([k]) => k !== "ALTRO").map(([k, a]) => `<option value="${k}">${esc(a.nome)}</option>`).join("");
  $$("tr[data-i]", v).forEach((r) => r.addEventListener("click", () => {
    const t = ts[+r.dataset.i], needs = "classificazione" in t.dati && !isClassified(t.dati.classificazione);
    modal(`<h2>Dettaglio ticket</h2>${ticketHtml({ codice: t.codice, ...t.dati }, true)}
      ${needs ? `<form id="cls" class="card" style="margin-top:14px;box-shadow:none"><h3>Classifica il ticket</h3>
        <p class="small muted" style="margin-top:0">Serve per aggiornare il profilo competenze dell'operatore (le anomalie software non contano come lacune).</p>
        <div class="grid g2"><label class="field"><span>Argomento</span><select class="input" name="argomento">${opts}</select></label>
        <label class="field"><span>Tipo</span><select class="input" name="tipo"><option value="supporto_operativo">Supporto operativo</option><option value="anomalia">Anomalia software</option><option value="formazione">Formazione</option></select></label></div>
        <button class="btn sm">Salva classificazione</button></form>` : ""}`);
    bindMsgActions($("#modal-body"));
    $("#cls")?.addEventListener("submit", async (e) => {
      e.preventDefault(); const fd = new FormData(e.target);
      try { await api(`/api/ticket/${t.id}/classifica`, { argomento: fd.get("argomento"), tipo: fd.get("tipo"), tecnico: me().nome }); closeModal(); toast("Ticket classificato: profilo dell'operatore aggiornato"); route(); }
      catch (err) { toast(err.message); }
    });
  }));
}

/* ------------------------------------------------------------------ DASHBOARD responsabile */
async function viewDashboard(v) {
  const d = await api("/api/dashboard"), k = d.kpi;
  const pct = k.richieste_90 ? Math.round(100 * k.risolte_ai_90 / k.richieste_90) : 0;
  const maxSup = Math.max(1, ...d.argomenti.map((a) => a.supporto));
  v.innerHTML = `<h1>Dashboard formazione</h1><p class="lead">Dove si concentrano le difficoltà degli operatori e come evolvono le competenze. <span class="badge b-grey">dati di esempio</span></p>
  <div class="grid g5">
    <div class="card kpi"><div class="v">${k.richieste_90}</div><div class="l">Richieste (90 giorni)</div></div>
    <div class="card kpi"><div class="v" style="color:var(--green)">${pct}%</div><div class="l">Risolte senza ticket</div><div class="s muted">${k.risolte_ai_90} su ${k.richieste_90}</div></div>
    <div class="card kpi"><div class="v" style="color:var(--red)">${k.lacune_aperte}</div><div class="l">Lacune confermate</div></div>
    <div class="card kpi"><div class="v" style="color:var(--orange)">${k.da_verificare}</div><div class="l">Possibili lacune</div></div>
    <div class="card kpi"><div class="v">${k.corsi_completati}</div><div class="l">Percorsi completati</div><div class="s muted">${k.quiz_svolti} quiz svolti</div></div>
  </div>
  <div class="grid g2" style="margin-top:16px">
    <div class="card"><h2>Andamento mensile</h2>${trendChart(d.trend)}</div>
  <div class="card"><h2>Percorsi formativi completati</h2>
    <table class="t"><tbody>${d.corsi.map((c) => `<tr><td>${esc(c.titolo)}</td><td style="width:50%"><div class="row" style="flex-wrap:nowrap"><div class="hbar" style="background:var(--green);width:${Math.max(4, 22 * c.completati)}px;max-width:100%"></div><span>${c.completati}</span></div></td></tr>`).join("")}</tbody></table></div>
  </div>
  <div class="card" style="margin-top:16px"><h2>Argomenti critici</h2><table class="t"><thead><tr><th>Argomento</th><th>Richieste “come si fa”</th><th>Media quiz</th><th>Operatori</th></tr></thead><tbody>
      ${d.argomenti.map((a) => `<tr><td><b>${esc(a.nome)}</b><div class="tiny muted">${esc(a.modulo)}</div></td>
        <td><div class="row" style="flex-wrap:nowrap"><div class="hbar" style="width:${Math.max(4, 90 * a.supporto / maxSup)}px"></div><span>${a.supporto}</span></div></td>
        <td>${a.media_quiz == null ? "—" : `<b style="color:${a.media_quiz < 60 ? "var(--red)" : a.media_quiz < 75 ? "var(--orange)" : "var(--green)"}">${a.media_quiz}%</b>`}</td>
        <td>${a.lacune ? `<span class="badge b-lacuna">${a.lacune} lacun${a.lacune > 1 ? "e" : "a"}</span> ` : ""}${a.da_verificare ? `<span class="badge b-da_verificare">${a.da_verificare} da verificare</span>` : ""}</td></tr>`).join("")}
    </tbody></table></div>
  <div class="card" style="margin-top:16px"><div class="row"><h2 style="margin:0">Mappa delle competenze</h2><span class="spacer"></span>
    <div class="legend">${Object.entries(STATO_LABEL).map(([s, l]) => `<span><i class="c-${s}"></i>${l}</span>`).join("")}<span><i class="c-none"></i>Nessun dato</span></div></div>
    <p class="small muted">Clicca su un operatore per aprire il suo profilo e vedere le evidenze.</p>
    <div class="matrix"><table><thead><tr><th></th>${d.colonne.map((c) => `<th class="rot"><div>${esc(c.nome)}</div></th>`).join("")}<th class="rot"><div>Corsi completati</div></th></tr></thead><tbody>
    ${d.matrice.map((r) => `<tr><td class="name" data-op="${r.id}"><b>${esc(r.nome)}</b> <span class="tiny muted">${esc(r.ufficio)}</span></td>
      ${d.colonne.map((c) => { const s = r.stati[c.code]; return `<td class="cell c-${s ? s.stato : "none"}" title="${s ? STATO_LABEL[s.stato] + " · " + s.competenza + "%" : "nessun dato"}">${s && s.stato !== "segnale_debole" ? s.competenza : ""}</td>`; }).join("")}
      <td class="cell c-none">${r.corsi_completati}</td></tr>`).join("")}</tbody></table></div></div>
`;
  $$("[data-op]", v).forEach((t) => t.addEventListener("click", () => location.hash = `#/profilo/${t.dataset.op}`));
}

function trendChart(t) {
  const W = 560, H = 250, L = 36, R = 40, T = 16, B = 42, iw = W - L - R, ih = H - T - B;
  const max = Math.max(5, ...t.map((x) => x.richieste)), bw = iw / t.length * 0.56;
  const x = (i) => L + iw / t.length * (i + 0.5), y = (vv) => T + ih - ih * vv / max, yq = (vv) => T + ih - ih * vv / 100;
  let s = `<svg class="chart" viewBox="0 0 ${W} ${H}" role="img" aria-label="Richieste mensili risolte dall'assistente e inoltrate, con media dei quiz">`;
  [0, 0.5, 1].forEach((f) => { const yy = T + ih - ih * f; s += `<line x1="${L}" x2="${W - R}" y1="${yy}" y2="${yy}" stroke="#e3e9ef"/><text x="${L - 6}" y="${yy + 4}" text-anchor="end">${Math.round(max * f)}</text><text x="${W - R + 6}" y="${yy + 4}">${100 * f}%</text>`; });
  t.forEach((m, i) => {
    const x0 = x(i) - bw / 2;
    s += `<rect x="${x0}" y="${y(m.ticket)}" width="${bw}" height="${ih - (y(m.ticket) - T)}" fill="#7a6bd6" rx="2"><title>${m.mese}: ${m.ticket} inoltrate</title></rect>`;
    s += `<rect x="${x0}" y="${y(m.ticket + m.risolte_ai)}" width="${bw}" height="${y(m.ticket) - y(m.ticket + m.risolte_ai)}" fill="#3aa57f" rx="2"><title>${m.mese}: ${m.risolte_ai} risolte dall'assistente</title></rect>`;
    s += `<text x="${x(i)}" y="${H - B + 16}" text-anchor="middle">${m.mese}${i === t.length - 1 ? "*" : ""}</text>`;
  });
  const pts = t.map((m, i) => m.media_quiz == null ? null : [x(i), yq(m.media_quiz), m.media_quiz]).filter(Boolean);
  if (pts.length) s += `<polyline points="${pts.map((p) => p[0] + "," + p[1]).join(" ")}" fill="none" stroke="#0066cc" stroke-width="2.5"/>` + pts.map((p) => `<circle cx="${p[0]}" cy="${p[1]}" r="4" fill="#0066cc" stroke="#fff" stroke-width="1.5"><title>Media quiz ${p[2]}%</title></circle>`).join("");
  s += `</svg><div class="legend"><span><i style="background:#3aa57f"></i>Risolte dall'assistente</span><span><i style="background:#7a6bd6"></i>Inoltrate al tecnico</span><span><i style="background:#0066cc;height:3px"></i>Media quiz (asse destro)</span><span>* mese in corso</span></div>`;
  return s;
}

/* ------------------------------------------------------------------ impostazioni demo */
$("#btn-settings").addEventListener("click", () => {
  const s = S.stato;
  modal(`<h2>Impostazioni della demo</h2>
  <p class="muted small">Pannello per chi presenta: non fa parte del prodotto.</p>
  <h3>Motore dell'assistente</h3>
  <div class="stack" style="margin-bottom:16px">
    <label class="opt"><input type="radio" name="eng" value="openai" ${s.motore === "openai" ? "checked" : ""} ${s.openai_disponibile ? "" : "disabled"}><span><b>OpenAI (${esc(s.modello)})</b><br><span class="small muted">${s.openai_disponibile ? "Risposte generate sui brani delle guide recuperati dalla ricerca." : "Non disponibile: avvia il server con la variabile OPENAI_API_KEY."}</span></span></label>
    <label class="opt"><input type="radio" name="eng" value="offline" ${s.motore === "offline" ? "checked" : ""}><span><b>Offline (riserva)</b><br><span class="small muted">Risposte preparate per i casi dimostrativi + ricerca della guida più pertinente. Utile se manca la rete.</span></span></label>
    <label class="opt"><input type="radio" name="eng" value="down" ${s.motore === "down" ? "checked" : ""}><span><b>Simula un guasto dell'AI</b><br><span class="small muted">Le richieste vanno nella coda di emergenza. Ripristinando, l'AI elabora quelle rimaste aperte.</span></span></label>
  </div>
  <h3>Dati</h3><p class="small muted">Ripristina operatori, richieste, quiz e ticket di esempio (utile prima di ogni prova del pitch).</p>
  <button class="btn danger sm" id="reset">Ripristina dati demo</button>`);
  $$("input[name=eng]").forEach((r) => r.addEventListener("change", async () => {
    try { await api("/api/motore", { motore: r.value }); await poll(); toast("Motore aggiornato"); route(); } catch (e) { toast(e.message); }
  }));
  $("#reset").addEventListener("click", async () => { await api("/api/reset", {}); S.chat = {}; closeModal(); await poll(); toast("Dati demo ripristinati"); route(); });
});

/* ------------------------------------------------------------------ avvio */
(async function init() {
  [S.ops, S.stato, S.argomenti] = await Promise.all([api("/api/operatori"), api("/api/stato"), api("/api/argomenti")]);
  if (!S.ops.find((o) => o.id === S.who)) S.who = "op1";
  renderWho(); renderStatus();
  if (!location.hash) location.hash = HOME[role()];
  route();
  setInterval(poll, 4000);
})();
