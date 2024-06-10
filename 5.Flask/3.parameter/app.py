from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {'name': 'Alice', 'age': 25, 'phone': '123-123-123'},
    {'name': 'Bob', 'age': 30, 'phone': '234-234-234'},
    {'name': 'Charlie', 'age': 35, 'phone': '555-555-555'}
]

@app.route('/')
def home():
    return jsonify(users)

@app.route('/user/<name>')
def search_user(name):
    user = None

    # user = [ u for u in users if u['name'].lower() == name.lower() ]

    for u in users:
        if u['name'].lower() == name.lower():
            user = u
            break
        if str(u['age']) == name:
            user = u
            break

    if user:
        return jsonify(user), 200
    else:
        return jsonify({'error': 'user not found'}), 404
    # 결과가 있을 때는 지금처럼 응답과 200을 보내고
    # 결과가 없을 때는 응답값에 404 보내기


if __name__ == "__main__":
    app.run(debug=True)