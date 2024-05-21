users = [
    {"name": "Alice", "age": 25, "location": "Seoul", "car": "BMW"},
    {"name": "Bob", "age": 30, "location": "Busan", "car": "Mercedes"},
    {"name": "Charlie", "age": 35, "location": "Daegu", "car": "Audi"},
    {"name": "Alice", "age": 40, "location": "Jeju", "car": "KS"},
]

def find_user(name):
    # 입력받은 사용자 정보를 출력하시오
    fuser = []
    for u in users:
        if u['name'].lower() == name.lower():
            fuser.append(u)
            # print(u)
            # return u
    # print('찾는 사용자가 없습니다')
    return fuser

found = find_user("alice")
print(f'찾은 사용자: {found}')

# find_user("alice")
# find_user("ALICE")
