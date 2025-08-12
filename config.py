# config.py
import os

# API Keys (set these as environment variables in production)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your-openai-key-here")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "your-deepseek-key-here")  # If using DeepSeek

# Default Models
DEFAULT_LLM_MODEL = "openai"
DEFAULT_EMBEDDING_MODEL = "text-embedding-3-small"  # OpenAI, or "BAAI/bge-base-en" for sentence-transformers

# Paths
DATA_DIR = "data"
VECTOR_DB_PATH = f"{DATA_DIR}/faiss_index"