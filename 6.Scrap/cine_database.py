import sqlite3

DATABASE = 'cine.db'

def init_db():
    # 테이블 생성 코드 추가
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS cine (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            rank TEXT NOT NULL,
            title TEXT NOT NULL,
            audience TEXT NOT NULL,
            link TEXT
        )
    ''')
    conn.commit()

    return conn, cur


def save_to_db(conn, cur, rank, title, audience, link):
    # 영화를 DB에 삽입
    query = 'INSERT INTO cine (rank, title, audience, link) VALUES (?, ?, ?, ?)'
    cur.execute(query, (rank, title, audience, link))
    conn.commit()

def query_movie(cur):
    # 영화 목록 모두 다 출력
    cur.execute('SELECT rank, title, audience, link FROM cine')
    rows = cur.fetchall()

    for r in rows:
        print(f"순위: {r[0]}, 영화 제목: {r[1]}, 관객수: {r[2]}")


def close_db(conn):
    # DB 연결 종료
    conn.close()