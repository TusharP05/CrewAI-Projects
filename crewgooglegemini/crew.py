import json
from crewai import Crew, Process
from tasks import research_task, write_task, link_finder
from agents import news_researcher, news_writer, linker
import markdown
from bs4 import BeautifulSoup

def markdown_to_json(markdown_text):
    # Convert Markdown to HTML
    html = markdown.markdown(markdown_text)
    
    # Parse HTML
    soup = BeautifulSoup(html, 'html.parser')
    
    sections = {}
    current_heading = None
    current_content = []
    
    for element in soup.descendants:
        if element.name == 'h2' or element.name == 'h3' or element.name == 'h4':
            if current_heading:
                sections[current_heading] = ''.join(str(x) for x in current_content).strip()
            current_heading = element.get_text()
            current_content = []
        else:
            current_content.append(element)
    
    if current_heading:
        sections[current_heading] = ''.join(str(x) for x in current_content).strip()
    
    return sections

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
