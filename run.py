from app import create_app
from app import api_modules

# 애플리케이션 생성
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
