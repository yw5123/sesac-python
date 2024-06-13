from flask import Flask, session

app = Flask(__name__)

app.secret_key = 'this-is-my-secret'
# 아무 문자열이나 쓰면 세션 데이터를 저장하는 암호키로 사용됨

@app.route('/')
def index():
    session['username'] = 'user'
    session['data'] = 'data'

    return '헬로우'

@app.route('/set_session/<id>')
def set_session_data(id):
    session['username'] = id
    
    return "데이터가 저장되었음"

@app.route('/get_session')
def get_session_data():
    username = session.get('username', '게스트')
    data = session.get('data', '데이터 없음')

    return f"사용자 이름: {username}, 사용자 데이터: {data}"

if __name__ == "__main__":
    app.run(debug=True)
