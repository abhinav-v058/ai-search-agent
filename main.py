from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from pprint import pprint
from tavily import TavilyClient
from langchain_tavily import TavilySearch

tavily = TavilyClient()


@tool
def search(query: str) -> str:
    """Search the web for the given query and return the results.
    Args:
        query (str): The search query.
    Returns:
        str: The search results.
    """

    print(f"Search results for '{query}'")
    search_results = tavily.search(query=query)
    pprint(search_results)
    return str(search_results)

llm = ChatOpenAI(model="gpt-4-0613", temperature=0)
#llm = ChatOllama(model="gemma3:270m", temperature=0)
#tools = [search]
tools = [TavilySearch()]
agent = create_agent(llm, tools)


def main():
    print("Hello from ai-search-agent!")
    result = agent.invoke({"messages": [HumanMessage(content="What is Fresh Production Application in Walmart?")]})
    pprint(result)


if __name__ == "__main__":
    main()
