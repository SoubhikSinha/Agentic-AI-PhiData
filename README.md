# Agentic AI @ PhiData

Agentic-AI-PhiData is a compact demonstration of modular **Agentic AI** built using the phi framework, combining **Groq-powered LLMs** with tool-based reasoning for finance, web search, document intelligence, and multimedia understanding. The repository includes playground.py (initializes agents using `Groq(id="llama-3.1-8b-instant")` along with `DuckDuckGo` and `YFinanceTools` for live insights), `financial_agent.py` (an autonomous finance agent performing real-time stock and market analysis), `PDFAssistant/pdfAssistant.py` (a document agent capable of reading, chunking, and reasoning over PDFs), and `Video Summarizer/app.py` (a video summarizer agent that processes long-form video content into concise, structured summaries). All agents rely on environment variables (.env with `GROQ_API_KEY`, `OPENAI_API_KEY`) managed via dotenv, with dependencies listed in requirements.txt. Together, they showcase end-to-end agentic workflows for financial forecasting, web data retrieval, PDF-based Q&A, and video summarization using tools like phi, Groq, DuckDuckGo, YFinanceTools, and OpenAI. Users can install dependencies using pip install -r requirements.txt, run agents independently, and extend the system toward enterprise-scale **RAG** or **multi-agent architectures**, with future support for **FAISS**, **Pinecone**, and cross-agent communication.
<br>
<br>

**Reference:**
[Krish Naik](https://github.com/krishnaik06)
