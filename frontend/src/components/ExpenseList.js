import React from "react";

function ExpenseList({ expenses }) {
  return (
    <ul>
      {expenses.map((expense) => (
        <li key={expense.id}>
          {expense.contributor}: {expense.amount} ({expense.status}) - {expense.comment}
        </li>
      ))}
    </ul>
  );
}

export default ExpenseList;
