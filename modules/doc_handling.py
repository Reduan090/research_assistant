# modules/document_handling.py
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings, HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import fitz  # PyMuPDF
import pdfplumber
from docx import Document
from config import DEFAULT_EMBEDDING_MODEL, VECTOR_DB_PATH, DATA_DIR

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

def load_document(file_path):
    """Load content from PDF/DOCX/TXT."""
    ext = os.path.splitext(file_path)[1].lower()
    if ext == ".pdf":
        with pdfplumber.open(file_path) as pdf:
            text = "\n".join(page.extract_text() for page in pdf.pages)
    elif ext == ".docx":
        doc = Document(file_path)
        text = "\n".join(para.text for para in doc.paragraphs)
    elif ext == ".txt":
        with open(file_path, "r") as f:
            text = f.read()
    else:
        raise ValueError("Unsupported file type")
    return text

def chunk_text(text):
    """Chunk text using LangChain splitter."""
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return splitter.split_text(text)

def get_embeddings(model_name=DEFAULT_EMBEDDING_MODEL):
    """Get embedding model."""
    if "openai" in model_name.lower():
        return OpenAIEmbeddings(model=model_name)
    elif "bge" in model_name.lower():
        return HuggingFaceEmbeddings(model_name="BAAI/bge-base-en")
    else:
        raise ValueError("Unsupported embedding model")

def load_and_embed_document(file_path):
    """Full pipeline: Load, chunk, embed, store in FAISS."""
    text = load_document(file_path)
    chunks = chunk_text(text)
    embeddings = get_embeddings()
    vectorstore = FAISS.from_texts(chunks, embeddings)
    vectorstore.save_local(VECTOR_DB_PATH)
    return vectorstore