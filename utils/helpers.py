# utils/helpers.py
import requests
import json

def fetch_api(url, params=None, headers=None):
    """Helper to make API calls (e.g., CrossRef, Semantic Scholar)."""
    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"API fetch error: {e}")
        return None

def save_to_json(data, filename):
    """Save data to JSON for local storage."""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)