# LangChain Documentation Helper

A tool that helps you understand and work with LangChain documentation more effectively.

## Features

- Interactive documentation search
- Code examples and explanations
- Integration with LangChain's latest updates
- Custom query support for specific documentation needs

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
   Then add the missing variables to .env
6. Run the application using streamlit:
   ```bash
   streamlit run main.py
   ```

## Environment Setup

Required environment variables:

- OPENAI_API_KEY
- LANGCHAIN_API_KEY
- LANGCHAIN_TRACING_V2
- LANGCHAIN_PROJECT
- PINECONE_API_KEY
- PINECONE_INDEX_NAME

## Usage

The tool provides an interactive interface to:

- Search through LangChain documentation
- Get explanations for specific concepts
- Find relevant code examples
- Understand best practices

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
