# 🤖 The Sovereign Agent

A production-ready implementation of an Autonomous AI Agent using the **Sovereign Stack**: Ollama, LangGraph, MCP, and FastAPI.

## 🏗 Architecture
- **Brain:** Ollama (Llama 3.1)
- **Tools:** Custom Python MCP Server (FileSystem, Math)
- **Memory:** ChromaDB (Local Vector Store)
- **Orchestration:** LangGraph (ReAct Loop)

## 🚀 Usage

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
2. **Start Ollama:**
   ```bash
   ollama serve
   ollama pull llama3.1
3. **Run the Server:**
   ```bash
   python client_test.py
4. **Run the Client:**
   ```bash
   python client_test.py
