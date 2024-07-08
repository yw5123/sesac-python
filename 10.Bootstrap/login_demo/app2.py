from flask import Flask, render_template, redirect, url_for, request, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'hello1234'

# 사용자 계정 정보 -> 나중에는 DB에서 가져와야함
# users = {'username': 'password'}
DATABASE = 'users.db'

def connect_db():
    return sqlite3.connect(DATABASE)

def init_database():
    db = connect_db()
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL           
        )
        ''')
    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', ('username', 'password'))
    except sqlite3.IntegrityError as e:
        print(f"Error creating user 'username': {e}")
    db.commit()
    cursor.close()
    db.close()

def query_db(query, args=(), isOne=False):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute(query, args)
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return (result[0] if result else None) if isOne else result
    # if isOne == True:
    #     if result is None:
    #         return None
    #     else:
    #         return result[0]
    # else:
    #     if result is None:
    #         return None
    #     else:
    #         return result

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        # if username in users and users[username] == password:
        # 여기서 db에 쿼리
        user = query_db('SELECT * FROM users WHERE username = ? and password = ?', (username, password), isOne=True)

        if user is not None:
            print('사용자 로그인 성공')
            flash('로그인 성공!', 'success')
            return redirect(url_for('dashboard'))
        else:
            print('사용자 로그인 실패')
            flash('로그인 실패, 사용자 이름 또는 비밀번호가 올바르지 않습니다', 'danger')

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == "__main__":
    init_database()
    app.run(debug=True)