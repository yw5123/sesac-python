# ORM = SQL 몰라도 그냥 개발언어를 통해 개발
# Object Relational Model = DB에 들어가는 테이블을 Object로 만들어둔 것
# 파이썬에서의 Object는 Class

# 파이썬 대표적인 라이브러리 sqlalchemy
# 플라스크에서 더 편하게 만들어둔 게 flask_sqlalchemy

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///example.db')
# conn = get_db_connection()
# cur = conn.cursor()
# query = ""
# cur.execute(query)
# conn.commit()
# conn.close()

# 테이블의 원형(base)
Base = declarative_base()

# 테이블 설계 (테이블이 가져야 하는 기본 속성을 base로부터 상속)
class User(Base):
    __tablename__ = 'users' # (옵션) 안 할 경우,  클래스명 = 테이블명
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    # hobby = Column(String)    # 추가해서 다시 실행해도 변경되지는 x
# CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER);

# 설계한 내용 실행
Base.metadata.create_all(engine)

# 만들어진 db와 통신해서 데이터 입출력 = 세션 이라고 부름
Session = sessionmaker(bind=engine)
session = Session()
# 이 session을 통해 CRUD 가능


# 사용자 추가
new_user = User(name="Alice", age=30)
session.add(new_user)
session.commit()
# INSERT INTO users (name, age) VALUES ('Alcie', 30);

new_user = User(name="Bob", age=25)
session.add(new_user)
session.commit()


# 사용자 조회
users = session.query(User).all()
for user in users:
    print(user.name, user.age)
# SELECT * FROM users;
# 10줄짜리 코드를 3줄로.. 원래는 conn, cur 등등 