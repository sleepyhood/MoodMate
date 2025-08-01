from flask import Blueprint, render_template, request

# Blueprint 생성 (Blueprint는 애플리케이션 내에서 여러 URL을 묶는 방법)
main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')


# 사용자 입력 처리 (POST)
@main.route('/submit', methods=['POST'])
def submit_emotion():
    # 폼에서 입력한 값 받기
    user_input = request.form.get('emotion_input').strip()  # 입력값 받기
    if not user_input:  # 빈 값 체크
        return render_template('index.html', error="기분을 입력해주세요.")  # 다시 폼으로 돌아가기

    
    # 여기서 받은 사용자 입력으로 감정 분석 API 연동 등을 할 수 있음
    # 예: sentiment = analyze_sentiment(user_input)

    # 예시: 분석 결과를 화면에 출력
    return f"입력한 기분: {user_input}"

@main.route('/about')
def about():
    return render_template('about.html')
