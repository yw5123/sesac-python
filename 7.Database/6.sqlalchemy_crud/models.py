from flask_sqlalchemy import SQLAlchemy


# Flask - SQLAlchemy 를 연결..할 건데 app을 못 가져오니(서로 참조..) 일단 비워둠
db = SQLAlchemy()

# 클래스를 통해 DB 테이블 설계/설정
class User(db.Model):
    __tablename__ = "users" # 옵셔널.. 테이블명과 클래스명 다를 때 설정
    id = db.Column(db.Integer, primary_key=True)    # PRIMARY KEY
    name = db.Column(db.String, nullable=False)     # VARCHAR(20), NOT NULL
    age = db.Column(db.Integer, nullable=True)

    def __repr__(self): # 나의 객체를 누군가 print할 때 표현해주고 싶은 함수 구현
        return f'<사용자: {self.id}, {self.name}, {self.age}>'