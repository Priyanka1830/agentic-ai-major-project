from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class ProductPriceResearcherCrew():
    """ProductPriceResearcherCrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def product_query_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['product_query_generator'], # type: ignore[index]
            verbose=True
        )

    @agent
    def serper_search_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['serper_search_agent'], # type: ignore[index]
            verbose=True
        )

    @agent
    def price_availability_extractor(self) -> Agent:
        return Agent(
            config=self.agents_config['price_availability_extractor'], # type: ignore[index]
            verbose=True
        )

    @agent
    def change_detector(self) -> Agent:
        return Agent(
            config=self.agents_config['change_detector'], # type: ignore[index]
            verbose=True
        )

    @agent
    def pricing_advisor(self) -> Agent:
        return Agent(
            config=self.agents_config['pricing_advisor'], # type: ignore[index]
            verbose=True
        )


    @task
    def product_query_generator_task(self) -> Task:
        return Task(
            config=self.tasks_config['product_query_generator_task'], # type: ignore[index]
            verbose=True
        )

    @task
    def serper_search_task(self) -> Task:
        return Task(
            config=self.tasks_config['serper_search_task'], # type: ignore[index]
            verbose=True
        )

    @task
    def price_availability_extractor_task(self) -> Task:
        return Task(
            config=self.tasks_config['price_availability_extractor_task'], # type: ignore[index]
            verbose=True
        )

    @task
    def change_detector_task(self) -> Task:
        return Task(
            config=self.tasks_config['change_detector_task'], # type: ignore[index]
            verbose=True
        )

    @task
    def pricing_advisor_task(self) -> Task:
        return Task(
            config=self.tasks_config['pricing_advisor_task'], # type: ignore[index]
            verbose=True
        )

    @crew
    def crew(self) -> Crew:
        """Creates the ProductPriceResearcher crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
