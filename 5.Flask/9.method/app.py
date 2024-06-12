from flask import Flask, render_template, request

app = Flask(__name__)

users = [
    {'name': 'Alice', 'id': 'alice', 'pw': 'alice'},
    {'name': 'Bob', 'id': 'bob', 'pw': 'bob1234'},
    {'name': 'Charlie', 'id': 'charlie', 'pw': 'hello'},
]

@app.route('/', methods=['GET', 'POST'])
def home():
    # id = request.args.get('id') # get 방식의 url 파라미터를 처리할 때만 가능한 방법
    
    if request.method == 'POST':
        id = request.form['id']  # post 방식 중 form-data를 처리할 때 payload를 받아오는 기법
        pw = request.form['password']
    
    # login_success = False
        user = None

    # for u in users:
    #     # 내가 작성한 코드
    #     # if id == u['id']:
    #     #     if pw == u['pw']:
    #     #         login_success = True
    #     #         print('로그인되었습니다')

    #     # 실습 코드
    #     if u['id'] == id and u['pw'] == pw:
    #         print('매치되는 사용자 있음')
    #         user = u

    # 위 5줄짜리 코드를 1줄로, next() 함수와 list comprehensiton으로 작성'
    # next() 함수는 next(iterate 조건문, 기본값) 형태로 구성됨
        user = next((user for user in users if user['id'] == id and user['pw'] == pw), None)

    # if not login_success:
    #     print('로그인 실패')
    
        if user:
            print(f"로그인 한 사용자는 {user['name']}")
            message = None
        else:
            print(f"로그인 가능한 사용자가 없습니다. id = {id}")
            message = '로그인 실패'

        return render_template('index.html', user=user, error=message)

    # 위 내용을 아래 html에 전달
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)