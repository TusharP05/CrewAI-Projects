from crewai import Task
from tools import tool, paper_tool
from agents import news_researcher, news_writer, linker

# Research task
research_task = Task(
    description=(
        "Go through only top 5 peer-reviewed journals and papers in {topic}. Analyze the content and summarize the key findings, methodologies, and conclusions do not make more than 5 requests."
    ),
    expected_output='A detailed summary of key points, methodologies, and conclusions in a 3-page document.',
    tools=[tool, paper_tool],
    agent=news_researcher,
)

# Writing task with language model configuration
write_task = Task(
    description=(
        "Provide students researching a new topic with important details such as a summary of key findings, relevant research papers along with their links, and useful video links."
    ),
    expected_output='A comprehensive research paper with proper format along with citations. Guide students on how to go about writing a review paper by including literature review glossary etc. Divide the writing into four parts with headings - 1) Review of Research done till now (add references for the lines you quote from papers), 2) Useful Paper Links, 3) Video References, 4) A comprehensive guide on how to go about writing your own research papers on the topic, detailed description of how to approach each segment, and new ideas or improvements. Ensure that each heading and subheading is properly spaced from the content above it. Make sure to cite important lines.'
    'Add a newline after headings for better readability.Ensure the list items are correctly formatted with a newline before starting the list.' ,
    tools=[tool, paper_tool],
    agent=news_writer,
    async_execution=False,
    output_file= 'final.md'
)

link_finder= Task(
    description=(
        "search internet for the papers and journals related to {topic} and provide a list of 10 of them, along with their heading links(mostly of google scholar and springer and ieee and other reputed ones like nature) and authors and date, please do not provide broken links."),
    
     expected_output=' a file with 15 research papers, with author names and date and links',
    tools=[tool,paper_tool],
    agent=linker,
    async_execution=False,
    output_file= 'papers.md'

)
