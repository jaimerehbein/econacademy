import urllib.request
import json

API_KEY = "AIzaSyDOmOkahMDrC0Rb-PYR7nNsIMyIoOqT39Y"
url = f"https://generativelanguage.googleapis.com/v1beta/models?key={API_KEY}"

try:
    with urllib.request.urlopen(url) as response:
        models_data = json.loads(response.read().decode())
        for model in models_data.get('models', []):
            name = model.get('name', 'Unknown')
            methods = model.get('supportedGenerationMethods', [])
            print(f"{name} | {methods}")
except Exception as e:
    print(f"Error: {e}")
