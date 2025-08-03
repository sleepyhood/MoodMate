from flask import Flask
from markdown import markdown

# pip install python-dotenv
# run.py에서 넘어온다.


def create_app():
    app = Flask(__name__)
    app.jinja_env.filters["markdown"] = lambda text: markdown(text)

    # 설정 파일 로드 (config.py에서 설정을 가져옴)
    # app.config.from_object('config.Config')

    # 라우팅 등록
    from .routes import main

    app.register_blueprint(main)

    return app
