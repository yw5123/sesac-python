from flask import Flask, render_template, request, session, redirect, url_for, flash
from datetime import timedelta
import database as db

app = Flask(__name__)
app.secret_key = 'hello1234'
app.permanent_session_lifetime = timedelta(minutes=5)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # 로그인 처리 구현
        username = request.form['username']
        password = request.form['password']

        # 사용자 데이터를 외부 db에서 가져오기
        query = "SELECT * FROM users WHERE username = ? AND password = ?"
        user_data = db.get_query(query, (username, password))
        print(f"조회된 사용자: ", user_data)

        ## 함수로 분리함 (database.py)
        # conn = db.get_db_connection()
        # cur = conn.cursor()
        # cur.execute('SELECT * FROM users WHERE username = ?', (username,))
        # user_data = cur.fetchone()
        # conn.close()

        # if user_data and user_data['password'] == password:
        if len(user_data) == 1:
            session['user'] = user_data[0]['username']
            if "email" in user_data[0]:
                session['email'] = user_data[0]['email']
            session.permanent = True
            print('로그인 성공')
            flash('로그인에 성공하였습니다')
            return redirect(url_for('home'))
        else:
            print('패스워드 틀림')
            flash('아이디/패스워드가 일치하지 않습니다')
            # 메세지가 있으면 전달하고 없으면 그냥 재 로그인
            return redirect(url_for('login'))
    else:
        # GET 요청이라 로그인 폼 보여주기
        if "user" in session:
            print('이전에 로그인 했음')
            return redirect(url_for('home'))
    
    # GET 요청 시 로그인 폼 보여주기
    return render_template('login.html')


@app.route('/user', methods=['GET', 'POST'])
def user():
    if "user" in session:
        username = session['user']
        email = session.get('email', None)

        if request.method == 'POST':
            # action = request.form["action"]
            # if action == "submit":
            #     email = request.form["email"]

            new_email = request.form.get('email', None)
            session['email'] = new_email
            new_password = request.form.get('password', None)
            if new_email:
                query = "UPDATE users SET email = ? WHERE username = ?"
                db.execute_query(query, (new_email, username))
                email = new_email

            if new_password:
                query = "UPDATE users SET password = ? WHERE username = ?"
                db.execute_query(query, (new_password, username))

            print('사용자 정보 업데이트')
            flash('사용자 정보가 업데이트되었습니다')

            # if not new_email and not new_password:
            #     query = "DELETE FROM users WHERE username = ?"
            #     db.execute_query(query, (username,))
            #     print('계정 삭제')
            #     flash('계정이 삭제되었습니다')
            #     return redirect(url_for('logout'))

        return render_template('user.html', email=email)
    
@app.route('/view')
def view():
    # users = []  # 미션1. DB 쿼리해서 모든 사용자 목록 받아오기

    # 사용자 데이터를 외부 db에서 가져오기
    query = "SELECT username, password, email FROM users"
    users = db.get_query(query)
    
    return render_template('view.html', users=users)

@app.route('/logout')
def logout():
    session.pop('user', None)
    session.pop('email', None)
    print('로그아웃')
    flash('로그아웃에 성공하였습니다')
    return redirect(url_for('login'))

@app.route('/join', methods=['GET', 'POST'])
def join():
    if request.method == 'POST':
        # 입력값 받아오기
        username = request.form['username']
        password = request.form['password']

        query = "INSERT INTO users (username, password) VALUES (?, ?)"
        db.execute_query(query, (username, password))
        print('회원가입 완료')
        flash('회원가입이 완료되었습니다')
        return redirect(url_for('home'))
        
    # GET 요청 시 회원가입 폼 보여주기
    return render_template('join.html')

if __name__ == "__main__":
    db.init_db()
    app.run(debug=True)