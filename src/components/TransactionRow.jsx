import React from "react";
import { motion } from "framer-motion";
import { ArrowUpRight, ArrowDownLeft } from "lucide-react";
import { S, COLORS } from "../styles/theme";
import { findBankById, formatNaira } from "../utils/helpers";

export function TransactionRow({ transaction }) {
  const bank = findBankById(transaction.bankId);
  const isOutgoing = transaction.isOutgoing;

  return (
    <motion.div
      whileHover={{ background: "#FAFAF7" }}
      transition={{ duration: 0.12 }}
      style={S.transactionRow}
    >
      <span style={{
        ...S.transactionIconBox,
        background: isOutgoing ? COLORS.redPale : COLORS.greenPale,
      }}>
        {isOutgoing
          ? <ArrowUpRight size={16} color={COLORS.red} />
          : <ArrowDownLeft size={16} color={COLORS.green} />
        }
      </span>

      <div style={{ flex: 1, minWidth: 0 }}>
        <div style={S.transactionName}>{transaction.description}</div>
        <div style={S.transactionMeta}>
          <span style={{ ...S.colorDot, background: bank.brandColor }} />
          {bank.name} · {transaction.timestamp}
        </div>
      </div>

      <div
        className="tabular-nums"
        style={{
          ...S.transactionAmount,
          color: isOutgoing ? COLORS.ink : "#15803D",
        }}
      >
        {isOutgoing ? "−" : "+"}{formatNaira(transaction.amount)}
      </div>
    </motion.div>
  );
}
