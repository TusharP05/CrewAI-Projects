from crewai import Agent
from tools import tool, paper_tool
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import os


## call the gemini models
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                           verbose=True,
                           temperature=0.5,
                           google_api_key=("AIzaSyAiXQTtkrnvA-v9cJaMASwXaz4etgkKon0"))

# Creating a senior researcher agent with memory and verbose mode

news_researcher=Agent(
    role="Research Summarizer",
    goal='Analyze and summarize research papers and journals on {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "you are an expert researcher with a keen eye for detail, capable of distilling complex research papers into concise, comprehensive summaries."

    ),
    tools=[tool, paper_tool],
    llm=llm,
    allow_delegation=True

)

## creating a write agent with custom tools responsible in writing news blog

news_writer = Agent(
  role='Writer',
  goal='Summarize what is the current status of research of {topic}',
  verbose=True,
  memory=True,
  backstory=(
    "With a flair for simplifying complex topics, you craft"
    "engaging narratives that captivate and educate, bringing new"
    "discoveries to light in an accessible manner."
  ),
  tools=[tool, paper_tool],
  llm=llm,
  allow_delegation=False
)

linker= Agent(
  role='researcher',
  goal='find research papers and journals',
  verbose=True,
  memory=True,
   backstory=(
    "With a flair for reaseraching around the world, you find"
    "out the most important highlights and details from papers and journals, bringing new"
    "discoveries to light in an accessible manner."
  ),
  tools=[tool, paper_tool],
  llm=llm,
  allow_delegation=False
  
)

