from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.tools import tool
from app.config import VECTOR_DB_PATH, EMBEDDING_MODEL

# Initialize Embeddings & Vector DB
embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
vector_store = Chroma(
    collection_name="agent_memory",
    embedding_function=embeddings,
    persist_directory=VECTOR_DB_PATH
)

@tool
def save_memory(content: str):
    """
    Useful for saving important facts, research summaries, or user preferences 
    to long-term memory for future retrieval.
    """
    vector_store.add_texts([content])
    return f"Saved to memory: {content[:50]}..."

@tool
def recall_memory(query: str):
    """
    Useful for searching the agent's long-term memory for relevant facts 
    or past research.
    """
    results = vector_store.similarity_search(query, k=2)
    if not results:
        return "No relevant memories found."
    return "\n".join([doc.page_content for doc in results])
