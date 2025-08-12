# modules/paper_understanding.py
from modules.llm_engine import ask_llm
from utils.helpers import fetch_api
from modules.document_handling import load_document

def extract_metadata(doi_or_url):
    """Fetch metadata using CrossRef API."""
    if "doi" in doi_or_url.lower():
        url = f"https://api.crossref.org/works/{doi_or_url}"
    else:
        # Assume URL; fetch via Semantic Scholar or similar
        url = f"https://api.semanticscholar.org/v1/paper/URL:{doi_or_url}"
    data = fetch_api(url)
    if data:
        return {
            "title": data.get("title"),
            "authors": data.get("author", []),
            "year": data.get("published", {}).get("date-parts", [[None]])[0][0],
            "institution": data.get("container-title"),
            "source": data.get("DOI") or doi_or_url
        }
    return {}

def summarize_paper(text, model="openai"):
    prompt = "Summarize this research paper section-wise or in abstract style."
    return ask_llm(prompt + "\n\n" + text, model=model)

def extract_key_points(text, model="openai"):
    prompt = "Extract key points from this paper."
    return ask_llm(prompt + "\n\n" + text, model=model)

def generate_glossary(text, model="openai"):
    prompt = "Create a glossary of terms with definitions from this academic paper."
    return ask_llm(prompt + "\n\n" + text, model=model)

def understand_paper(input_path_or_doi):
    """Full module: Handle input, extract, summarize."""
    if input_path_or_doi.startswith("http") or "doi" in input_path_or_doi.lower():
        metadata = extract_metadata(input_path_or_doi)
        # Fetch full text via Unpaywall or similar (placeholder)
        text = "Full text fetching not implemented; using metadata."  # Expand with API
    else:
        text = load_document(input_path_or_doi)
        metadata = {}  # Extract from text if needed

    summary = summarize_paper(text)
    key_points = extract_key_points(text)
    glossary = generate_glossary(text)

    return {
        "metadata": metadata,
        "summary": summary,
        "key_points": key_points,
        "glossary": glossary
    }