from google import genai
import re, json
import requests
from dotenv import load_dotenv
import os

# pip install -q -U google-genai
# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

load_dotenv()
KAKAO_API_KEY = os.getenv("KAKAO_API_KEY")


def search_book_by_title(title):
    url = "https://dapi.kakao.com/v3/search/book"
    headers = {"Authorization": f"KakaoAK {KAKAO_API_KEY}"}
    params = {"query": title, "target": "title", "size": 1}  # 가장 상위 결과 1개만

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        result = response.json()
        if result.get("documents"):
            book = result["documents"][0]
            return {
                "title": book["title"],
                "authors": book["authors"],
                "thumbnail": book["thumbnail"],
                "contents": book["contents"],
                "url": book["url"],
            }
    else:
        print("📛 카카오 API 요청 실패:", response.status_code)

    return None  # 실패 시


def extract_json_from_text(text):
    match = re.search(r"\{[\s\S]*?\}", text)
    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            print("❌ JSON 파싱 실패:\n", match.group())
            return {}
    else:
        print("❗ JSON 블록을 찾을 수 없습니다.")
        return {}


def analyze_sentiment_gemini(user_input):

    prompt = f"""
    당신은 감정 분석 및 콘텐츠 추천 전문가입니다.
    다음 문장을 읽고 감정을 분석한 뒤, 어울리는 책과 음악을 추천해주세요.

    문장:
    \"\"\"{user_input}\"\"\"

    다음과 같은 **JSON 형식**으로만 응답하세요 (추가 텍스트 없이):

    ```json
    {{
    "emotion": "긍정 | 부정 | 중립 중 하나",
    "book": "추천 도서 제목",
    "music": "추천 음악 제목",
    "emotion_detail": "감정 분석 상세 설명",
    "book_detail": "도서 추천 이유",
    "music_detail": "음악 추천 이유"
    }}
    """

    response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
    print(response.text)

    return extract_json_from_text(response.text)
