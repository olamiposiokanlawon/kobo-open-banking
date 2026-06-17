import React, { useState, useEffect, useMemo } from "react";
import {
  Wallet, ArrowDownLeft, ArrowUpRight, Plus, Search, Bell, Settings,
  LayoutDashboard, Receipt, PieChart, Building2, ShieldCheck, ChevronRight,
  TrendingUp, TrendingDown, Check, X, Link2, CreditCard, Send
} from "lucide-react";


const BANKS = [
  { id: "access", name: "Access Bank",  short: "Access",   tint: "#E85C2B", balance: 842500.75, acct: "•••• 4471", type: "Savings" },
  { id: "gtco",   name: "GTBank",       short: "GTBank",   tint: "#E94E1B", balance: 1290340.00, acct: "•••• 8820", type: "Current" },
  { id: "first",  name: "First Bank",   short: "FirstBank",tint: "#11366B", balance: 318900.20, acct: "•••• 0193", type: "Savings" },
  { id: "uba",    name: "UBA",          short: "UBA",      tint: "#D8232A", balance: 67450.00,  acct: "•••• 7765", type: "Current" },
  { id: "stanbic",name: "Stanbic IBTC", short: "Stanbic",  tint: "#0033A0", balance: 2104780.50,acct: "•••• 3309", type: "Savings" },
];

const AVAILABLE = [
  { id: "fidelity", name: "Fidelity Bank", tint: "#0B7A3B" },
  { id: "wema",     name: "Wema Bank",     tint: "#69247C" },
  { id: "zenith",   name: "Zenith Bank",   tint: "#C8102E" },
];

const TXNS = [
  { id: 1, bank: "stanbic", name: "Salary — Andela",        cat: "Income",        amt: 1850000, ts: "Today, 09:12",        out: false },
  { id: 2, bank: "gtco",    name: "Jumia Order #88231",      cat: "Shopping",      amt: 47200,   ts: "Today, 08:40",        out: true  },
  { id: 3, bank: "access",  name: "MTN Airtime",             cat: "Bills",         amt: 5000,    ts: "Yesterday, 21:05",    out: true  },
  { id: 4, bank: "uba",     name: "Transfer to Chidinma",    cat: "Transfer",      amt: 25000,   ts: "Yesterday, 17:33",    out: true  },
  { id: 5, bank: "stanbic", name: "Refund — Bolt",           cat: "Transport",     amt: 3400,    ts: "Yesterday, 14:18",    out: false },
  { id: 6, bank: "first",   name: "Shoprite Lekki",          cat: "Groceries",     amt: 38950,   ts: "12 Jun, 19:44",       out: true  },
  { id: 7, bank: "gtco",    name: "Netflix",                 cat: "Subscriptions", amt: 4400,    ts: "12 Jun, 06:00",       out: true  },
  { id: 8, bank: "access",  name: "Freelance — Pixelhaus",   cat: "Income",        amt: 420000,  ts: "11 Jun, 11:27",       out: false },
  { id: 9, bank: "stanbic", name: "DSTV Premium",            cat: "Bills",         amt: 44500,   ts: "11 Jun, 08:15",       out: true  },
  { id: 10,bank: "uba",     name: "Filling Station — TotalEnergies", cat: "Transport", amt: 30000, ts: "10 Jun, 16:52", out: true },
];

const SPEND = [
  { cat: "Shopping",      amt: 86150,  tint: "#16A34A" },
  { cat: "Bills",         amt: 49500,  tint: "#0EA5E9" },
  { cat: "Groceries",     amt: 38950,  tint: "#F59E0B" },
  { cat: "Transport",     amt: 60000,  tint: "#A855F7" },
  { cat: "Subscriptions", amt: 8800,   tint: "#EC4899" },
];

const naira = (n, dec = true) =>
  "₦" + n.toLocaleString("en-NG", { minimumFractionDigits: dec ? 2 : 0, maximumFractionDigits: dec ? 2 : 0 });

const bankOf = (id) => BANKS.find((b) => b.id === id) || AVAILABLE.find((b) => b.id === id) || { name: id, tint: "#64748B" };

function useCountUp(target, ms = 900) {
  const [v, setV] = useState(0);
  useEffect(() => {
    let raf, start;
    const tick = (t) => {
      if (!start) start = t;
      const p = Math.min((t - start) / ms, 1);
      const eased = 1 - Math.pow(1 - p, 3);
      setV(target * eased);
      if (p < 1) raf = requestAnimationFrame(tick);
    };
    raf = requestAnimationFrame(tick);
    return () => cancelAnimationFrame(raf);
  }, [target, ms]);
  return v;
}

/* ----------------------------- app ----------------------------- */

export default function App() {
  const [tab, setTab] = useState("home");
  const [banks, setBanks] = useState(BANKS);
  const [connecting, setConnecting] = useState(null); // bank obj being connected
  const [query, setQuery] = useState("");

  const total = useMemo(() => banks.reduce((s, b) => s + b.balance, 0), [banks]);
  const totalAnim = useCountUp(total);

  const monthIn  = TXNS.filter(t => !t.out).reduce((s,t)=>s+t.amt,0);
  const monthOut = TXNS.filter(t =>  t.out).reduce((s,t)=>s+t.amt,0);

  const filtered = TXNS.filter(t =>
    t.name.toLowerCase().includes(query.toLowerCase()) ||
    bankOf(t.bank).name.toLowerCase().includes(query.toLowerCase())
  );

  const NAV = [
    { id: "home",     label: "Overview",     icon: LayoutDashboard },
    { id: "txns",     label: "Transactions", icon: Receipt },
    { id: "insights", label: "Insights",     icon: PieChart },
    { id: "banks",    label: "Banks",        icon: Building2 },
  ];

  return (
    <div style={S.root}>
      <style>{CSS}</style>

      {/* ---- sidebar ---- */}
      <aside style={S.side}>
        <div style={S.brand}>
          <div style={S.brandMark}><Wallet size={18} strokeWidth={2.4} /></div>
          <div>
            <div style={S.brandName}>Kɔbo</div>
            <div style={S.brandSub}>open banking</div>
          </div>
        </div>

        <nav style={S.nav}>
          {NAV.map((n) => {
            const Icon = n.icon;
            const on = tab === n.id;
            return (
              <button key={n.id} onClick={() => setTab(n.id)}
                className="navbtn" style={{ ...S.navItem, ...(on ? S.navItemOn : {}) }}>
                <Icon size={18} strokeWidth={on ? 2.4 : 2} />
                <span>{n.label}</span>
                {on && <span style={S.navDot} />}
              </button>
            );
          })}
        </nav>

        <div style={S.secureCard}>
          <ShieldCheck size={16} color="#16A34A" />
          <div>
            <div style={{ fontWeight: 600, fontSize: 12.5 }}>Bank-grade secure</div>
            <div style={{ fontSize: 11, color: "#7C8AA0", lineHeight: 1.4 }}>
              OAuth 2.0 · AES-256 · read-only access
            </div>
          </div>
        </div>
      </aside>

      {/* ---- main ---- */}
      <main style={S.main}>
        {/* topbar */}
        <header style={S.top}>
          <div>
            <div style={S.kicker}>Good morning, Tunde</div>
            <h1 style={S.h1}>
              {tab === "home" && "Your money, all banks"}
              {tab === "txns" && "Transactions"}
              {tab === "insights" && "Spending insights"}
              {tab === "banks" && "Connected banks"}
            </h1>
          </div>
          <div style={S.topRight}>
            <div style={S.searchWrap}>
              <Search size={15} color="#9AA7BC" />
              <input
                placeholder="Search transactions"
                value={query}
                onChange={(e) => { setQuery(e.target.value); if (tab !== "txns") setTab("txns"); }}
                style={S.search}
              />
            </div>
            <button className="icobtn" style={S.ico}><Bell size={17} /><span style={S.badge} /></button>
            <button className="icobtn" style={S.ico}><Settings size={17} /></button>
            <div style={S.avatar}>TA</div>
          </div>
        </header>

        <div style={S.scroll}>
          {tab === "home" && (
            <Overview banks={banks} totalAnim={totalAnim} total={total}
              monthIn={monthIn} monthOut={monthOut} setTab={setTab} />
          )}
          {tab === "txns" && <Transactions txns={filtered} query={query} />}
          {tab === "insights" && <Insights monthIn={monthIn} monthOut={monthOut} />}
          {tab === "banks" && (
            <Banks banks={banks} onAdd={(b) => setConnecting(b)} />
          )}
        </div>
      </main>

      {connecting && (
        <ConnectModal
          bank={connecting}
          onClose={() => setConnecting(null)}
          onDone={(b) => {
            setBanks((prev) => [
              ...prev,
              { ...b, balance: Math.round(Math.random() * 900000) + 40000, acct: "•••• " + Math.floor(1000 + Math.random()*8999), type: "Savings", short: b.name.split(" ")[0] },
            ]);
            setConnecting(null);
          }}
        />
      )}
    </div>
  );
}

/* --------------------------- Overview --------------------------- */

function Overview({ banks, totalAnim, total, monthIn, monthOut, setTab }) {
  return (
    <div style={{ display: "grid", gap: 22 }}>
      {/* hero balance */}
      <section style={S.hero}>
        <div style={S.heroGlow} />
        <div style={{ position: "relative", zIndex: 1 }}>
          <div style={S.heroLabel}>Total balance · {banks.length} banks</div>
          <div style={S.heroNum} className="tnum">{naira(totalAnim)}</div>
          <div style={S.heroRow}>
            <Pill icon={ArrowDownLeft} tint="#16A34A" label="In this month" value={naira(monthIn, false)} />
            <Pill icon={ArrowUpRight} tint="#FB7185" label="Out this month" value={naira(monthOut, false)} />
            <button className="cta" style={S.heroSend} onClick={() => setTab("txns")}>
              <Send size={15} /> Move money
            </button>
          </div>
        </div>

        {/* fanned bank rail = signature element */}
        <div style={S.rail}>
          {banks.slice(0, 5).map((b, i) => (
            <div key={b.id} className="railcard"
              style={{ ...S.railCard, background: b.tint, marginLeft: i === 0 ? 0 : -34, zIndex: i }}>
              <div style={S.railName}>{b.short}</div>
              <div style={S.railAcct}>{b.acct}</div>
              <div style={S.railBal} className="tnum">{naira(b.balance, false)}</div>
            </div>
          ))}
        </div>
      </section>

      {/* bank grid */}
      <section>
        <SectionHead title="Accounts" action="Manage" onAction={() => setTab("banks")} />
        <div style={S.bankGrid}>
          {banks.map((b) => {
            const pct = (b.balance / total) * 100;
            return (
              <div key={b.id} className="card" style={S.bankCard}>
                <div style={S.bankTop}>
                  <span style={{ ...S.bankChip, background: b.tint }}>{b.short[0]}</span>
                  <div style={{ flex: 1 }}>
                    <div style={S.bankNm}>{b.name}</div>
                    <div style={S.bankMeta}>{b.type} · {b.acct}</div>
                  </div>
                </div>
                <div style={S.bankBal} className="tnum">{naira(b.balance)}</div>
                <div style={S.barTrack}>
                  <div style={{ ...S.barFill, width: `${pct}%`, background: b.tint }} />
                </div>
                <div style={S.bankShare}>{pct.toFixed(1)}% of total</div>
              </div>
            );
          })}
        </div>
      </section>

      {/* recent */}
      <section>
        <SectionHead title="Recent activity" action="See all" onAction={() => setTab("txns")} />
        <div className="card" style={S.list}>
          {TXNS.slice(0, 5).map((t) => <TxnRow key={t.id} t={t} />)}
        </div>
      </section>
    </div>
  );
}

/* --------------------------- Transactions --------------------------- */

function Transactions({ txns, query }) {
  return (
    <div className="card" style={{ ...S.list, padding: 0 }}>
      <div style={S.txnHeadRow}>
        <span style={{ flex: 1 }}>Description</span>
        <span style={{ width: 130 }}>Category</span>
        <span style={{ width: 150, textAlign: "right" }}>Amount</span>
      </div>
      {txns.length === 0 ? (
        <div style={S.empty}>
          <Search size={22} color="#B6C0D0" />
          <div style={{ fontWeight: 600, marginTop: 8 }}>No matches for “{query}”</div>
          <div style={{ color: "#8A97AC", fontSize: 13 }}>Try a bank name or merchant.</div>
        </div>
      ) : txns.map((t) => <TxnRow key={t.id} t={t} wide />)}
    </div>
  );
}

function TxnRow({ t, wide }) {
  const b = bankOf(t.bank);
  return (
    <div className="txnrow" style={S.txnRow}>
      <span style={{ ...S.txnIco, background: t.out ? "#FFF1F2" : "#ECFDF3" }}>
        {t.out ? <ArrowUpRight size={16} color="#F43F5E" /> : <ArrowDownLeft size={16} color="#16A34A" />}
      </span>
      <div style={{ flex: 1, minWidth: 0 }}>
        <div style={S.txnName}>{t.name}</div>
        <div style={S.txnMeta}>
          <span style={{ ...S.dot, background: b.tint }} />{b.name} · {t.ts}
        </div>
      </div>
      {wide && <span style={S.catTag}>{t.cat}</span>}
      <div style={{ ...S.txnAmt, color: t.out ? "#0B1B2B" : "#15803D", width: wide ? 150 : "auto" }} className="tnum">
        {t.out ? "−" : "+"}{naira(t.amt)}
      </div>
    </div>
  );
}

/* --------------------------- Insights --------------------------- */

function Insights({ monthIn, monthOut }) {
  const totalSpend = SPEND.reduce((s, x) => s + x.amt, 0);
  // donut geometry
  let acc = 0;
  const R = 70, C = 2 * Math.PI * R;
  const segs = SPEND.map((s) => {
    const frac = s.amt / totalSpend;
    const seg = { ...s, frac, dash: frac * C, offset: -acc * C };
    acc += frac;
    return seg;
  });
  const net = monthIn - monthOut;

  return (
    <div style={{ display: "grid", gap: 22 }}>
      <div style={S.statRow}>
        <StatCard label="Money in" value={naira(monthIn, false)} tint="#16A34A" icon={TrendingUp} delta="+18%" />
        <StatCard label="Money out" value={naira(monthOut, false)} tint="#F43F5E" icon={TrendingDown} delta="+6%" />
        <StatCard label="Net flow" value={(net>=0?"+":"−")+naira(Math.abs(net),false)} tint={net>=0?"#0EA5E9":"#F43F5E"} icon={Wallet} delta="Healthy" />
      </div>

      <div style={S.insGrid}>
        <div className="card" style={S.donutCard}>
          <div style={S.cardTitle}>Where it went</div>
          <div style={{ display: "flex", gap: 28, alignItems: "center", flexWrap: "wrap" }}>
            <svg width="180" height="180" viewBox="0 0 180 180">
              <g transform="rotate(-90 90 90)">
                {segs.map((s, i) => (
                  <circle key={i} cx="90" cy="90" r={R} fill="none" stroke={s.tint}
                    strokeWidth="20" strokeDasharray={`${s.dash} ${C - s.dash}`}
                    strokeDashoffset={s.offset} className="seg" style={{ animationDelay: `${i * 90}ms` }} />
                ))}
              </g>
              <text x="90" y="84" textAnchor="middle" style={S.donutBig} className="tnum">{naira(totalSpend, false)}</text>
              <text x="90" y="104" textAnchor="middle" style={S.donutSmall}>spent · June</text>
            </svg>
            <div style={{ flex: 1, minWidth: 180, display: "grid", gap: 10 }}>
              {segs.map((s) => (
                <div key={s.cat} style={S.legendRow}>
                  <span style={{ ...S.dot, background: s.tint, width: 9, height: 9 }} />
                  <span style={{ flex: 1, fontSize: 13.5 }}>{s.cat}</span>
                  <span style={{ fontSize: 13, color: "#64748B" }}>{(s.frac * 100).toFixed(0)}%</span>
                  <span className="tnum" style={{ fontWeight: 600, fontSize: 13.5, width: 78, textAlign: "right" }}>{naira(s.amt, false)}</span>
                </div>
              ))}
            </div>
          </div>
        </div>

        <div className="card" style={S.barsCard}>
          <div style={S.cardTitle}>Top categories</div>
          <div style={{ display: "grid", gap: 16, marginTop: 6 }}>
            {[...SPEND].sort((a, b) => b.amt - a.amt).map((s) => (
              <div key={s.cat}>
                <div style={S.barLabelRow}>
                  <span style={{ fontSize: 13.5 }}>{s.cat}</span>
                  <span className="tnum" style={{ fontSize: 13, fontWeight: 600 }}>{naira(s.amt, false)}</span>
                </div>
                <div style={S.barTrack}>
                  <div className="grow" style={{ ...S.barFill, width: `${(s.amt / SPEND[3].amt) * 100}%`, background: s.tint }} />
                </div>
              </div>
            ))}
          </div>
          <div style={S.insTip}>
            <PieChart size={15} color="#16A34A" />
            <span>Transport is up <b>22%</b> vs last month. Bolt + fuel are the main drivers.</span>
          </div>
        </div>
      </div>
    </div>
  );
}

/* --------------------------- Banks --------------------------- */

function Banks({ banks, onAdd }) {
  const connectedIds = banks.map((b) => b.id);
  const toAdd = AVAILABLE.filter((b) => !connectedIds.includes(b.id));
  return (
    <div style={{ display: "grid", gap: 22 }}>
      <section>
        <SectionHead title="Connected" sub={`${banks.length} accounts linked via Mono & Okra`} />
        <div style={S.bankGrid}>
          {banks.map((b) => (
            <div key={b.id} className="card" style={S.bankCard}>
              <div style={S.bankTop}>
                <span style={{ ...S.bankChip, background: b.tint }}>{b.short?.[0] ?? b.name[0]}</span>
                <div style={{ flex: 1 }}>
                  <div style={S.bankNm}>{b.name}</div>
                  <div style={S.bankMeta}>{b.type} · {b.acct}</div>
                </div>
                <span style={S.liveTag}><span className="livedot" />Live</span>
              </div>
              <div style={S.bankBal} className="tnum">{naira(b.balance)}</div>
              <div style={S.consentRow}>
                <ShieldCheck size={13} color="#16A34A" /> Read-only · renews in 89 days
              </div>
            </div>
          ))}
        </div>
      </section>

      <section>
        <SectionHead title="Add a bank" sub="One tap — you authenticate on your bank's own page" />
        <div style={S.bankGrid}>
          {toAdd.map((b) => (
            <button key={b.id} className="card addcard" style={S.addCard} onClick={() => onAdd(b)}>
              <span style={{ ...S.bankChip, background: b.tint }}>{b.name[0]}</span>
              <div style={{ flex: 1, textAlign: "left" }}>
                <div style={S.bankNm}>{b.name}</div>
                <div style={S.bankMeta}>Tap to connect</div>
              </div>
              <span style={S.addPlus}><Plus size={16} /></span>
            </button>
          ))}
        </div>
      </section>
    </div>
  );
}

/* --------------------------- Connect modal --------------------------- */

function ConnectModal({ bank, onClose, onDone }) {
  const STEPS = ["Redirecting to bank", "Authenticate securely", "Granting read access", "Linked"];
  const [step, setStep] = useState(0);
  useEffect(() => {
    if (step >= STEPS.length - 1) { const t = setTimeout(() => onDone(bank), 700); return () => clearTimeout(t); }
    const t = setTimeout(() => setStep((s) => s + 1), 850);
    return () => clearTimeout(t);
  }, [step]);

  return (
    <div style={S.overlay} onClick={onClose}>
      <div className="modal" style={S.modal} onClick={(e) => e.stopPropagation()}>
        <button className="icobtn" style={S.modalX} onClick={onClose}><X size={16} /></button>
        <div style={{ ...S.modalChip, background: bank.tint }}>{bank.name[0]}</div>
        <div style={S.modalTitle}>Connecting {bank.name}</div>
        <div style={S.modalSub}>Secured by Mono · OAuth 2.0</div>

        <div style={{ display: "grid", gap: 2, marginTop: 22 }}>
          {STEPS.map((label, i) => {
            const done = i < step, active = i === step;
            return (
              <div key={i} style={S.stepRow}>
                <span style={{
                  ...S.stepDot,
                  background: done ? "#16A34A" : active ? "#0B1B2B" : "#E6EAF0",
                  color: done || active ? "#fff" : "#9AA7BC",
                }}>
                  {done ? <Check size={13} /> : active ? <span className="spin" /> : i + 1}
                </span>
                <span style={{ fontSize: 14, color: done || active ? "#0B1B2B" : "#9AA7BC", fontWeight: active ? 600 : 500 }}>
                  {label}
                </span>
              </div>
            );
          })}
        </div>

        <div style={S.modalFoot}>
          <Link2 size={13} color="#8A97AC" /> Kɔbo never sees your password. Access is read-only.
        </div>
      </div>
    </div>
  );
}

/* --------------------------- small pieces --------------------------- */

function Pill({ icon: Icon, tint, label, value }) {
  return (
    <div style={S.pill}>
      <span style={{ ...S.pillIco, background: tint + "22" }}><Icon size={15} color={tint} /></span>
      <div>
        <div style={S.pillLabel}>{label}</div>
        <div style={S.pillVal} className="tnum">{value}</div>
      </div>
    </div>
  );
}

function StatCard({ label, value, tint, icon: Icon, delta }) {
  return (
    <div className="card" style={S.statCard}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <span style={{ ...S.statIco, background: tint + "18" }}><Icon size={17} color={tint} /></span>
        <span style={{ ...S.deltaTag, color: tint, background: tint + "12" }}>{delta}</span>
      </div>
      <div style={S.statVal} className="tnum">{value}</div>
      <div style={S.statLabel}>{label}</div>
    </div>
  );
}

function SectionHead({ title, sub, action, onAction }) {
  return (
    <div style={S.secHead}>
      <div>
        <h2 style={S.secTitle}>{title}</h2>
        {sub && <div style={S.secSub}>{sub}</div>}
      </div>
      {action && (
        <button className="link" style={S.secAction} onClick={onAction}>
          {action} <ChevronRight size={15} />
        </button>
      )}
    </div>
  );
}

/* ------------------------------ styles ------------------------------ */

const ink = "#0B1B2B";
const S = {
  root: { display: "flex", height: "100vh", width: "100%", background: "#F4F2ED", color: ink,
    fontFamily: "'Inter', system-ui, sans-serif", overflow: "hidden" },

  /* sidebar */
  side: { width: 232, flexShrink: 0, background: ink, color: "#E8EDF4", padding: "26px 18px",
    display: "flex", flexDirection: "column", gap: 26 },
  brand: { display: "flex", gap: 12, alignItems: "center", paddingLeft: 6 },
  brandMark: { width: 38, height: 38, borderRadius: 11, background: "#16A34A",
    display: "grid", placeItems: "center", color: "#fff" },
  brandName: { fontFamily: "'Bricolage Grotesque', sans-serif", fontWeight: 700, fontSize: 20, letterSpacing: "-0.02em" },
  brandSub: { fontSize: 10.5, color: "#7C8AA0", letterSpacing: "0.16em", textTransform: "uppercase", marginTop: -1 },
  nav: { display: "grid", gap: 4 },
  navItem: { display: "flex", alignItems: "center", gap: 12, padding: "11px 13px", borderRadius: 11,
    background: "transparent", border: "none", color: "#9AA7BC", fontSize: 14, fontWeight: 500,
    cursor: "pointer", width: "100%", position: "relative", transition: "all .15s" },
  navItemOn: { background: "rgba(255,255,255,0.07)", color: "#fff" },
  navDot: { position: "absolute", right: 13, width: 6, height: 6, borderRadius: 6, background: "#16A34A" },
  secureCard: { marginTop: "auto", display: "flex", gap: 10, alignItems: "flex-start",
    padding: "13px 14px", borderRadius: 13, background: "rgba(22,163,74,0.10)",
    border: "1px solid rgba(22,163,74,0.22)" },

  /* main */
  main: { flex: 1, display: "flex", flexDirection: "column", minWidth: 0 },
  top: { display: "flex", justifyContent: "space-between", alignItems: "center", padding: "22px 32px 18px",
    borderBottom: "1px solid #E7E3DA" },
  kicker: { fontSize: 12.5, color: "#16A34A", fontWeight: 600, letterSpacing: "0.01em" },
  h1: { fontFamily: "'Bricolage Grotesque', sans-serif", fontSize: 26, fontWeight: 700,
    letterSpacing: "-0.025em", margin: "2px 0 0" },
  topRight: { display: "flex", alignItems: "center", gap: 10 },
  searchWrap: { display: "flex", alignItems: "center", gap: 8, background: "#fff", border: "1px solid #E5E1D7",
    borderRadius: 11, padding: "9px 13px", width: 230 },
  search: { border: "none", outline: "none", background: "transparent", fontSize: 13.5, width: "100%", color: ink },
  ico: { position: "relative", width: 40, height: 40, borderRadius: 11, background: "#fff", border: "1px solid #E5E1D7",
    display: "grid", placeItems: "center", color: "#475569", cursor: "pointer" },
  badge: { position: "absolute", top: 9, right: 10, width: 7, height: 7, borderRadius: 7, background: "#F43F5E", border: "1.5px solid #fff" },
  avatar: { width: 40, height: 40, borderRadius: 11, background: ink, color: "#fff",
    display: "grid", placeItems: "center", fontWeight: 700, fontSize: 13 },

  scroll: { padding: "26px 32px 40px", overflowY: "auto", flex: 1 },

  /* hero */
  hero: { position: "relative", background: ink, color: "#fff", borderRadius: 22, padding: "30px 32px",
    overflow: "hidden", display: "flex", justifyContent: "space-between", alignItems: "center", gap: 24 },
  heroGlow: { position: "absolute", top: -120, right: -60, width: 360, height: 360, borderRadius: "50%",
    background: "radial-gradient(circle, rgba(22,163,74,0.45), transparent 65%)" },
  heroLabel: { fontSize: 13, color: "#9DB0C8", fontWeight: 500 },
  heroNum: { fontFamily: "'Bricolage Grotesque', sans-serif", fontSize: 46, fontWeight: 700,
    letterSpacing: "-0.03em", margin: "6px 0 18px", lineHeight: 1 },
  heroRow: { display: "flex", gap: 12, alignItems: "center", flexWrap: "wrap" },
  pill: { display: "flex", gap: 10, alignItems: "center", background: "rgba(255,255,255,0.07)",
    padding: "9px 14px 9px 9px", borderRadius: 13, border: "1px solid rgba(255,255,255,0.09)" },
  pillIco: { width: 30, height: 30, borderRadius: 9, display: "grid", placeItems: "center" },
  pillLabel: { fontSize: 11, color: "#9DB0C8" },
  pillVal: { fontSize: 15, fontWeight: 600 },
  heroSend: { display: "flex", gap: 8, alignItems: "center", background: "#16A34A", color: "#fff",
    border: "none", borderRadius: 13, padding: "11px 18px", fontSize: 13.5, fontWeight: 600, cursor: "pointer" },

  rail: { position: "relative", display: "flex", flexShrink: 0 },
  railCard: { width: 134, height: 150, borderRadius: 16, padding: "16px 16px", color: "#fff",
    boxShadow: "0 16px 30px -14px rgba(0,0,0,0.55)", display: "flex", flexDirection: "column",
    transition: "transform .25s ease", border: "1px solid rgba(255,255,255,0.16)" },
  railName: { fontWeight: 700, fontSize: 14, letterSpacing: "-0.01em" },
  railAcct: { fontSize: 11, opacity: 0.82, marginTop: 3, letterSpacing: "0.04em" },
  railBal: { marginTop: "auto", fontSize: 17, fontWeight: 700 },

  /* sections */
  secHead: { display: "flex", justifyContent: "space-between", alignItems: "flex-end", marginBottom: 14 },
  secTitle: { fontFamily: "'Bricolage Grotesque', sans-serif", fontSize: 18, fontWeight: 700, letterSpacing: "-0.02em", margin: 0 },
  secSub: { fontSize: 12.5, color: "#8A97AC", marginTop: 2 },
  secAction: { display: "flex", alignItems: "center", gap: 2, background: "none", border: "none",
    color: "#16A34A", fontSize: 13, fontWeight: 600, cursor: "pointer" },

  /* bank cards */
  bankGrid: { display: "grid", gridTemplateColumns: "repeat(auto-fill, minmax(238px, 1fr))", gap: 14 },
  bankCard: { background: "#fff", borderRadius: 16, padding: "16px 17px", border: "1px solid #ECE8DE" },
  bankTop: { display: "flex", gap: 11, alignItems: "center", marginBottom: 13 },
  bankChip: { width: 36, height: 36, borderRadius: 10, color: "#fff", fontWeight: 700, fontSize: 15,
    display: "grid", placeItems: "center", flexShrink: 0 },
  bankNm: { fontWeight: 600, fontSize: 14, letterSpacing: "-0.01em" },
  bankMeta: { fontSize: 11.5, color: "#94A1B5", marginTop: 1 },
  bankBal: { fontSize: 22, fontWeight: 700, letterSpacing: "-0.02em", fontFamily: "'Bricolage Grotesque', sans-serif" },
  barTrack: { height: 6, borderRadius: 6, background: "#F0ECE2", marginTop: 12, overflow: "hidden" },
  barFill: { height: "100%", borderRadius: 6, transition: "width .9s cubic-bezier(.2,.7,.2,1)" },
  bankShare: { fontSize: 11.5, color: "#94A1B5", marginTop: 7 },
  liveTag: { display: "flex", alignItems: "center", gap: 5, fontSize: 11, fontWeight: 600, color: "#16A34A",
    background: "#ECFDF3", padding: "4px 9px", borderRadius: 20 },
  consentRow: { display: "flex", alignItems: "center", gap: 6, fontSize: 11.5, color: "#8A97AC", marginTop: 13 },

  addCard: { display: "flex", gap: 11, alignItems: "center", background: "#fff", borderRadius: 16,
    padding: "16px 17px", border: "1px dashed #D6CFC0", cursor: "pointer", width: "100%" },
  addPlus: { width: 30, height: 30, borderRadius: 9, background: "#F4F2ED", display: "grid", placeItems: "center", color: ink },

  /* lists */
  list: { background: "#fff", borderRadius: 16, border: "1px solid #ECE8DE", padding: "6px 4px" },
  txnHeadRow: { display: "flex", padding: "14px 18px 12px", fontSize: 11, fontWeight: 600, color: "#9AA7BC",
    textTransform: "uppercase", letterSpacing: "0.06em", borderBottom: "1px solid #F0ECE2" },
  txnRow: { display: "flex", alignItems: "center", gap: 13, padding: "13px 16px", borderRadius: 12 },
  txnIco: { width: 36, height: 36, borderRadius: 10, display: "grid", placeItems: "center", flexShrink: 0 },
  txnName: { fontWeight: 600, fontSize: 14, letterSpacing: "-0.01em", whiteSpace: "nowrap", overflow: "hidden", textOverflow: "ellipsis" },
  txnMeta: { display: "flex", alignItems: "center", gap: 6, fontSize: 12, color: "#94A1B5", marginTop: 2 },
  dot: { width: 7, height: 7, borderRadius: 7, display: "inline-block" },
  catTag: { width: 130, fontSize: 12, color: "#64748B", fontWeight: 500 },
  txnAmt: { fontSize: 14.5, fontWeight: 700, textAlign: "right", letterSpacing: "-0.01em" },
  empty: { padding: "48px 20px", textAlign: "center" },

  /* insights */
  statRow: { display: "grid", gridTemplateColumns: "repeat(3, 1fr)", gap: 14 },
  statCard: { background: "#fff", borderRadius: 16, padding: "18px 18px", border: "1px solid #ECE8DE" },
  statIco: { width: 38, height: 38, borderRadius: 11, display: "grid", placeItems: "center" },
  deltaTag: { fontSize: 11.5, fontWeight: 600, padding: "4px 9px", borderRadius: 20 },
  statVal: { fontSize: 25, fontWeight: 700, letterSpacing: "-0.02em", marginTop: 16,
    fontFamily: "'Bricolage Grotesque', sans-serif" },
  statLabel: { fontSize: 12.5, color: "#8A97AC", marginTop: 2 },
  insGrid: { display: "grid", gridTemplateColumns: "1.25fr 1fr", gap: 16 },
  donutCard: { background: "#fff", borderRadius: 18, padding: "20px 22px", border: "1px solid #ECE8DE" },
  barsCard: { background: "#fff", borderRadius: 18, padding: "20px 22px", border: "1px solid #ECE8DE" },
  cardTitle: { fontFamily: "'Bricolage Grotesque', sans-serif", fontWeight: 700, fontSize: 15.5, marginBottom: 16 },
  donutBig: { fontSize: 17, fontWeight: 700, fill: ink, fontFamily: "'Bricolage Grotesque', sans-serif" },
  donutSmall: { fontSize: 9.5, fill: "#94A1B5" },
  legendRow: { display: "flex", alignItems: "center", gap: 9 },
  barLabelRow: { display: "flex", justifyContent: "space-between", marginBottom: 6 },
  insTip: { display: "flex", gap: 9, alignItems: "flex-start", marginTop: 20, padding: "12px 13px",
    background: "#F0FAF3", borderRadius: 12, fontSize: 12.5, color: "#2F4A3A", lineHeight: 1.5 },
  cardTitleSm: {},

  /* modal */
  overlay: { position: "fixed", inset: 0, background: "rgba(11,27,43,0.55)", backdropFilter: "blur(3px)",
    display: "grid", placeItems: "center", zIndex: 50 },
  modal: { position: "relative", width: 380, background: "#fff", borderRadius: 22, padding: "30px 30px 22px",
    boxShadow: "0 30px 70px -20px rgba(0,0,0,0.4)" },
  modalX: { position: "absolute", top: 16, right: 16, width: 32, height: 32, borderRadius: 9,
    border: "none", background: "#F4F2ED", display: "grid", placeItems: "center", cursor: "pointer", color: "#64748B" },
  modalChip: { width: 50, height: 50, borderRadius: 14, color: "#fff", fontWeight: 700, fontSize: 22,
    display: "grid", placeItems: "center" },
  modalTitle: { fontFamily: "'Bricolage Grotesque', sans-serif", fontWeight: 700, fontSize: 20, marginTop: 16, letterSpacing: "-0.02em" },
  modalSub: { fontSize: 12.5, color: "#8A97AC", marginTop: 3 },
  stepRow: { display: "flex", alignItems: "center", gap: 12, padding: "9px 0" },
  stepDot: { width: 26, height: 26, borderRadius: 26, display: "grid", placeItems: "center", fontSize: 12, fontWeight: 700, flexShrink: 0 },
  modalFoot: { display: "flex", gap: 7, alignItems: "center", marginTop: 18, paddingTop: 16,
    borderTop: "1px solid #F0ECE2", fontSize: 11.5, color: "#8A97AC", lineHeight: 1.4 },
};

const CSS = `
@import url('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@600;700;800&family=Inter:wght@400;500;600;700&display=swap');
* { box-sizing: border-box; }
::-webkit-scrollbar { width: 9px; height: 9px; }
::-webkit-scrollbar-thumb { background: #d8d2c5; border-radius: 9px; border: 2px solid #F4F2ED; }
.tnum { font-variant-numeric: tabular-nums; }
.navbtn:hover { background: rgba(255,255,255,0.05); color: #fff; }
.icobtn:hover { background: #F4F2ED; }
.card { transition: box-shadow .18s, transform .18s, border-color .18s; }
.card:hover { box-shadow: 0 10px 26px -16px rgba(11,27,43,0.28); }
.addcard:hover { border-color: #16A34A; background: #FCFBF8; }
.txnrow:hover { background: #FAF8F3; }
.cta:hover { filter: brightness(1.07); }
.link:hover { opacity: .75; }
.railcard:hover { transform: translateY(-10px); }
.livedot { width: 6px; height: 6px; border-radius: 6px; background: #16A34A; display: inline-block; animation: pulse 1.6s infinite; }
@keyframes pulse { 0%,100% { opacity: 1; } 50% { opacity: .35; } }
.seg { animation: draw .8s ease forwards; opacity: 0; }
@keyframes draw { to { opacity: 1; } }
.grow { animation: grow .9s cubic-bezier(.2,.7,.2,1); }
@keyframes grow { from { width: 0 !important; } }
.spin { width: 12px; height: 12px; border: 2px solid rgba(255,255,255,.4); border-top-color:#fff; border-radius: 50%; animation: sp .7s linear infinite; }
@keyframes sp { to { transform: rotate(360deg); } }
.modal { animation: pop .22s cubic-bezier(.2,.8,.2,1); }
@keyframes pop { from { transform: scale(.94); opacity: 0; } }
input::placeholder { color: #9AA7BC; }
@media (max-width: 920px) {
  aside { display: none; }
  .insGrid, [style*="repeat(3, 1fr)"] { grid-template-columns: 1fr !important; }
}
@media (prefers-reduced-motion: reduce) { * { animation: none !important; transition: none !important; } }
`;
