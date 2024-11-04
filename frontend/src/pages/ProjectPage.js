import React, { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import { fetchProjects, addExpense } from "../api";
import ExpenseList from "../components/ExpenseList";
import CurrencyConverter from "../components/CurrencyConverter";

function ProjectPage() {
  const { projectId } = useParams();
  const [project, setProject] = useState(null);
  const [expenses, setExpenses] = useState([]);

  useEffect(() => {
    const getProject = async () => {
      try {
        const response = await fetchProjects();
        const projectData = response.data.find(p => p.id === parseInt(projectId));
        setProject(projectData);
        setExpenses(projectData.expenses || []);
      } catch (error) {
        console.error("Error fetching project:", error);
      }
    };
    getProject();
  }, [projectId]);

  const handleAddExpense = async (newExpense) => {
    try {
      const response = await addExpense(newExpense);
      setExpenses([...expenses, response.data]);
    } catch (error) {
      console.error("Error adding expense:", error);
    }
  };

  if (!project) return <div>Loading...</div>;

  return (
    <div>
      <h2>{project.name}</h2>
      <p>Goal: {project.goal_amount} {project.currency}</p>
      <p>Status: {project.is_archived ? "Archived" : "Active"}</p>

      <h3>Expenses</h3>
      <ExpenseList expenses={expenses} />

      <h3>Add Expense</h3>
      <CurrencyConverter projectId={projectId} onAddExpense={handleAddExpense} />
    </div>
  );
}

export default ProjectPage;
