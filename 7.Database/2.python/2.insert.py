import sqlite3

# DB에 연결
conn = sqlite3.connect('example.db')

# 커서를 통해 데이터 입출력 포인터 가져오기
cur = conn.cursor()

# 테이블에 데이터가 있는지 확인
cur.execute('SELECT COUNT(*) FROM users')
count = cur.fetchone()[0]
print(count)

if count == 0:
    # 커서를 통해 명령어 보내기
    cur.execute('INSERT INTO users (name, age) VALUES ("Alice", 30)')

    cur.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Bob', 25))

    # 커밋
    conn.commit()
else:
    print('데이터가 이미 있습니다.')

# 연결 닫기
conn.close()