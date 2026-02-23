import asyncio
import os
import json
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def test_notebook_query():
    # Attempting to manually trigger the synthesis for A5 using the notebook ID
    notebook_id = "8a00eb64-5110-4ae9-b677-accc805612cf"
    task_id = "66d892fa-ad62-4c18-84a5-a348bcb35da1"
    
    server_params = StdioServerParameters(
        command="notebooklm-mcp",
        args=["--query-timeout", "300"],
        env=None
    )
    
    print(f"=== Lanzando Test Synthesis Directo para Notebook: {notebook_id} ===")
    
    try:
        async with stdio_client(server_params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                
                print("1. Forzando Importacion de Fuentes...")
                import_res = await session.call_tool("research_import", arguments={
                    "notebook_id": notebook_id,
                    "task_id": task_id
                })
                print(f"Import Res: {import_res}")
                
    except Exception as e:
        print(f"Error test: {e}")

if __name__ == "__main__":
    asyncio.run(test_notebook_query())
