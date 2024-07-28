## https://serper.dev/

from dotenv import load_dotenv
load_dotenv()
import os

os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')
os.environ['EXA_API_KEY']= os.getenv('EXA_API_KEY')
os.environ['GOOGLE_API_KEY']=os.getenv('GOOGLE_API_KEY')

from crewai_tools import (SerperDevTool,
                          EXASearchTool,
)


# Initialize the tool for internet searching capabilities

tool = SerperDevTool()
paper_tool= EXASearchTool()
