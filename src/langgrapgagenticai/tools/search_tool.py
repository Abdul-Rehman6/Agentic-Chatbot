from langchain_tavily import TavilySearch
from langgraph.prebuilt import ToolNode

def get_tools():
    """
    Returns the list of tools to be used in the chatbot
    """

    tools = [TavilySearch(max_results = 2)]

    return tools

def create_tool_node(tools):
    """
    Creates and returns a Toolnode fot the graph"""

    return ToolNode(tools = tools)