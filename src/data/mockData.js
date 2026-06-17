export const CONNECTED_BANKS = [
  { id: "access",  name: "Access Bank",  shortName: "Access",    brandColor: "#E85C2B", balance: 842500.75,   maskedAccount: "•••• 4471", accountType: "Savings"  },
  { id: "gtco",    name: "GTBank",       shortName: "GTBank",    brandColor: "#E94E1B", balance: 1290340.00,  maskedAccount: "•••• 8820", accountType: "Current"  },
  { id: "first",   name: "First Bank",   shortName: "FirstBank", brandColor: "#11366B", balance: 318900.20,   maskedAccount: "•••• 0193", accountType: "Savings"  },
  { id: "uba",     name: "UBA",          shortName: "UBA",       brandColor: "#D8232A", balance: 67450.00,    maskedAccount: "•••• 7765", accountType: "Current"  },
  { id: "stanbic", name: "Stanbic IBTC", shortName: "Stanbic",   brandColor: "#0033A0", balance: 2104780.50,  maskedAccount: "•••• 3309", accountType: "Savings"  },
];

export const TRANSACTIONS = [
  { id: 1,  bankId: "stanbic", description: "Salary — Andela",                category: "Income",        amount: 1850000, timestamp: "Today, 09:12",     isOutgoing: false },
  { id: 2,  bankId: "gtco",    description: "Jumia Order #88231",              category: "Shopping",      amount: 47200,   timestamp: "Today, 08:40",     isOutgoing: true  },
  { id: 3,  bankId: "access",  description: "MTN Airtime",                     category: "Bills",         amount: 5000,    timestamp: "Yesterday, 21:05", isOutgoing: true  },
  { id: 4,  bankId: "uba",     description: "Transfer to Chidinma",            category: "Transfer",      amount: 25000,   timestamp: "Yesterday, 17:33", isOutgoing: true  },
  { id: 5,  bankId: "stanbic", description: "Refund — Bolt",                   category: "Transport",     amount: 3400,    timestamp: "Yesterday, 14:18", isOutgoing: false },
  { id: 6,  bankId: "first",   description: "Shoprite Lekki",                  category: "Groceries",     amount: 38950,   timestamp: "12 Jun, 19:44",    isOutgoing: true  },
  { id: 7,  bankId: "gtco",    description: "Netflix",                         category: "Subscriptions", amount: 4400,    timestamp: "12 Jun, 06:00",    isOutgoing: true  },
  { id: 8,  bankId: "access",  description: "Freelance — Pixelhaus",           category: "Income",        amount: 420000,  timestamp: "11 Jun, 11:27",    isOutgoing: false },
  { id: 9,  bankId: "stanbic", description: "DSTV Premium",                    category: "Bills",         amount: 44500,   timestamp: "11 Jun, 08:15",    isOutgoing: true  },
  { id: 10, bankId: "uba",     description: "TotalEnergies — Filling Station", category: "Transport",     amount: 30000,   timestamp: "10 Jun, 16:52",    isOutgoing: true  },
];

export const NAV_ITEMS = [
  { id: "overview",     label: "Overview"     },
  { id: "transactions", label: "Transactions" },
  { id: "insights",     label: "Insights"     },
  { id: "banks",        label: "Banks"        },
];
