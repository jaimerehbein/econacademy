import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run():
    server_params = StdioServerParameters(
        command="notebooklm-mcp",
        args=[],
        env=None
    )
    
    try:
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                
                print("--- AVAILABLE TOOLS ---")
                tools_response = await session.list_tools()
                for tool in tools_response.tools:
                    print(f"- {tool.name}: {tool.description}")
                
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    asyncio.run(run())
