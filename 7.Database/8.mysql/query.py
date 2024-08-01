import pymysql

host = "192.168.56.101"
user = "sesac"
password = "sesac1234"
database = "sesac"

connection = pymysql.connect(host=host, user=user, password=password, database=database)

cursor = connection.cursor()
cursor.execute("SELECT * FROM user")
results = cursor.fetchall()

for res in results:
    print(res)
