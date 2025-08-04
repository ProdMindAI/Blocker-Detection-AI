# Blocker-Detection-AI
A proof-of-concept NLP agent that uses a custom RAG framework to detect project blockers, risks, and cross-team misalignments from status updates. Built with LangChain, OpenAI, and vector-based retrieval.

## Features
- Document loading and indexing with FAISS
- RAG-based QA using OpenAI + LangChain
- Simple API interface via FastAPI


## Environment Variable Requirement

This application requires an OpenAI API key for the language model to function. Please set the environment variable `OPENAI_API_KEY` with your OpenAI API key before running the application.

Example:

Linux/macOS (bash):
``` bash
export OPENAI_API_KEY="your_openai_api_key_here"
```
Windows (PowerShell):
``` bash
setx OPENAI_API_KEY "your_openai_api_key_here"
```

Make sure to restart your terminal or IDE after setting the environment variable.

## Running the PMBuddy Client

Run App:
```bash
uvicorn main:app --reload --port 8000
```

The `client.py` script provides a simple terminal interface to interact with the PMBuddy API.

### Prerequisites

Make sure you have installed the required dependencies, including `requests`:

```bash
pip install -r requirements.txt
```
