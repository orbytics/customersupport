from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent


@CrewBase
class Customersupport():
    """Customersupport crew"""

    agents_config = "config/agents.yaml"
    tasks_config  = "config/tasks.yaml"

    @agent
    def customer_support_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['customer_support_agent'], # type: ignore[index]
            verbose=True
        )

    @task
    def support_task(self) -> Task:
        return Task(
            config=self.tasks_config['support_task'], # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Customersupport crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
