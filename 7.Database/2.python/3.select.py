import sqlite3

conn = sqlite3.connect('example.db')
cur = conn.cursor()

# 데이터 조회
cur.execute('SELECT * FROM users')

# 데이터 가져오기
rows = cur.fetchall()
# print(rows)

# 결과 포멧팅
for row in rows:
    print(row)

# 연결 닫기
conn.close()