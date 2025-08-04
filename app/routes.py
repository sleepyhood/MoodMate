from flask import Blueprint, render_template, request
from app import api_modules
from markdown import markdown
import textwrap
import json, re

# Blueprint 생성 (Blueprint는 애플리케이션 내에서 여러 URL을 묶는 방법)
main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("index.html")


# 사용자 입력 처리 (POST)
@main.route("/submit", methods=["POST"])
def submit_emotion():
    # 폼에서 입력한 값 받기
    user_input = request.form.get("emotion_input").strip()  # 입력값 받기
    if not user_input:  # 빈 값 체크
        return render_template(
            "index.html", error="기분을 입력해주세요."
        )  # 다시 폼으로 돌아가기

    gemini_result = api_modules.analyze_sentiment_gemini(user_input)

    # api 아깝다! 일단 임시 데이터로 대체
    # gemini_result = {
    #     "emotion": "부정",
    #     "book": "하마터면 열심히 살 뻔했다",
    #     "music": "숨 (Breath)",
    #     "emotion_detail": "문장은 '너무 우울해', '원망스러워'와 같은 직접적인 부정적 감정 표현을 포함하고 있습니다. 이직을 원하지만 현실적으로 불가능한 상황 에 대한 좌절감, 무력감, 그리고 그 현실에 대한 원망이 복합적으로 나타나 전반적으로 매우 부정적인 감정 상태임을 알 수 있습니다.",
    #     "book_detail": "현재 느끼는 우울함과 현실에 대한 원망은 '열심히 살아야 한다'는 사회적 압박감에서 비롯될 수 있습니다. 이 책은 '열심히 살지 않아도 괜찮다'는 역설적인 메시지를 통해 삶의 속도를 늦추고, 자신의 진정한 행복을 찾아가는 과정을 유쾌하면서도 통찰력 있게 제시합니다. 이직이라는 목표에 갇혀 자 신을 원망하기보다, 잠시 멈춰 서서 삶의 방향과 진정한 가치에 대해 재고해볼 기회를 제공하여 답답함과 무력감을 덜어주고 새로운 시각을 얻는 데 도움을 줄 것입니다.",
    #     "music_detail": "박효신의 '숨'은 지치고 힘든 마음을 위로하는 대표적인 곡입니다. '괜찮아 질 거야'라는 직접적인 위로 대신, 그저 '숨 쉬는 것만으로도 충 분하다'는 메시지로 듣는 이에게 깊은 공감과 편안함을 선사합니다. 현재 이직 문제로 인한 좌절감과 우울감 속에서 자신을 다그치기보다, 잠시 멈춰 서서 스스로에게 숨 돌릴 여유를 주고 감정을 보듬어 주는 시간을 가질 수 있도록 도울 것입니다.",
    # }

    # print(gemini_result)
    # print(type(gemini_result))

    recommended_book_title = gemini_result.get("book")
    # Kakao API로 책 정보 검색
    book_info = api_modules.search_book_by_title(recommended_book_title)

    return render_template(
        "index.html",
        sentiment=gemini_result,
        user_input=user_input,
        book_info=book_info,
    )


@main.route("/about")
def about():
    return render_template("about.html")
