import requests
import os
from dotenv import load_dotenv

def get_lighthouse_score(url):
    load_dotenv()
    API_KEY = os.getenv('LIGHTHOUSE_API_KEY')
    params = {
        "url": url,
        "key": API_KEY,
        "category": ["performance", "seo", "accessibility", "best-practices"]
    }

    response = requests.get("https://www.googleapis.com/pagespeedonline/v5/runPagespeed", params=params)

    data = response.json()
    categories = data["lighthouseResult"]["categories"]

    for key, value in categories.items():
        print(f"{key.title()} Score: {round(value['score'] * 100)} / 100")
