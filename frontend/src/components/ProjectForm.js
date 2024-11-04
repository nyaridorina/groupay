import React, { useState } from "react";
import { createProject } from "../api";

function ProjectForm() {
  const [name, setName] = useState("");
  const [goalAmount, setGoalAmount] = useState("");
  const [currency, setCurrency] = useState("USD");

  const handleSubmit = async (e) => {
    e.preventDefault();
    await createProject({ name, goalAmount, currency });
  };

  return (
    <form onSubmit={handleSubmit}>
      <input value={name} onChange={(e) => setName(e.target.value)} placeholder="Project Name" />
      <input value={goalAmount} onChange={(e) => setGoalAmount(e.target.value)} placeholder="Goal Amount" />
      <input value={currency} onChange={(e) => setCurrency(e.target.value)} placeholder="Currency" />
      <button type="submit">Create Project</button>
    </form>
  );
}

export default ProjectForm;
