import sqlite3

this_is_my_db = 'example.db'

# DB 연결 함수 만들기
def connect_db():
    return sqlite3.connect(this_is_my_db)


# 테이블 생성 함수 만들기
def create_table():
    # DB 생성&연결
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    age INTEGER NOT NULL
                )
                ''')
    conn.commit()
    conn.close()


# 데이터 삽입 함수 만들기
def insert_user(name, age):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))
    # prepared-statement 시큐어코딩 기법 중 하나
    
    conn.commit()
    conn.close()


# 데이터 조회 함수 만들기
def fetch_users():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users')
    rows = cur.fetchall()
    conn.close()
    return rows


# 데이터 업데이트 함수 만들기
def update_user(name, new_age):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('UPDATE users SET age = ? WHERE name = ?', (new_age, name))
    conn.commit()
    conn.close()


# 데이터 삭제 함수 만들기
def delete_user(name):
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('DELETE FROM users WHERE name = ?', (name,))
    conn.commit()
    conn.close()