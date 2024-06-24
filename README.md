# Text Summarizer

## Overview

This project is a text summarizer implemented using Python, FastAPI, LangChain, and the open-source LLaMA model. The summarizer is designed to process and summarize text efficiently, leveraging advanced natural language processing capabilities.

## Features

- **Text Summarization**: Summarizes input text to provide a concise version of the original content.
- **FastAPI Integration**: Uses FastAPI to handle API requests and provide a scalable web interface.
- **LangChain Management**: Manages interactions with the LLaMA model using LangChain.
- **Open-Source LLaMA Model**: Utilizes the LLaMA model for natural language processing.

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Clone the Repository

```sh
cd text-summarizer
```

### Install Dependencies

```sh
pip install -r requirements.txt
Set Up LLaMA Model // (through Ollama it's just going to be ollama run $model, refer to: https://python.langchain.com/v0.1/docs/guides/development/local_llms/)
```

### Usage

Running the Server
Start the FastAPI server by running:

```sh
uvicorn main:app --reload
```
