import asyncio
import socket
from browser_use import Agent, Browser, ChatBrowserUse, ChatGoogle, ChatOpenAI
from pydantic_settings import BaseSettings


def get_browser_ip(port = 9222):
    """remote debugging session blocks non-IP access if not localhost"""
    try:
        docker_ip = socket.gethostbyname('host.docker.internal')
        print(docker_ip)
        return f"http://{docker_ip}:{port}"
    except:
        return '172.17.0.1' # Fallback for standard Linux Docker

TASK = """
1. Visit page https://hok-elanto.fi/s-etukortti/ajankohtaista-asiakasomistajalle
2. Check bonus doubled (bonus tuplana) on the page and determine the campaign offerings, summarize in json format with shop short name and date
"""

async def run_task():
    
    agent = Agent(
        task=TASK,
        llm=ChatOpenAI(model="gpt-5.4-nano"),  # ChatGoogle(model="gemini-2.0-flash")
        browser=Browser(cdp_url=get_browser_ip()),
    )
    history = await agent.run()

if __name__ == "__main__":
    asyncio.run(run_task())