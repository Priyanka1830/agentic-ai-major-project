from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, FileWriterTool
from typing import List
from dotenv import load_dotenv

load_dotenv()

@CrewBase
class AiNews():
    """AiNews crew"""

    agents: List[BaseAgent]
    tasks: List[Task]


    @agent
    def retrieve_news(self) -> Agent:
        return Agent(
            config=self.agents_config['retrieve_news'],
            tools=[SerperDevTool()],
            verbose=True
        )

    @agent
    def website_scraper(self) -> Agent:
        return Agent(
            config=self.agents_config['website_scraper'],
            tools=[ScrapeWebsiteTool()],
            verbose=True
        )

    @agent
    def ai_news_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['ai_news_writer'],
            verbose=True
        )

    @agent
    def file_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['file_writer'],
            tools=[FileWriterTool()],
            verbose=True
        )

    @task
    def retrieve_news_task(self) -> Task:
        return Task(
            config=self.tasks_config['retrieve_news_task'],
        )

    @task
    def website_scrape_task(self) -> Task:
        return Task(
			config=self.tasks_config['website_scrape_task'],
        )
	
    @task
    def ai_news_write_task(self) -> Task:
        return Task(
			config=self.tasks_config['ai_news_write_task'],
        )
	
    @task
    def file_write_task(self) -> Task:
        return Task(
			config=self.tasks_config['file_write_task'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the AiNews crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
