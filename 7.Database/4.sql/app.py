from flask import Flask, render_template, request, session, redirect, url_for
from datetime import timedelta
import sqlite3

app = Flask(__name__)
app.secret_key = 'hello1234'
app.permanent_session_lifetime = timedelta(minutes=5)

# 사용자 DB

DATABASE = 'users.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # 행을 sqlite3.Row 라는 객체 타입으로 반환
                                    # 설정하면 각 Row의 결과가 Dict 유형으로 반환됨
    return conn

def init_db():
    with app.app_context():
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL)
        ''')

        cur.execute("SELECT COUNT(*) AS count FROM users")
        count = cur.fetchone()['count']
        # count = cur.fetchone()[0] # 이건 Row 타입이 아닌 기본값(튜플)로 반납될 때

        if count == 0:
            cur.execute('INSERT INTO users (username, password) VALUES (?, ?)', ('user1', 'password1'))
            cur.execute('INSERT INTO users (username, password) VALUES (?, ?)', ('user2', 'password2'))
            conn.commit()
        
        cur.execute('SELECT * FROM users')
        rows = cur.fetchall()

        print('-' * 30)
        for row in rows:
            print(row['id'], row['username'], row['password'])
        print('-' * 30)

        conn.close()

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
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM users WHERE username = ?', (username,))
        user_data = cur.fetchone()
        conn.close()

        if user_data and user_data['password'] == password:
            session['user'] = username
            session.permanent = True
            print('로그인 성공')
            return redirect(url_for('home'))
        else:
            print('패스워드 틀림')
            # 메세지가 있으면 전달하고 없으면 그냥 재 로그인
            return redirect(url_for('login'))
    else:
        # GET 요청이라 로그인 폼 보여주기
        if "user" in session:
            print('이전에 로그인 했음')
            return redirect(url_for('home'))
    
    # GET 요청 시 로그인 폼 보여주기
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    print('로그아웃')
    return redirect(url_for('login'))

if __name__ == "__main__":
    init_db()
    app.run(debug=True)