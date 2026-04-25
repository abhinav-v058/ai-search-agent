# AI Search Agent

An intelligent agent powered by LangChain that can perform web searches and provide answers to user queries using AI models.

## Features

- 🤖 **AI-Powered Agent**: Built with LangChain for flexible agent creation
- 🔍 **Web Search**: Integrates Tavily for real-time web search capabilities
- 🧠 **Multiple LLM Support**: 
  - OpenAI's GPT-4 (default)
  - Local models via Ollama (e.g., Gemma 3)
- 📦 **Modern Python Stack**: Uses `uv` for dependency management

## Requirements

- Python 3.10+
- OpenAI API key (or local Ollama setup)
- Tavily API key

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd ai-search-agent
```

2. Install dependencies using `uv`:
```bash
uv sync
```

3. Create a `.env` file in the project root with your API keys:
```env
OPENAI_API_KEY=your_openai_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

## Usage

Run the agent with:
```bash
python main.py
```

The agent will process a sample query and return results with web search capabilities.

## Configuration

### LLM Selection

Edit `main.py` to switch between models:

**Using OpenAI GPT-4 (default):**
```python
llm = ChatOpenAI(model="gpt-4-0613", temperature=0)
```

**Using Local Ollama Model:**
```python
llm = ChatOllama(model="gemma3:270m", temperature=0)
```

## Project Structure

```
ai-search-agent/
├── main.py              # Main agent implementation
├── pyproject.toml       # Project configuration and dependencies
├── README.md           # This file
└── .env                # Environment variables (create this)
```

## Dependencies

- **langchain** (>=1.2.15) - Agent framework
- **langchain-openai** (>=1.2.0) - OpenAI integration
- **langchain-ollama** (>=1.1.0) - Ollama integration
- **langchain-tavily** (>=0.2.18) - Tavily search integration
- **tavily** (>=1.1.0) - Tavily API client
- **python-dotenv** (>=1.2.2) - Environment variable management
- **black** (>=26.3.1) - Code formatting
- **isort** (>=8.0.1) - Import sorting

## License

Open source project 
