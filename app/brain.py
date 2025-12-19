from langchain_ollama import ChatOllama
from config.config import MODEL_NAME

def get_llm():
    """
    Returns the configured Ollama LLM instance.
    We set temperature to 0 for deterministic tool usage.
    """
    return ChatOllama(
        model=MODEL_NAME,
        temperature=0,
        keep_alive="5m"  # Keep model in VRAM
    )
