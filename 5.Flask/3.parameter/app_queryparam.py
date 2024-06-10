from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

users = [
    {'name': 'Alice', 'age': 25, 'phone': '123-123-1234'},
    {'name': 'Alice', 'age': 30, 'phone': '123-321-4321'},
    {'name': 'Bob', 'age': 30, 'phone': '234-234-2345'},
    {'name': 'Charlie', 'age': 35, 'phone': '555-555-5555'}
]

@app.route('/')
def home():
    return jsonify(users)

@app.route('/search')
def search():
    # query = request.args.get('q')       # /search?q=python
    # page = request.args.get('page', default=1, type=int)     # /search?page=2
    # return f"검색 중: {query} on 페이지 {page}..", 200
    name_query = request.args.get('name')
    age_query = request.args.get('age')
    phone_query = request.args.get('phone')
    # result = None
    result = users
    
    # 미션1. 위에 있는 users에서 query 구문이 name인 사람 찾아서 출력
    # 미션2. 나이도 검색
    # 미션3. 전화번호 끝자리로 검색

    # for u in users:
    #     if u['name'].lower() == name_query.lower():
    #         return u      
    #     if str(u['age']) == age_query:
    #         return u
    #     if str(u['phone'][-4:]) == phone_query:
    #         return u
    # return jsonify({'error': 'user not found'}), 404
    # --> 이름만 일치하면 다른 값이 틀려도 출력됨...(!!)


    # --------------------


    # 내가 작성해본 코드
    # if name_query:
    #     n_user = [u for u in users if name_query.lower() in u['name'].lower()]
    # else:
    #     n_user = users

    # if age_query:
    #     a_user = [u for u in n_user if age_query == str(u['age'])]
    # else:
    #     a_user = n_user
    
    # if phone_query:
    #     result = [u for u in a_user if phone_query == str(u['phone'][-4:])]
    # else:
    #     result = a_user

    # --------------------

    # 강사님 코드 바탕으로 다시 작성한 코드
    if name_query:
        result = [u for u in users if name_query.lower() in u['name'].lower()]
    
    if age_query:
        try:
            age_query = int(age_query)
            result = [u for u in result if age_query == u['age']]
        except ValueError:
            return jsonify({'error': 'Age parameter must be an integer'}), 400

    if phone_query:
        try:
            phone_query = int(phone_query)
            result = [u for u in result if phone_query == int(u['phone'][-4:])]
        except ValueError:
            return jsonify({'error': 'Phone parameter must be an integer'}), 400

    if result:
        return jsonify(result)
    else:
        return jsonify({'error': 'user not found'}), 404


if __name__ == "__main__":
    app.run(debug=True)