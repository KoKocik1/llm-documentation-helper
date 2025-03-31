# LangChain Documentation Helper

A tool that helps you understand and work with LangChain documentation more effectively. This application provides an interactive interface to search and explore LangChain documentation using natural language queries.

## Features

- Interactive documentation search with natural language processing
- Real-time chat interface for querying documentation
- Code examples and explanations from official LangChain docs
- Integration with LangChain's latest updates
- Custom query support for specific documentation needs
- Vector database storage of documentation for efficient searching
- Source attribution for all documentation references
- User-friendly Streamlit interface with chat history
- Persistent chat history during session

## Prerequisites

- Python 3.12
- pipenv for dependency management
- OpenAI API key
- Pinecone API key
- LangChain API key

## Getting Started

1. Clone this repository
2. Install pipenv if not already installed:
   ```bash
   pip install pipenv
   ```
3. Install dependencies using pipenv:
   ```bash
   pipenv install
   ```
4. Activate the virtual environment:
   ```bash
   pipenv shell
   ```
5. Copy `.env.copy` to `.env` and add your API keys:
   ```bash
   cp .env.copy .env
   ```
6. Run the ingestion script to create vector database:
   ```bash
   python ingestion.py
   ```
   This script crawls the LangChain documentation, processes the content, and stores it in a Pinecone vector database for efficient semantic searching.
7. Run the application using streamlit:
   ```bash
   streamlit run main.py
   ```

## Environment Setup

Required environment variables in `.env`:

- `OPENAI_API_KEY`: Your OpenAI API key for embeddings and LLM
- `LANGCHAIN_API_KEY`: Your LangChain API key
- `LANGCHAIN_TRACING_V2`: Enable/disable LangChain tracing
- `LANGCHAIN_PROJECT`: Your LangChain project name
- `PINECONE_API_KEY`: Your Pinecone API key
- `PINECONE_INDEX_NAME`: Name of your Pinecone index

## Project Structure

- `main.py`: Main Streamlit application interface
- `ingestion.py`: Script for processing and ingesting documentation
- `Backend/`: Core functionality and utilities
- `langchain-docs/`: Local copy of LangChain documentation

## Dependencies

Key dependencies include:

- langchain
- langchain-community
- langchain-pinecone
- langchain-openai
- streamlit
- beautifulsoup4
- firecrawl-py

## Usage

The application provides an interactive chat interface where you can:

1. Enter your questions about LangChain in natural language
2. Get comprehensive answers with relevant code examples
3. Access source documentation through provided links
4. Maintain conversation history during your session
5. View your profile and application information in the sidebar

The search functionality is powered by a vector database created during the ingestion process, allowing for semantic search and quick retrieval of relevant documentation.
