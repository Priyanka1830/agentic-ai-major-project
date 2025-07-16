from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class ResearchBuddy():
    """ResearchBuddy crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            verbose=True
        )

    @agent
    def research_article_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['research_article_writer'],
            verbose=True
        )

    @agent
    def research_article_editor(self) -> Agent:
        return Agent(
            config=self.agents_config['research_article_editor'],
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
        )

    @task
    def research_article_writer_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_article_writer_task'],
        )

    @task
    def research_article_editor_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_article_editor_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the ResearchBuddy crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
