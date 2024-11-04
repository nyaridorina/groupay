import axios from "axios";

const api = axios.create({
  baseURL: "https://groupay.onrender.com",
});

export const fetchProjects = () => api.get("/projects");
export const createProject = (data) => api.post("/projects", data);
export const addExpense = (data) => api.post("/expenses", data);
