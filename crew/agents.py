import os
from tools import search_tool
from crewai import Agent, LLM
from dotenv import load_dotenv
load_dotenv()


llm = LLM(model='gemini/gemini-1.5-flash', api_key=os.getenv("GOOGLE_API_KEY"))

news_researcher_agent=Agent(
    role="Senior News Researcher",
    goal='Unccover ground breaking News or advancements in {topic}',
    backstory="Driven by curiosity, you're at the forefront of innovation, eager to explore and share knowledge that could change the world.",
    verbose=True,
    memory=True,
    tools=[search_tool],
    llm=llm,
    allow_delegation=True
)

news_writer_agent = Agent(
  role='Writer',
  goal='Narrate compelling tech stories about {topic}',
  verbose=True,
  memory=True,
  backstory="With a flair for simplifying complex topics, you craft engaging narratives that captivate and educate, bringing new discoveries to light in an accessible manner.",
  tools=[search_tool],
  llm=llm,
)
