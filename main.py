from crewai import Crew,Process
from crew.tasks import news_researcher_task, news_writer_task
from crew.agents import news_researcher_agent,news_writer_agent

crew=Crew(
    agents=[news_researcher_agent,news_writer_agent],
    tasks=[news_researcher_task,news_writer_task],
    process=Process.sequential,
)

def main():
    topic= input("Enter the topic for News Article:\n")

    inputs={'topic': topic}
    crew.kickoff(inputs)

if __name__ == '__main__':
    main()