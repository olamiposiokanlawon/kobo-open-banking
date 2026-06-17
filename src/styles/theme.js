export const COLORS = {
  ink:           "#0A1628",
  inkMid:        "#1E293B",
  canvas:        "#F8F6F1",
  canvasDark:    "#EFECE5",
  white:         "#FFFFFF",
  green:         "#16A34A",
  greenPale:     "#ECFDF5",
  red:           "#F43F5E",
  redPale:       "#FFF1F2",
  blue:          "#0EA5E9",
  border:        "#E8E4DC",
  borderLight:   "#F2EFE8",
  mutedLight:    "#94A3B8",
  muted:         "#64748B",
  sidebarText:   "#C4CDD8",
  sidebarMuted:  "#7A8BA0",
};

export const FONT = {
  display: "'Bricolage Grotesque', system-ui, sans-serif",
  body:    "'Inter', system-ui, sans-serif",
};

export const SHADOW = {
  card:      "0 1px 2px rgba(10,22,40,0.04), 0 4px 14px rgba(10,22,40,0.06)",
  cardHover: "0 8px 32px rgba(10,22,40,0.14), 0 2px 6px rgba(10,22,40,0.06)",
};

export const S = {

  appShell: {
    display: "flex", height: "100vh", width: "100%",
    background: COLORS.canvas, color: COLORS.ink,
    fontFamily: FONT.body, overflow: "hidden",
  },

  sidebar: {
    width: 244, flexShrink: 0,
    background: COLORS.ink, color: COLORS.sidebarText,
    padding: "28px 20px",
    display: "flex", flexDirection: "column", gap: 32,
  },
  brandArea: { display: "flex", gap: 13, alignItems: "center", paddingLeft: 4 },
  brandLogo: {
    width: 42, height: 42, borderRadius: 13, background: COLORS.green,
    display: "grid", placeItems: "center", color: "#fff", flexShrink: 0,
  },
  brandName: {
    fontFamily: FONT.display, fontWeight: 700, fontSize: 21,
    letterSpacing: "-0.025em", color: "#fff",
  },
  brandTagline: {
    fontSize: 10, color: COLORS.sidebarMuted,
    letterSpacing: "0.18em", textTransform: "uppercase", marginTop: 1,
  },
  navList:   { display: "grid", gap: 3 },
  navButton: {
    display: "flex", alignItems: "center", gap: 11,
    padding: "10px 13px", borderRadius: 11,
    background: "transparent", border: "none",
    color: COLORS.sidebarMuted, fontSize: 13.5, fontWeight: 500,
    cursor: "pointer", width: "100%", position: "relative", textAlign: "left",
  },
  navButtonActive: { background: "rgba(255,255,255,0.09)", color: "#fff" },
  navActiveIndicator: {
    position: "absolute", right: 13,
    width: 6, height: 6, borderRadius: 6, background: COLORS.green,
  },
  securityBadge: {
    marginTop: "auto",
    display: "flex", gap: 10, alignItems: "flex-start",
    padding: "14px 14px", borderRadius: 13,
    background: "rgba(22,163,74,0.08)",
    border: "1px solid rgba(22,163,74,0.2)",
  },

  mainColumn:    { flex: 1, display: "flex", flexDirection: "column", minWidth: 0 },
  topBar: {
    display: "flex", justifyContent: "space-between", alignItems: "center",
    padding: "20px 40px 18px",
    borderBottom: `1px solid ${COLORS.border}`,
    background: COLORS.canvas,
    flexShrink: 0,
  },
  pageGreeting: { fontSize: 12, color: COLORS.green, fontWeight: 600, letterSpacing: "0.01em" },
  pageTitle: {
    fontFamily: FONT.display, fontSize: 26, fontWeight: 700,
    letterSpacing: "-0.03em", margin: "3px 0 0", color: COLORS.ink,
  },
  topBarRight: { display: "flex", alignItems: "center", gap: 10 },
  iconButton: {
    position: "relative", width: 40, height: 40, borderRadius: 11,
    background: COLORS.white, border: `1px solid ${COLORS.border}`,
    display: "grid", placeItems: "center", color: COLORS.muted, cursor: "pointer", flexShrink: 0,
  },
  notificationBadge: {
    position: "absolute", top: 9, right: 9,
    width: 7, height: 7, borderRadius: 7,
    background: COLORS.red, border: `2px solid ${COLORS.canvas}`,
  },
  avatarCircle: {
    width: 40, height: 40, borderRadius: 11,
    background: COLORS.ink, color: "#fff",
    display: "grid", placeItems: "center",
    fontWeight: 700, fontSize: 13, flexShrink: 0,
  },
  pageScrollArea: { padding: "36px 40px 56px", overflowY: "auto", flex: 1 },

  heroCard: {
    position: "relative", background: COLORS.ink, color: "#fff",
    borderRadius: 24, padding: "40px 44px",
    overflow: "hidden",
    display: "flex", justifyContent: "space-between",
    alignItems: "center", gap: 32,
  },
  heroGlowOrbGreen: {
    position: "absolute", top: -110, right: -30,
    width: 400, height: 400, borderRadius: "50%",
    background: "radial-gradient(circle, rgba(22,163,74,0.5), transparent 60%)",
    pointerEvents: "none",
  },
  heroGlowOrbBlue: {
    position: "absolute", bottom: -80, left: 60,
    width: 220, height: 220, borderRadius: "50%",
    background: "radial-gradient(circle, rgba(14,165,233,0.22), transparent 65%)",
    pointerEvents: "none",
  },
  heroLabel: { fontSize: 12.5, color: "#9DB0C8", fontWeight: 500, letterSpacing: "0.01em" },
  heroBalanceNumber: {
    fontFamily: FONT.display, fontSize: 52, fontWeight: 700,
    letterSpacing: "-0.04em", margin: "8px 0 22px", lineHeight: 1,
  },
  heroActionsRow: { display: "flex", gap: 12, alignItems: "center", flexWrap: "wrap" },
  moveMoneyCta: {
    display: "flex", gap: 8, alignItems: "center",
    background: COLORS.green, color: "#fff", border: "none",
    borderRadius: 12, padding: "11px 20px",
    fontSize: 13.5, fontWeight: 600, cursor: "pointer",
  },

  bankCardFan:          { position: "relative", display: "flex", flexShrink: 0 },
  miniCard: {
    width: 138, height: 162, borderRadius: 18,
    padding: "18px 17px", color: "#fff",
    boxShadow: "0 20px 40px -14px rgba(0,0,0,0.65)",
    display: "flex", flexDirection: "column",
    border: "1px solid rgba(255,255,255,0.18)",
  },
  miniCardBankName:      { fontWeight: 700, fontSize: 14, letterSpacing: "-0.01em" },
  miniCardAccountNumber: { fontSize: 11, opacity: 0.78, marginTop: 3, letterSpacing: "0.04em" },
  miniCardBalance:       { marginTop: "auto", fontSize: 16, fontWeight: 700, letterSpacing: "-0.015em" },

  statPill: {
    display: "flex", gap: 10, alignItems: "center",
    background: "rgba(255,255,255,0.08)",
    padding: "10px 16px 10px 10px",
    borderRadius: 14, border: "1px solid rgba(255,255,255,0.1)",
  },
  pillIconWrapper: { width: 32, height: 32, borderRadius: 10, display: "grid", placeItems: "center" },
  pillLabel:       { fontSize: 11, color: "#9DB0C8" },
  pillValue:       { fontSize: 15, fontWeight: 600 },

  sectionHeaderRow: {
    display: "flex", justifyContent: "space-between",
    alignItems: "flex-end", marginBottom: 18,
  },
  sectionTitle: {
    fontFamily: FONT.display, fontSize: 19, fontWeight: 700,
    letterSpacing: "-0.025em", margin: 0,
  },
  sectionSubtitle:     { fontSize: 12.5, color: COLORS.mutedLight, marginTop: 3 },
  sectionActionButton: {
    display: "flex", alignItems: "center", gap: 2, background: "none",
    border: "none", color: COLORS.green, fontSize: 13, fontWeight: 600, cursor: "pointer",
  },

  bankGrid:       { display: "grid", gridTemplateColumns: "repeat(auto-fill, minmax(244px, 1fr))", gap: 16 },
  bankCard: {
    background: COLORS.white, borderRadius: 18,
    padding: "22px 22px", border: `1px solid ${COLORS.border}`,
    boxShadow: SHADOW.card,
  },
  bankCardHeader:   { display: "flex", gap: 12, alignItems: "center", marginBottom: 18 },
  bankInitialBadge: {
    width: 40, height: 40, borderRadius: 12, color: "#fff",
    fontWeight: 700, fontSize: 16, display: "grid", placeItems: "center", flexShrink: 0,
  },
  bankName:            { fontWeight: 600, fontSize: 14, letterSpacing: "-0.01em" },
  bankAccountMeta:     { fontSize: 12, color: COLORS.mutedLight, marginTop: 2 },
  bankBalanceAmount: {
    fontSize: 26, fontWeight: 700, letterSpacing: "-0.03em",
    fontFamily: FONT.display,
  },
  shareBarTrack:        { height: 5, borderRadius: 5, background: COLORS.borderLight, marginTop: 16, overflow: "hidden" },
  shareBarFill:         { height: "100%", borderRadius: 5, transition: "width 1s cubic-bezier(.2,.7,.2,1)" },
  sharePercentageLabel: { fontSize: 11.5, color: COLORS.mutedLight, marginTop: 8 },

  transactionListCard: {
    background: COLORS.white, borderRadius: 18,
    border: `1px solid ${COLORS.border}`, boxShadow: SHADOW.card, overflow: "hidden",
  },
  transactionRow:     { display: "flex", alignItems: "center", gap: 14, padding: "15px 22px" },
  transactionIconBox: { width: 40, height: 40, borderRadius: 12, display: "grid", placeItems: "center", flexShrink: 0 },
  transactionName: {
    fontWeight: 600, fontSize: 14, letterSpacing: "-0.01em",
    whiteSpace: "nowrap", overflow: "hidden", textOverflow: "ellipsis",
  },
  transactionMeta:   { display: "flex", alignItems: "center", gap: 6, fontSize: 12, color: COLORS.mutedLight, marginTop: 2 },
  colorDot:          { width: 7, height: 7, borderRadius: 7, display: "inline-block", flexShrink: 0 },
  transactionAmount: { fontSize: 14.5, fontWeight: 700, textAlign: "right", letterSpacing: "-0.01em" },
};
