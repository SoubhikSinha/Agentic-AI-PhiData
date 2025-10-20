# Importing libraries
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
import os
import openai

# Load environment variables from .env file
load_dotenv()

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
openai.api_key = os.getenv("OPENAI_API_KEY")

'''
NOTE : By default, Agent() method considers OpenAI model - until specified otherwise.
'''

# Creating Web-Search Agent
web_search_agent=Agent(
    name="Web Search Agent", # Agent Name
    role="Search the web for the information", # Role of the agent
    model=Groq(id="llama-3.1-8b-instant"), # LLM Model
    tools=[DuckDuckGo()], # Tools (Web Search)
    instructions=["Always include sources"], # Custom Instructions
    memory={}, # Disable memory
    show_tools_calls=True,
    markdown=True
)

# Creating Financial Agent
finance_agent=Agent(
    name="Finance AI Agent",
    model=Groq(id="llama-3.1-8b-instant"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,
                      company_news=True),
    ],
    instructions=["Use tables to display the data"],
    memory={}, # Disable memory
    show_tools_calls=True, # Show tool calls
    markdown=True
)

# Creating Multi-AI-Agent
multi_ai_agent=Agent(
    team=[web_search_agent, finance_agent],
    instructions=["Always include sources", "Use table to display the data"],
    memory={}, # Disable memory
    markdown=True,
)

# Initialize the agents
# multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news for NVDA", stream=True)
multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news for NVDA")