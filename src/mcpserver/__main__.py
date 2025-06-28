from .deployment import mcp

def main():
    mcp.run()
    print("MCP server is running...")
    
if __name__ == "__main__":
    main()