from flask import Flask, session, render_template, request
from flask import redirect, url_for

app = Flask(__name__)
app.secret_key = 'this-is-another-my-secret'

# 사용자 DB
users = [
    {'name': 'Alice', 'id': 'alice', 'pw': 'alice'},
    {'name': 'Bob', 'id': 'bob', 'pw': 'bob1234'},
    {'name': 'Charlie', 'id': 'charlie', 'pw': 'hello'},
]

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # 로그인 처리를 해야함
        id = request.form.get('id', None)
        pw = request.form.get('password', None)
        user = None

        # 사용자가 목록에 있는지 검사
        # for u in users:
        #     if id == u.get('id') and pw == u.get('pw'):
        #         user = u
        user = next((u for u in users if u['id'] == id and u['pw'] == pw), None)

        if user:
            session['user'] = user  # 로그인한 사용자의 정보를 세션에 저장
            return redirect(url_for('profile'))
        else:
            return render_template('index.html', error='로그인 실패')

    # get 요청일 때는 페이지를 보내줌
    return render_template('index.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    user = session.get('user')  # 위에서 저장한 내용 다시 받아오기
    message = None

    if request.method == "POST":
        new_pw = request.form.get('new_password', None)
        for u in users:
            if user['id'] == u['id']:
                # 나의 DB 변경
                u['pw'] = new_pw
                user = u
                message="변경되었습니다"
        
        # 나의 세션 변경
        user['pw'] = new_pw
        session['user'] = user

    return render_template('profile3.html', user=user, message=message)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)