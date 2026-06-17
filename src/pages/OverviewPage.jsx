import React from "react";
import { motion } from "framer-motion";
import { ArrowDownLeft, ArrowUpRight, Send } from "lucide-react";
import { S, COLORS, SHADOW } from "../styles/theme";
import { TRANSACTIONS } from "../data/mockData";
import { formatNaira } from "../utils/helpers";
import { SectionHeader } from "../components/SectionHeader";
import { Pill } from "../components/Pill";
import { TransactionRow } from "../components/TransactionRow";

const cardVariants = {
  hidden:  { opacity: 0, y: 16 },
  visible: { opacity: 1, y: 0  },
};

export function OverviewPage({ connectedBanks, animatedTotalBalance, totalBalance, totalMoneyIn, totalMoneyOut, onNavigate }) {
  const recentTransactions = TRANSACTIONS.slice(0, 5);

  return (
    <div style={{ display: "grid", gap: 32 }}>

      <motion.section
        style={S.heroCard}
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0  }}
        transition={{ duration: 0.35 }}
      >
        <div style={S.heroGlowOrbGreen} />
        <div style={S.heroGlowOrbBlue} />

        <div style={{ position: "relative", zIndex: 1 }}>
          <div style={S.heroLabel}>
            Total balance · {connectedBanks.length} bank{connectedBanks.length !== 1 ? "s" : ""}
          </div>
          <div style={S.heroBalanceNumber} className="tabular-nums">
            {formatNaira(animatedTotalBalance)}
          </div>
          <div style={S.heroActionsRow}>
            <Pill
              icon={ArrowDownLeft}
              accentColor={COLORS.green}
              label="Money in this month"
              value={formatNaira(totalMoneyIn, false)}
            />
            <Pill
              icon={ArrowUpRight}
              accentColor="#FB7185"
              label="Money out this month"
              value={formatNaira(totalMoneyOut, false)}
            />
            <motion.button
              whileHover={{ filter: "brightness(1.08)" }}
              whileTap={{ scale: 0.96 }}
              style={S.moveMoneyCta}
              onClick={() => onNavigate("transactions")}
            >
              <Send size={15} /> Move money
            </motion.button>
          </div>
        </div>

        <div style={S.bankCardFan}>
          {connectedBanks.slice(0, 5).map((bank, index) => (
            <motion.div
              key={bank.id}
              whileHover={{ y: -12, zIndex: 10 }}
              transition={{ duration: 0.22 }}
              style={{
                ...S.miniCard,
                background: bank.brandColor,
                marginLeft: index === 0 ? 0 : -38,
                zIndex: index,
                position: "relative",
              }}
            >
              <div style={S.miniCardBankName}>{bank.shortName}</div>
              <div style={S.miniCardAccountNumber}>{bank.maskedAccount}</div>
              <div style={S.miniCardBalance} className="tabular-nums">
                {formatNaira(bank.balance, false)}
              </div>
            </motion.div>
          ))}
        </div>
      </motion.section>

      <section>
        <SectionHeader title="Accounts" actionLabel="Manage" onAction={() => onNavigate("banks")} />
        <div style={S.bankGrid}>
          {connectedBanks.map((bank, index) => {
            const portfolioPercentage = (bank.balance / totalBalance) * 100;

            return (
              <motion.div
                key={bank.id}
                variants={cardVariants}
                initial="hidden"
                animate="visible"
                transition={{ delay: index * 0.07, duration: 0.3 }}
                whileHover={{ y: -4, boxShadow: SHADOW.cardHover }}
                style={S.bankCard}
              >
                <div style={S.bankCardHeader}>
                  <span style={{ ...S.bankInitialBadge, background: bank.brandColor }}>
                    {bank.shortName[0]}
                  </span>
                  <div>
                    <div style={S.bankName}>{bank.name}</div>
                    <div style={S.bankAccountMeta}>{bank.accountType} · {bank.maskedAccount}</div>
                  </div>
                </div>

                <div style={S.bankBalanceAmount} className="tabular-nums">
                  {formatNaira(bank.balance)}
                </div>

                <div style={S.shareBarTrack}>
                  <div
                    className="bar-grow"
                    style={{ ...S.shareBarFill, width: `${portfolioPercentage}%`, background: bank.brandColor }}
                  />
                </div>

                <div style={S.sharePercentageLabel}>
                  {portfolioPercentage.toFixed(1)}% of total portfolio
                </div>
              </motion.div>
            );
          })}
        </div>
      </section>

      <section>
        <SectionHeader title="Recent activity" actionLabel="See all" onAction={() => onNavigate("transactions")} />
        <div style={S.transactionListCard}>
          {recentTransactions.map((transaction, index) => (
            <motion.div
              key={transaction.id}
              initial={{ opacity: 0, x: -10 }}
              animate={{ opacity: 1, x: 0  }}
              transition={{ delay: index * 0.06 }}
            >
              <TransactionRow transaction={transaction} />
            </motion.div>
          ))}
        </div>
      </section>

    </div>
  );
}
