# modules/llm_engine.py
from openai import OpenAI
from config import OPENAI_API_KEY, DEEPSEEK_API_KEY
# Assuming DeepSeek and LLaMA wrappers; replace with actual if available
# For LLaMA, use huggingface_hub or ollama if installed

client_openai = OpenAI(api_key=OPENAI_API_KEY)

def openai_chat(prompt, model="gpt-4-turbo-preview"):
    response = client_openai.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def deepseek_chat(prompt):
    # Placeholder: Use actual DeepSeek API (assuming similar to OpenAI)
    # Replace with real implementation
    client_deepseek = OpenAI(api_key=DEEPSEEK_API_KEY, base_url="https://api.deepseek.com")  # Hypothetical
    response = client_deepseek.chat.completions.create(
        model="deepseek-chat",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def llama_chat(prompt):
    # Placeholder: Use Hugging Face or Ollama
    # Example with transformers (requires torch)
    from transformers import pipeline
    pipe = pipeline("text-generation", model="meta-llama/Llama-2-7b-chat-hf")  # Needs auth/token
    response = pipe(prompt, max_length=200)[0]['generated_text']
    return response

def ask_llm(prompt, model="openai", **kwargs):
    if model == "openai":
        return openai_chat(prompt, **kwargs)
    elif model == "deepseek":
        return deepseek_chat(prompt, **kwargs)
    elif model == "llama":
        return llama_chat(prompt, **kwargs)
    else:
        raise ValueError("Unsupported LLM model")