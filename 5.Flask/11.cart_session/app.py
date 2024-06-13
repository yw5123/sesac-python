from flask import Flask, session, render_template, redirect, url_for
from datetime import timedelta

app = Flask(__name__)
app.secret_key = 'abcd1234'
app.permanent_session_lifetime = timedelta(minutes = 5)    # 5분 후에 만료

# 상품 DB
items = {
    'item1': {'name': '상품1', 'price': 1000, 'image': 'item1.jpg'},
    'item2': {'name': '상품2', 'price': 2000, 'image': 'item2.jpg'},
    'item3': {'name': '상품3', 'price': 3000, 'image': 'item3.jpg'},
}

@app.route('/')
def index():
    return render_template('index.html', items=items)

@app.route('/add_to_cart/<item_name>')
def add_to_cart(item_name):
    print(f'상품 담기: {item_name}')
    
    # 상품을 세션안의 cart라는 변수에 담기
    if 'cart' not in session:
        session['cart'] = {}
        session.permanent = True

    # 카트 안에 물건 담기
    if item_name in session['cart']:        # 이전에 담은 적 있는지 확인
        session['cart'][item_name] += 1     # 있으면 개수 1개 증가
    else:
        item_info = items.get(item_name)    # 해당 상품을 DB에서 조회
        if item_info:                       # 상품이 DB에 있으면
            session['cart'][item_name] = 1  # 신규 상품으로 1개 추가

    # 세션 정보 변경된 거 알려주기
    session.modified = True

    return redirect(url_for('index'))

@app.route('/remove_item_from_cart/<item_name>')
def remove_item_from_cart(item_name):
    print(f'상품 지우기: {item_name}')
    # 상품 지우는 코드 작성
    if 'cart' in session and item_name in session['cart']:
        # del session['cart'][item_name]
        session['cart'].pop(item_name)
        session.modified = True

    return redirect(url_for('view_cart'))

@app.route('/clear_cart')
def clear_cart():
    print('카트 지우기')
    #카트 통째로 비우기 - 세션 삭제
    if 'cart' in session:
        session.pop('cart', None)
        session.modified = True
    
    return redirect(url_for('view_cart'))

@app.route('/view_cart')
def view_cart():
    cart_items = {}
    total_price = 0

    # 카트에 담긴 상품의 수량과 가격 조회
    for item_name, quantity in session.get('cart', {}).items(): # 세션 안의 cart 변수의 dict 객체들 가져오기
        item = items.get(item_name) # 첫번째 항목의 아이템을 DB에서 조회
        if item:
            # 프런트에서 표현하기 위한 key, value들 모아서 담고, total_price 합산 가격 구하기
            cart_items[item_name] = {'name': item['name'], 'quantity': quantity, 'price': item['price'], 'image': item['image']}
            total_price += item['price'] * quantity

    # 위에서 정리한 내용 전달
    return render_template('cart.html', cart_items=cart_items, total_price=total_price)

if __name__ == "__main__":
    app.run(debug=True)