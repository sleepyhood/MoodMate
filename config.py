
import os
from dotenv import load_dotenv

load_dotenv()  # .env 파일 로드
# 아직 구현중...
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')


# config.py (예시)

# utils/emotion_api.py (예시)
# import openai
# from config import Config

# openai.api_key = Config.OPENAI_API_KEY

# def analyze_sentiment(text):
#     response = openai.Completion.create(
#         engine="text-davinci-003",
#         prompt=f"Analyze the sentiment of this text: {text}",
#         max_tokens=60
#     )
#     sentiment = response.choices[0].text.strip()
#     return sentiment
