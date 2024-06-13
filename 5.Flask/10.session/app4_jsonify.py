from flask import Flask, session, request, jsonify, send_from_directory
from flask import redirect, url_for

app = Flask(__name__)
app.secret_key = 'this-is-another-my-secret'

# 사용자 DB
users = [
    {'name': 'Alice', 'id': 'alice', 'pw': 'alice'},
    {'name': 'Bob', 'id': 'bob', 'pw': 'bob1234'},
    {'name': 'Charlie', 'id': 'charlie', 'pw': 'hello'},
]


@app.route('/')
def home():
    return send_from_directory('static', 'index.html')

@app.route('/profile')
def profile():
    return send_from_directory('static', 'profile.html')

@app.route('/api/login', methods=['POST'])
def api_login():
    # 로그인 처리를 해야함
    # id = request.form.get('id', None)
    # pw = request.form.get('password', None)
    # user = None

    data = request.json
    id = data.get('id')
    pw = data.get('pw')

    # 사용자가 목록에 있는지 검사
    # for u in users:
    #     if id == u.get('id') and pw == u.get('pw'):
    #         user = u
    user = next((u for u in users if u['id'] == id and u['pw'] == pw), None)

    if user:
        session['user'] = user  # 로그인한 사용자의 정보를 세션에 저장
        return jsonify({'status': 'success', 'message': '로그인 성공'})
    else:
        return jsonify({'status': 'error', 'message': '사용자 없음'})


@app.route('/api/profile', methods=['POST'])
def api_profile():
    user = session.get('user')  # 위에서 저장한 내용 다시 받아오기
    message = None

    if request.method == "POST":
        new_pw = request.form.get('new_password', None)
        for u in users:
            if user['id'] == u['id']:
                # 나의 DB 변경
                u['pw'] = new_pw
                user = u
                # message="변경되었습니다"
                return jsonify({'status': 'success', 'message': '비밀번호 변경 성공', 'user': user})
        
        # 나의 세션 변경
        user['pw'] = new_pw
        session['user'] = user

    # return render_template('profile3.html', user=user, message=message)
    return jsonify({'status': 'success', 'user': user})

@app.route('/api/logout')
def api_logout():
    session.pop('user', None)
    return jsonify({'status': 'success', 'message': '로그아웃 성공'})

if __name__ == "__main__":
    app.run(debug=True)