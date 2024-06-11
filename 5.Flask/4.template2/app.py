from flask import Flask, render_template
from flask import request

app = Flask(__name__)

users = [
    {'name': 'Alice', 'age': 25, 'phone': '123-123-1234'},
    {'name': 'Alice', 'age': 35, 'phone': '321-321-4321'},
    {'name': 'Bob', 'age': 30, 'phone': '234-234-2345'},
    {'name': 'Charlie', 'age': 35, 'phone': '555-555-5555'}
]

@app.route('/')
def main():
    return render_template("index.html", users=users)

@app.route('/user')
def user():
    search_name = request.args.get('name')
    search_age = request.args.get('age')
    search_phone = request.args.get('phone')
    user = users

    if search_name:
        user = [u for u in user if search_name.lower() in u['name'].lower()]

    if search_age:
        user = [u for u in user if int(search_age) == u['age']]
        # type이 number라 어차피 정수만 입력됨
        # try:
        #     search_age = int(search_age)
        #     user = [u for u in user if search_age == u['age']]
        # except ValueError:
        #     pass
    
    if search_phone:
        user = [u for u in user if search_phone == u['phone'][-4:]]

    return render_template("index.html", users=user)


if __name__ == "__main__":
    app.run(debug=True)

