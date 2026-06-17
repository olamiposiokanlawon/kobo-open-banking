import React from "react";
import { S } from "../styles/theme";

export function Pill({ icon: Icon, accentColor, label, value }) {
  return (
    <div style={S.statPill}>
      <span style={{ ...S.pillIconWrapper, background: accentColor + "22" }}>
        <Icon size={15} color={accentColor} />
      </span>
      <div>
        <div style={S.pillLabel}>{label}</div>
        <div style={S.pillValue} className="tabular-nums">{value}</div>
      </div>
    </div>
  );
}
