from flask import Flask, request, jsonify
import os
import asyncio
import logging
from crew import gather_results  # Import the gather_results function from crew.py

app = Flask(__name__)

@app.route('/research', methods=['POST'])
def run_research():
    data = request.json
    topic = data.get('topic')

    if not topic:
        return jsonify({'error': 'Topic is required'}), 400

    try:
        # Run the tasks with the given topic and gather results
        result = asyncio.run(gather_results_async(topic))

        # Assuming gather_results generates 'final.md'
        markdown_file = 'final.md'

        if not os.path.exists(markdown_file):
            return jsonify({'error': 'Markdown file not found'}), 404

        # Read the Markdown content from the file
        with open(markdown_file, 'r') as f:
            markdown_content = f.read()

        # Return the Markdown content as text
        return markdown_content, 200, {'Content-Type': 'text/markdown'}

    except Exception as e:
        logging.error(f"Error in /research: {str(e)}")
        return jsonify({'error': str(e)}), 500

async def gather_results_async(topic):
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, gather_results, topic)
    return result

@app.route('/research', methods=['GET'])
def get_sample_research():
    sample_data = """
    # Review of Research done till now
    This section will contain the summary of key findings with references.

    ## Useful Paper Links
    - [Link to paper 1](https://linktopaper1.com)
    - [Link to paper 2](https://linktopaper2.com)

    ## Video References
    - [Link to video 1](https://linktovideo1.com)
    - [Link to video 2](https://linktovideo2.com)

    ## Guide on Writing Research Papers
    This section will provide a comprehensive guide on writing research papers with detailed descriptions.
    """
    return sample_data, 200, {'Content-Type': 'text/markdown'}

@app.route('/papers', methods=['POST'])
def run_papers():
    data = request.json
    topic = data.get('topic')

    if not topic:
        return jsonify({'error': 'Topic is required'}), 400

    try:
        # Run the tasks with the given topic and gather results
        result = asyncio.run(gather_results_async(topic))

        # Assuming gather_results generates 'final.md'
        markdown_file = 'papers.md'

        if not os.path.exists(markdown_file):
            return jsonify({'error': 'Markdown file not found'}), 404

        # Read the Markdown content from the file
        with open(markdown_file, 'r', encoding='utf-8', errors='ignore') as f:
            markdown_content = f.read()

        # Return the Markdown content as text
        return markdown_content, 200, {'Content-Type': 'text/markdown'}

    except Exception as e:
        logging.error(f"Error in /papers: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
