from flask import Blueprint, render_template

# app = Flask(__name__) 을 대체해주는 코드 작성
admin_app = Blueprint('admin', __name__)

@admin_app.route("/")
def home():
    return render_template('product/index.html')