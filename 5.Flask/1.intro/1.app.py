from flask import Flask

app = Flask(__name__)   # 플라스크명을 파일명으로 선언

@app.route("/")
def home():
    return "<HTML><BODY><H1>나의 헤딩</H1><P>여기는 나의 문장</P></BODY></HTML>"

@app.route("/user/<name>")  # <name> 변수 -> 변수명과 함수 인자를 매칭해서 내부에서 처리
def user(name=None):
    username = name

    return f"""
        <HTML><BODY><H1>사용자 페이지: {username}님 안녕하세요</H1>
        <P>여기는 {username}의 소개</P></BODY></HTML>"""

@app.route("/admin")
def admin():
    return "<HTML><BODY><H1>관리자 페이지</H1><P>여기는 나의 문장</P></BODY></HTML>"

if __name__ == "__main__":
    app.run(debug=True)

