from flask import Flask, render_template, request
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads/'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        return '<h1>파일 저장 완료</h1>'
    else:
        return '<h1>파일 없음</h1>'

if __name__ == "__main__":
    app.run(debug=True)