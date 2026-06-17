import React from "react";
import { motion } from "framer-motion";
import { Bell, Settings } from "lucide-react";
import { S } from "../styles/theme";

export function TopBar() {
  return (
    <header style={S.topBar}>
      <div>
        <div style={S.pageGreeting}>Good morning, Tunde</div>
        <h1 style={S.pageTitle}>Your money, all banks</h1>
      </div>

      <div style={S.topBarRight}>
        <motion.button whileTap={{ scale: 0.93 }} style={S.iconButton}>
          <Bell size={17} />
          <span style={S.notificationBadge} />
        </motion.button>

        <motion.button whileTap={{ scale: 0.93 }} style={S.iconButton}>
          <Settings size={17} />
        </motion.button>

        <div style={S.avatarCircle}>TA</div>
      </div>
    </header>
  );
}
