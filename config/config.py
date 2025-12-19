import os

# Configuration Settings
MODEL_NAME = "llama3.1"  # Make sure to run: ollama pull llama3.1
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
VECTOR_DB_PATH = "./chroma_db_data"

# Create workspace for file operations if it doesn't exist
if not os.path.exists("./workspace"):
    os.makedirs("./workspace")
