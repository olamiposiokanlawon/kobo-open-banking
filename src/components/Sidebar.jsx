import React from "react";
import { motion } from "framer-motion";
import { Wallet, LayoutDashboard, Receipt, PieChart, Building2, ShieldCheck } from "lucide-react";
import { S } from "../styles/theme";
import { NAV_ITEMS } from "../data/mockData";

const NAV_ICONS = {
  overview:     LayoutDashboard,
  transactions: Receipt,
  insights:     PieChart,
  banks:        Building2,
};

export function Sidebar({ activeTab, onNavigate }) {
  return (
    <aside style={S.sidebar}>
      <div style={S.brandArea}>
        <motion.div whileHover={{ scale: 1.06 }} style={S.brandLogo}>
          <Wallet size={19} strokeWidth={2.5} />
        </motion.div>
        <div>
          <div style={S.brandName}>Kɔbo</div>
          <div style={S.brandTagline}>open banking</div>
        </div>
      </div>

      <nav style={S.navList}>
        {NAV_ITEMS.map((item) => {
          const Icon = NAV_ICONS[item.id];
          const isActive = activeTab === item.id;

          return (
            <motion.button
              key={item.id}
              onClick={() => onNavigate(item.id)}
              whileHover={{ x: 3 }}
              whileTap={{ scale: 0.97 }}
              transition={{ duration: 0.15 }}
              style={{ ...S.navButton, ...(isActive ? S.navButtonActive : {}) }}
            >
              <Icon size={18} strokeWidth={isActive ? 2.4 : 2} />
              <span style={{ flex: 1 }}>{item.label}</span>
              {isActive && (
                <motion.span
                  layoutId="navActiveIndicator"
                  style={S.navActiveIndicator}
                  transition={{ type: "spring", stiffness: 420, damping: 32 }}
                />
              )}
            </motion.button>
          );
        })}
      </nav>

      
    </aside>
  );
}
