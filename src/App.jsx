import React, { useMemo } from "react";

import { S } from "./styles/theme";
import { CONNECTED_BANKS, TRANSACTIONS } from "./data/mockData";
import { useCountUp } from "./hooks/useCountUp";

import { Sidebar }      from "./components/Sidebar";
import { TopBar }       from "./components/TopBar";
import { OverviewPage } from "./pages/OverviewPage";

export default function App() {
  const totalBalance = useMemo(
    () => CONNECTED_BANKS.reduce((sum, bank) => sum + bank.balance, 0),
    []
  );

  const animatedTotalBalance = useCountUp(totalBalance);

  const totalMoneyIn  = TRANSACTIONS.filter((t) => !t.isOutgoing).reduce((sum, t) => sum + t.amount, 0);
  const totalMoneyOut = TRANSACTIONS.filter((t) =>  t.isOutgoing).reduce((sum, t) => sum + t.amount, 0);

  return (
    <div style={S.appShell}>
      <Sidebar activeTab="overview" onNavigate={() => {}} />
      <div style={S.mainColumn}>
        <TopBar />
        <div style={S.pageScrollArea}>
          <OverviewPage
            connectedBanks={CONNECTED_BANKS}
            animatedTotalBalance={animatedTotalBalance}
            totalBalance={totalBalance}
            totalMoneyIn={totalMoneyIn}
            totalMoneyOut={totalMoneyOut}
            onNavigate={() => {}}
          />
        </div>
      </div>
    </div>
  );
}
