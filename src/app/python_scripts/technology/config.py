import os
from dotenv import load_dotenv

load_dotenv()

OPEN_AI_API_KEY = os.getenv("OPEN_AI_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
