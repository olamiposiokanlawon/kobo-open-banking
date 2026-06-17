import { CONNECTED_BANKS } from "../data/mockData";

export function formatNaira(amount, showDecimals = true) {
  const places = showDecimals ? 2 : 0;
  return "₦" + amount.toLocaleString("en-NG", {
    minimumFractionDigits: places,
    maximumFractionDigits: places,
  });
}

export function findBankById(bankId) {
  return (
    CONNECTED_BANKS.find((bank) => bank.id === bankId) ||
    { name: bankId, brandColor: "#64748B" }
  );
}
