import asyncio

from fastmcp import Client

async def test_server():
    # Test the MCP server using sse transport
    async with Client("http://localhost:8080/sse") as client:
        # List available tools
        tools = await client.list_tools()
        for tool in tools:
            print(f">>> 🛠️  Tool found: {tool.name}")
        # Call add tool
        print(">>> 🪛  Calling add tool for 1 + 2")
        result = await client.call_tool("add", {"a": 1, "b": 2})
        print(f"<<< ✅ Result: {result[0].text}")
        # Call subtract tool
        print(">>> 🪛  Calling subtract tool for 10 - 3")
        result = await client.call_tool("subtract", {"a": 10, "b": 3})
        print(f"<<< ✅ Result: {result[0].text}")

if __name__ == "__main__":
    asyncio.run(test_server())