import React from "react";
import { ChevronRight } from "lucide-react";
import { S } from "../styles/theme";

export function SectionHeader({ title, subtitle, actionLabel, onAction }) {
  return (
    <div style={S.sectionHeaderRow}>
      <div>
        <h2 style={S.sectionTitle}>{title}</h2>
        {subtitle && <div style={S.sectionSubtitle}>{subtitle}</div>}
      </div>

      {actionLabel && (
        <button style={S.sectionActionButton} onClick={onAction}>
          {actionLabel} <ChevronRight size={14} />
        </button>
      )}
    </div>
  );
}
