from mcp.server.fastmcp import FastMCP

# Initialize your custom server
mcp = FastMCP("My Custom Agent Server")

# --- Define Your Custom Tools Here ---

@mcp.tool()
def write_to_file(filename: str, content: str) -> str:
    """
    Writes content to a file in the workspace. 
    Useful for creating reports, code files, or logs.
    """
    try:
        # Security: ensure we only write to the workspace directory
        safe_path = f"./workspace/{filename}"
        with open(safe_path, "w", encoding="utf-8") as f:
            f.write(content)
        
        return f"✅ Successfully wrote {len(content)} characters to {safe_path}."
    except Exception as e:
        return f"❌ Error writing file: {str(e)}"

@mcp.tool()
def calculate_metrics(data: list[float]) -> str:
    """
    A custom tool to demonstrate logic that is hard for an LLM to do precisely.
    Calculates sum, average, and max of a list of numbers.
    """
    if not data:
        return "No data provided."
    return f"Sum: {sum(data)}, Avg: {sum(data)/len(data)}, Max: {max(data)}"

if __name__ == "__main__":
    # This command starts the server on Stdio so the Agent can talk to it
    mcp.run(transport="stdio")
