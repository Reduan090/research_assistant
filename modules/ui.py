# modules/ui.py
import streamlit as st
from modules.document_handling import load_and_embed_document
from modules.paper_understanding import understand_paper
from modules.llm_engine import ask_llm

def setup_ui():
    """Setup Streamlit UI with tabs."""
    st.title("🧠 Research Bot")

    # Sidebar for global options
    st.sidebar.title("Settings")
    selected_llm = st.sidebar.selectbox("Select LLM", ["openai", "deepseek", "llama"], index=0)

    # Tabs for modules
    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
        "📄 Upload PDF", "📝 AI Writer", "🔍 Literature Review", "🧠 Ask a Paper",
        "📚 Topic Finder", "🔠 Grammar & Style", "📌 Citation/Reference Tool", "📉 Plagiarism Check"
    ])

    with tab1:  # Upload PDF (integrates with Module 2)
        st.header("Upload Document")
        uploaded_file = st.file_uploader("Choose a file (PDF/DOCX/TXT)", type=["pdf", "docx", "txt"])
        if uploaded_file:
            # Save to data dir
            file_path = f"data/{uploaded_file.name}"
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.success("File uploaded!")
            if st.button("Process and Embed"):
                embeddings = load_and_embed_document(file_path)
                st.write("Embeddings created and stored!")

    with tab2:  # AI Writer (uses Module 3 LLM)
        st.header("AI Writer")
        title = st.text_input("Enter title")
        keywords = st.text_input("Enter keywords (comma-separated)")
        if st.button("Generate Outline"):
            prompt = f"Generate an outline for an article titled '{title}' with keywords: {keywords}"
            response = ask_llm(prompt, model=selected_llm)
            st.write(response)

    with tab3:  # Literature Review (placeholder, expands later)
        st.header("Literature Review")
        query = st.text_input("Enter query")
        if st.button("Generate Review"):
            st.write("Coming soon...")  # Integrate with Module 10 later

    with tab4:  # Ask a Paper (integrates with Module 4)
        st.header("Ask a Paper")
        paper_input = st.text_input("Enter Paper URL/DOI or Upload PDF")
        question = st.text_input("Ask a question")
        if st.button("Understand Paper"):
            result = understand_paper(paper_input)
            st.write(result)
        if st.button("Answer Question"):
            prompt = f"Based on the paper, answer: {question}"
            response = ask_llm(prompt, model=selected_llm)  # Would use RAG in full impl
            st.write(response)

    # Other tabs as placeholders for now (expand as per later modules)
    with tab5:
        st.header("Topic Finder")
        st.write("Coming soon...")
    with tab6:
        st.header("Grammar & Style")
        st.write("Coming soon...")
    with tab7:
        st.header("Citation Tool")
        st.write("Coming soon...")
    with tab8:
        st.header("Plagiarism Check")
        st.write("Coming soon...")