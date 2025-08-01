# config.py (예시)
class Config:
    SECRET_KEY = 'your_secret_key'
    OPENAI_API_KEY = 'your_openai_api_key'
    KAKAO_BOOK_API_KEY = 'your_kakao_api_key'
    YOUTUBE_API_KEY = 'your_youtube_api_key'

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
