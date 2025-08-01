from flask import Blueprint, render_template

# Blueprint 생성 (Blueprint는 애플리케이션 내에서 여러 URL을 묶는 방법)
main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/about')
def about():
    return render_template('about.html')
