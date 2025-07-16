from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class RoadMapBuddy():
    """RoadMapBuddy crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def topic_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['topic_analyst'],
            verbose=True
        )

    @agent
    def resource_finder(self) -> Agent:
        return Agent(
            config=self.agents_config['resource_finder'],
            verbose=True
        )

    @agent
    def syllabus_designer(self) -> Agent:
        return Agent(
            config=self.agents_config['syllabus_designer'],
            verbose=True
        )

    @agent
    def schedule_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['schedule_generator'],
            verbose=True
        )

    @task
    def topic_analyst_task(self) -> Task:
        return Task(
            config=self.tasks_config['topic_analyst_task'],
        )

    @task
    def resource_finder_task(self) -> Task:
        return Task(
            config=self.tasks_config['resource_finder_task']
        )

    @task
    def syllabus_designer_task(self) -> Task:
        return Task(
            config=self.tasks_config['syllabus_designer_task'],
        )

    @task
    def schedule_generator_task(self) -> Task:
        return Task(
            config=self.tasks_config['schedule_generator_task']
        )

    @crew
    def crew(self) -> Crew:
        """Creates the RoadMapBuddy crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
