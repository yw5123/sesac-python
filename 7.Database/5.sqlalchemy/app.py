from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///example.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

# fask-sqlalchemy 설정
db = SQLAlchemy(app)

# # 모델 불러오기
# from models import User

# DB 모델 정의
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    age = db.Column(db.Integer)


@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/add', methods=['POST'])
def add():
    name = request.form.get('name')
    age = request.form.get('age')

    new_user = User(name=name, age=int(age))
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_user(id):
    user = User.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)


## 실습 코드
# # 초기화
# with app.app_context():
#     db.create_all()

#     # 새로운 사용자 계정 생성
#     new_user = User(name='user1', age=30)
#     db.session.add(new_user)
#     new_user = User(name='user2', age=22)
#     db.session.add(new_user)
#     db.session.commit()

#     #조회
#     users = User.query.all()
#     for user in users:
#         print(user.name, user.age)
#     print('-' * 30)