from flask import Flask, jsonify, request
from database import get_stores, get_store_by_name

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/api/stores')
def api_stores():
    name = request.args.get('name')
    if name:
        stores = get_store_by_name(name)
    else:
        stores = get_stores()
    
    return jsonify(stores)



if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)