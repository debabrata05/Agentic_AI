import sys
import os
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_mcp_adapters.client import MultiServerMCPClient
from app.memory import save_memory, recall_memory

# Standard web search tool
web_search = DuckDuckGoSearchRun()

async def get_tools():
    """
    Aggregates:
    1. Native Memory Tools (Chroma)
    2. Web Search
    3. YOUR CUSTOM MCP TOOLS (from app/my_server.py)
    """
    # Start with the basic tools
    tools = [save_memory, recall_memory, web_search]

    # Get the absolute path to your server script
    # This ensures Python can find it regardless of where you run main.py from
    server_script = os.path.abspath("../MCP_servers/server_1.py")

    try:
        # Connect to YOUR custom Python MCP server
        mcp_client = MultiServerMCPClient(
            {
                "my-custom-server": {
                    "command": sys.executable, # Uses the current python venv
                    "args": [server_script],
                    "transport": "stdio",
                }
            }
        )
        
        # This will load 'write_to_file' and 'calculate_metrics' automatically
        custom_mcp_tools = await mcp_client.get_tools()
        print(f"✅ Loaded {len(custom_mcp_tools)} tools from Custom MCP Server")
        
        tools.extend(custom_mcp_tools)
        
    except Exception as e:
        print(f"⚠️ Failed to connect to Custom MCP server: {e}")
        print("Tip: Make sure 'mcp' is installed: pip install mcp")

    return tools
