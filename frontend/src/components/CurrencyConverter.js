import React, { useState } from "react";
import { addExpense } from "../api";

function CurrencyConverter({ projectId }) {
  const [amount, setAmount] = useState("");
  const [currency, setCurrency] = useState("USD");

  const handleAddExpense = async () => {
    await addExpense({ amount, currency, project_id: projectId });
  };

  return (
    <div>
      <input value={amount} onChange={(e) => setAmount(e.target.value)} placeholder="Amount" />
      <input value={currency} onChange={(e) => setCurrency(e.target.value)} placeholder="Currency" />
      <button onClick={handleAddExpense}>Add Expense</button>
    </div>
  );
}

export default CurrencyConverter;
