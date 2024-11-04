import React, { useEffect, useState } from "react";
import { fetchProjects } from "../api";
import { Link } from "react-router-dom";

function HomePage() {
  const [projects, setProjects] = useState([]);

  useEffect(() => {
    const getProjects = async () => {
      try {
        const response = await fetchProjects();
        setProjects(response.data);
      } catch (error) {
        console.error("Error fetching projects:", error);
      }
    };
    getProjects();
  }, []);

  return (
    <div>
      <h1>Projects</h1>
      <ul>
        {projects.map((project) => (
          <li key={project.id}>
            <Link to={`/project/${project.id}`}>
              {project.name} - Goal: {project.goal_amount} {project.currency}
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default HomePage;
