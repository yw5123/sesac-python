from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, User
import os

app = Flask(__name__)
app.secret_key = 'sesacsesac'

DATABASE_NAME = 'example.db'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DATABASE_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 해당 모듈을 불러온 이후 초기화 함수를 통해 db - flask 연결
db.init_app(app)

@app.route('/')
def index():
    users = User.query.all()
    # print(users)
    return render_template('index.html', users=users)

@app.route('/add_user', methods=['post'])
def add_user():
    # GET 방식일 때는 URL 파라미터를 통해 정보가 전달되고 args 안에 담겨서 온다.
    # name = request.args.get('name')
    # age = request.args.get('age')
    # POST 방식일 때는 BODY 안에 데이터가 담겨서 온다. 그 body 중 우리가 보낸 건 FORM 타입.
    name = request.form.get('name')
    age = request.form.get('age')

    print(f'입력값은 {name}, {age} 입니다')

    if int(age) < 0:
        flash('나이는 음수일 수 없습니다')
        return redirect(url_for('index'))
    
    if int(age) > 100:
        flash('나이는 100살보다 클 수 없습니다')
        return redirect(url_for('index'))
        

    new_user = User(name=name, age=int(age))
    db.session.add(new_user)
    db.session.commit()
    flash(f'사용자 {name}({age} 세)가 추가되었습니다')

    # return f"<H1>사용자 {name}가 추가되었습니다</H1>"
    return redirect(url_for('index'))

@app.route('/update_user/<id>', methods=['POST'])
def update_user(id):
    user = db.session.get(User, id)

    name = request.form.get('name')
    age = request.form.get('age')

    user.name = name
    user.age = int(age)

    if not name or not age:
        flash('이름과 나이는 빈칸일 수 없습니다')
        return redirect(url_for('edit_user', id=id))


    db.session.commit()

    flash(f'사용자 {user.name}의 정보를 업데이트하였습니다')

    return redirect(url_for('index'))


@app.route('/edit_user/<id>')
def edit_user(id):
    print(f"수정할 사용자 아이디는 {id}")

    # 수정할 사용자 정보 가져와서 어떻게 바꿀지 물어보기
    user = db.session.get(User, id)

    # if not user:  # 클릭으로는 user 없이 넘어갈 수 없어서 지금은 필요하지 않은 코드
    #     flash('선택한 사용자가 없습니다.')
    #     return redirect(url_for('index'))
    
    return render_template('user_edit.html', user=user)

@app.route('/delete_user/<id>')
def delete_user(id):
    print(f"삭제할 사용자 아이디는: {id}")

    # 삭제하는 코드 구현
    user = db.session.get(User, id)
    if user:
        db.session.delete(user)
        db.session.commit()
        print(f'사용자 {user.name}가 삭제되었습니다')
    else:
        print('사용자가 없습니다')

    # return f"<H1>사용자 삭제함</H1>"
    return redirect(url_for('index'))

if __name__ == "__main__":
    with app.app_context(): # 우리의 app, 즉 플라스크 앱이 초기화 된 상태에서..
        # instance 폴더 안에 example.db가 없으면 만들고 싶음
        db_path = os.path.join(app.instance_path, DATABASE_NAME)
        if not os.path.exists(db_path):
            db.create_all()
            print('DB가 없어서 만들었음')

        # 초기화할 때 사용자 데이터도 추가
        if not User.query.first():
            # 없으면 추가
            print('사용자가 없어서 새로 추가')
            user1 = User(name='user1', age=30)
            user2 = User(name='user2', age=33)
            user3 = User(name='user3', age=35)

            db.session.add(user1)
            db.session.add(user2)
            db.session.add(user3)
            db.session.commit()
            # 여기서 세션은 sqlalchemy 원작자가 db와 통신하는 방식을 session이라고 이름 지은 것.. db.connect 라고 하는 게 더 좋앗을텐데....

    app.run(debug=True)