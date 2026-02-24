import urllib.request
import json

API_KEY = "AIzaSyDOmOkahMDrC0Rb-PYR7nNsIMyIoOqT39Y"
url = f"https://generativelanguage.googleapis.com/v1beta/models?key={API_KEY}"

try:
    with urllib.request.urlopen(url) as response:
        models = json.load(response)
        for m in models.get('models', []):
            print(f"{m['name']} - Methods: {m['supportedGenerationMethods']}")
except Exception as e:
    print(f"Error: {e}")
