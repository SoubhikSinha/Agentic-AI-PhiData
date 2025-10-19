# Importing libraries
from phi.agent import Agent
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.model.groq import Groq
from dotenv import load_dotenv
import os
import openai
import phi.api
import phi
from phi.playground import serve_playground_app, Playground


# Load environment variables from .env file
load_dotenv()

phi.api=os.getenv("PHIDATA_KEY")

# Creating Web-Search Agent
web_search_agent=Agent(
    name="Web Search Agent", # Agent Name
    role="Search the web for the information", # Role of the agent
    model=Groq(id="llama-3.1-8b-instant"), # LLM Model
    tools=[DuckDuckGo()], # Tools (Web Search)
    instructions=["Always include sources"], # Custom Instructions
    # memory={}, # Disable memory
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
    # memory={}, # Disable memory
    show_tools_calls=True, # Show tool calls
    markdown=True
)

# Playground app
app = Playground(
    agents=[web_search_agent, finance_agent]
).get_app()

# Starting app
if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True)