from flask import Flask, render_template
import csv

app = Flask(__name__)

csv_data = []

def load_csv_data(filename):
    with open(filename, newline="", encoding="utf-8") as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            csv_data.append(row)


@app.route('/')
@app.route('/<int:page>')
def index(page=1):
    per_page = 10   # 한 페이지에 보여줄 항목 수

    totalpages = (len(csv_data) - 1) // 10 if (len(csv_data) - 1) % 10 == 0 else (len(csv_data) - 1) // 10 + 1
    if page > totalpages:
        page = totalpages

    header = csv_data[0]

    start_index = (page - 1) * per_page + 1
    end_index = page * per_page + 1
    users = csv_data[start_index:end_index]

    return render_template("index.html", users=users, page=page, totalpages=totalpages, header=header)



if __name__ == "__main__":
    load_csv_data('./user.csv')
    app.run(debug=True)

# 1. 이 파일에 flask 기본 툴 추가
# 2. /에 접속 시 이 사용자의 데이터를 보여준다