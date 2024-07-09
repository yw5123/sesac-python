from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    data = {
        'labels': ['2023-01', '2023-02', '2023-03', '2023-04', '2023-05', '2023-06'],
        'revenues': [797500, 401500, 665500, 660000, 566500, 709500]
    }

    return render_template('index_ssr.html', revenue=data)


if __name__ == "__main__":
    app.run(debug=True)