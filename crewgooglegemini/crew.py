import json
from crewai import Crew, Process
from tasks import research_task, write_task, link_finder
from agents import news_researcher, news_writer, linker

from bs4 import BeautifulSoup



# Forming the tech-focused crew with some enhanced configuration
crew = Crew(
    agents=[news_researcher, news_writer, linker],
    tasks=[research_task, write_task, link_finder],
    process=Process.sequential,
)

def gather_results(topic):
    try:
        result = crew.kickoff(inputs={'topic': topic})
        
        # Debugging statement to print raw result
        
    
    except Exception as e:
        print(f"Error in gather_results: {e}")  # Debugging print statement
        return {'error': str(e)}
