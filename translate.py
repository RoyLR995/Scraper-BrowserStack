import requests
import json
from config import RAPIDAPI_KEY, RAPIDAPI_HOST

# Function to translate text using RapidAPI
def translate_text(text, target_lang="en", source_lang="es"):
    url = f"https://{RAPIDAPI_HOST}/t"
    headers = {
        "Content-Type": "application/json",
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": RAPIDAPI_HOST
    }
    payload = {
        "from": source_lang,
        "to": target_lang,
        "q": text
    }
    # Sending POST request with the correct body and headers
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        translated_text = response.json()[0]  # Directly access the list element
        return translated_text
    else:
        print(f"Error translating text: {response.status_code}")
        return text
