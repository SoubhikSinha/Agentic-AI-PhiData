# Importing libraries
import typer
from typing import Optional, List
from phi.assistant import Assistant
# from phi.storage.agent.postgres import PgAssistantStorage
from phi.storage.assistant.postgres import PgAssistantStorage
from phi.knowledge.pdf import PDFUrlKnowledgeBase
from phi.vectordb.pgvector import PgVector2

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Setting up environment variables
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

# Database URL
db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

# Creating knowledge base
knowledge_base = PDFUrlKnowledgeBase(
    urls=["https://phi-public.s3.amazonaws.com/recipes/ThaiRecipes.pdf"],
    use_ocr=True, # 🌟
    vector_db=PgVector2(collection="recipes", db_url=db_url)
)

# Loading knowledge base
knowledge_base.load()

# Creating assistant
storage = PgAssistantStorage(table_name="pdf_assistant", db_url=db_url)

# def pdf_assistant(new: bool = False, user: str = "user"):
    # run_id: Optional[str] = None  # type: ignore

    # if not new: # Load existing run
    #     existing_run_ids: List[str] = storage.get_run_ids(user)
    #     if len(existing_run_ids) > 0:
    #         run_id = existing_run_ids[0]

    # if not new:
    #     runs = storage.list_runs(user_id=user)
    #     if runs:
    #         run_id = runs[0].id  # or runs[-1].id if you want the latest
    #         print(f"Continuing Run: {run_id}\n")
    #     else:
    #         print("No previous runs found, starting new...\n")

def pdf_assistant(user: str = "user"):
    assistant = Assistant(
        # run_id=run_id,
        user_id=user,
        knowledge_base=knowledge_base,
        storage=storage,
        # Showing tool calls in the response
        show_tool_calls=True,
        # Enabling the assistant to search the knowledge base
        search_knowledge=True,
        # Enabling the assistant to read the chat history
        read_chat_history=True,
    )

    # Only load last run if not starting new
    # if not new:
    #     try:
    #         past_runs = assistant.get_runs(user_id=user)
    #         if past_runs:
    #             run_id = past_runs[-1]["id"]
    #             assistant.run_id = run_id
    #             print(f"Continuing Run: {run_id}\n")
    #         else:
    #             print("No previous runs found — starting new.\n")
    #     except AttributeError:
    #         print("⚠️ Your phidata version does not expose get_runs(); starting a fresh run.\n")

    # if run_id is None:
    #     run_id = assistant.run_id
    #     print (f"Started Run: {run_id}\n")
    # else:
    #     print (f"Continuing Run: {run_id}\n")
    #     assistant.cli_app (markdown=True)

    # if run_id is None:
    #     print(f"Started new Run: {assistant.run_id}\n")

    print(f"Started new Run: {assistant.run_id}\n")
    assistant.cli_app(markdown=True)


# Running the assistant
if __name__ == "__main__":
    typer.run(pdf_assistant)