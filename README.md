# AI Podcast Assistant

AI Podcast Assistant is a custom chatbot designed to assist with various podcast-related tasks using Langchain and Large Language Models (LLMs). This assistant can help with tasks such as summarizing podcast episodes, generating show notes, extracting key highlights, and more.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Summarization**: Summarizes podcast episodes to provide a concise overview.
- **Show Notes Generation**: Automatically generates detailed show notes from podcast transcripts.
- **Highlight Extraction**: Extracts key highlights and important moments from podcast episodes.
- **Q&A**: Answers questions related to podcast content.


## Installation

To set up the AI Podcast Assistant, follow these steps:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/ai-podcast-assistant.git
    cd ai-podcast-assistant
    ```

2. **Create and activate a virtual environment** (optional but recommended):
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required packages**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To use the AI Podcast Assistant, follow these steps:

1. **Set up environment variables**: Create a `.env` file and add your API keys and other configuration details. For example:
    ```sh
    OPENAI_API_KEY=your_openai_api_key
    ```

2. **Run the chatbot**:
    ```sh
    python main.py
    ```

3. **Interact with the chatbot**: Once the chatbot is running, you can interact with it via the command line or integrate it with a messaging platform.

## Configuration

The AI Podcast Assistant can be configured using environment variables or a configuration file. Below are some of the configurable options:

- `OPENAI_API_KEY`: Your OpenAI API key.
- `MODEL_NAME`: The name of the language model to use (e.g., `gpt-4`).
- `PROMPT_TEMPLATES`: Path to custom prompt templates if any.


## Examples

Here are some example interactions with the AI Podcast Assistant:

### Summarization

**Input**: "Summarize the latest episode of the podcast."

**Output**: "In this episode, the host discusses the impact on cold exposure on the immune system, featuring an interview with a leading expert in the field..."

### Information Search

**Input**: "In which episode can find the information about the benefits of sauna?"

**Output**: "To find more information about the benefits of sauna, please check the episode 5. (link)"


