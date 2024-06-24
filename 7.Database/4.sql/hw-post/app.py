from flask import Flask, render_template, request, session
from flask import redirect, url_for, flash
from datetime import timedelta

import database as db

app = Flask(__name__)
app.secret_key = 'hello1234'
app.permanent_session_lifetime = timedelta(minutes=5)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/join', methods=['GET', 'POST'])
def join():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        try:
            query = "INSERT INTO users (username, password) VALUES (?, ?)"
            db.execute_query(query, (username, password))
            print('회원가입 완료')
            flash('회원가입이 완료되었습니다.')
            return redirect(url_for('home'))
        except:
            flash('이미 존재하는 username입니다.')
            return redirect(url_for('join'))

    return render_template('join.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        query = "SELECT * FROM users WHERE username = ?"
        user_data = db.get_query(query, (username,))

        if (len(user_data) == 1):
            if (password == user_data[0]['password']):
                session['user'] = user_data[0]['username']
                if user_data[0]['email']:
                    session['email'] = user_data[0]['email']
                session.permanent = True
                print('로그인 성공')
                flash('로그인되었습니다.')
                
                return redirect(url_for('home'))
            else:
                print('패스워드 틀림')
                flash('아이디와 패스워드가 일치하지 않습니다.')

                return redirect(url_for('login'))
        print('아이디 없음')
        flash('아이디가 존재하지 않습니다.')

        return redirect(url_for('login'))
    else:
        if "user" in session:
            print('이전에 로그인했음')
            return redirect(url_for('home'))
        
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('user', None)
    session.pop('email', None)
    print('로그아웃')
    flash('로그아웃되었습니다.')
    
    return redirect(url_for('home'))


@app.route('/userlist')
def userlist():
    query = "SELECT username, password, email FROM users"
    users = db.get_query(query)

    return render_template('userlist.html', users=users)


@app.route('/user', methods=['GET', 'POST'])
def userpage():
    if "user" in session:
        username = session['user']
        email = session.get('email', None)

        if request.method == 'POST':
            action = request.form['action']

            if action == 'submit':
                email = request.form.get('email', None)
                password = request.form.get('password', None)

                if email:
                    try:
                        query = "UPDATE users SET email = ? WHERE username = ?"
                        db.execute_query(query, (email, username))
                    except:
                        flash('이미 등록된 이메일입니다.')

                        return redirect(url_for('user'))
                    session['email'] = email
                    print('이메일 업데이트됨')

                if password:
                    query = "UPDATE users SET password = ? WHERE username = ?"
                    db.execute_query(query, (password, username))
                    print('비밀번호 업데이트됨')

                if email or password:
                    flash('사용자 정보가 업데이트되었습니다.')
            elif action == 'delete':
                query = "DELETE FROM users WHERE username = ?"
                db.execute_query(query, (username,))
                print('계정 삭제')
                flash('계정이 삭제되었습니다.')

                return redirect(url_for('logout'))

        query = '''SELECT p.id AS id, p.title AS title 
                FROM posts p INNER JOIN users u
                ON p.user_id = u.id  WHERE u.username = ?'''
        my_post_list = db.get_query(query, (username,))

        return render_template('userpage.html', myposts=my_post_list)
    else:
        flash('로그인이 필요합니다.')
        return redirect(url_for('home'))


@app.route('/post', methods=['GET', 'POST'])
def postlist():
    if request.method == 'POST':
        if 'user' in session:
            return redirect(url_for('edit_post'))
    query = '''SELECT p.id AS id, p.title AS title, u.username AS username 
            FROM posts p INNER JOIN users u ON p.user_id = u.id'''
    post_list = db.get_query(query)

    return render_template('postlist.html', posts=post_list)


@app.route('/post/<int:post_id>', methods=['GET', 'POST'])
def post(post_id, prev=None):
    if request.method == 'POST':
        action = request.form.get('action', None)
        if action == "Delete Post":
            query = "DELETE FROM posts WHERE id = ?"
            db.execute_query(query, (post_id,))
            print('게시글 삭제')
            flash('게시글이 삭제되었습니다.')
            if prev == 'my':
                return redirect(url_for('userpage'))
            return redirect(url_for('postlist'))
        
        if action == "Edit Post":
            return redirect(url_for('edit_post', post_id=post_id, prev=prev))
    
    query = '''SELECT p.id AS id, p.title AS title, p.content AS content, u.username AS username
            FROM posts p INNER JOIN users u ON p.user_id = u.id WHERE p.id = ?'''
    post_content = db.get_query(query, (post_id,))[0]

    return render_template('post.html', post=post_content)


@app.route('/posteditor', methods=['GET', 'POST'])
@app.route('/posteditor/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id=None, prev=None):
    if 'user' in session:
        if post_id:
            query = '''SELECT p.id AS id, p.title AS title, p.content AS content, u.username AS username
            FROM posts p INNER JOIN users u ON p.user_id = u.id WHERE p.id = ?'''
            post_content = db.get_query(query, (post_id,))[0]
        else:
            post_content = None

        if request.method == 'POST':
            username = session['user']
            action = request.form.get('action', None)
            title = request.form['title']
            content = request.form['content']

            query = "SELECT id FROM users WHERE username = ?"
            user_id = db.get_query(query, (username,))[0]['id']

            if action == 'Write':
                query = "INSERT INTO posts (title, content, user_id) VALUES (?, ?, ?)"
                db.execute_query(query, (title, content, user_id))

            if action == 'Edit':
                query = "UPDATE posts SET title = ?, content = ? WHERE id = ?"
                db.execute_query(query, (title, content, post_id))

            print('게시글 작성')
            if prev == 'my':
                return redirect(url_for('userpage'))
            return redirect(url_for('postlist'))
                
        return render_template('editpost.html', post=post_content)
    else:
        flash('로그인이 필요합니다.')
        return redirect(url_for('home'))


if __name__ == "__main__":
    db.init_db()
    app.run(debug=True)