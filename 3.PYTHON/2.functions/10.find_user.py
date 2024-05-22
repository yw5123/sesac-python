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

def find_user2(name, age):
    # 입력받은 사용자 정보를 출력하시오
    fuser = []
    for u in users:
        if u['name'].lower() == name.lower() and u['age'] == age:
            fuser.append(u)
    return fuser

def find_user3(name=None, age=None):    # 미션 - 내가 작성한 코드
    if str(type(name)) == "<class 'int'>":
        age = name
        name = None

    fuser = []
    if name is None and age is None:
        fuser = list(users)
    elif age is None:
        for u in users:
            if u['name'].lower() == name.lower():
                fuser.append(u)
    elif name is None:
        for u in users:
            if u['age'] == age:
                fuser.append(u)
    else:
        for u in users:
            if u['name'].lower() == name.lower() and u['age'] == age:
                fuser.append(u)
    return fuser

def find_user4(name=None, age=None):
    found_user = []

    if name is None and age is None:
        return users

    for u in users:
        if name is not None and age is not None:
            if u["name"].lower() == name.lower() and \
               u["age"] == age:
                found_user.append(u)
        elif name is not None:
            if u["name"].lower() == name.lower():
                found_user.append(u)
        elif age is not None:
            if u["age"] == age:
                found_user.append(u)
    return found_user

def display_user(users):
    print("\t--- 찾은 사용자 목록 ---")
    for u in users:
        print(f'이름: {u["name"]} \t 나이: {u["age"]} \t 사는 곳: {u["location"]}')


# found = find_user("alice")
# print(f'이름으로 찾은 사용자: {found}')

# found2 = find_user2("alice", 25)
# print(f'이름과 나이로 찾은 사용자: {found2}')

# found3 = find_user3()
# print(f'입력 값 없을 때 결과: {found3}')
# found3 = find_user3('Alice')
# print(f'이름만 넣었을 때 결과: {found3}')
# found3 = find_user3(25)
# print(f'나이만 넣었을 때 결과: {found3}')
# found3 = find_user3('Alice', 25)
# print(f'이름과 나이를 넣었을 때 결과: {found3}')

# found4 = find_user4()
# print(f'입력 값 없을 때 결과: {found4}')
# found4 = find_user4('Alice')
# print(f'이름만 넣었을 때 결과: {found4}')
# found4 = find_user4(age=25)
# print(f'나이만 넣었을 때 결과: {found4}')
# found4 = find_user4('Alice', 25)
# print(f'이름과 나이를 넣었을 때 결과: {found4}')

# found3 = find_user3(25)
# display_user(found3)

def find_user5(search):
    result = []
    
    for u in users:
        if (search.get('age') is None or u.get('age') == search.get('age')) and \
           (search.get('name') is None or u.get('name') == search.get('name')) and \
           (search.get('location') is None or u.get('location') == search.get('location')) and \
           (search.get('car') is None or u.get('car') == search.get('car')):
            if search.get('min_age') is None or int(u.get('age')) >= int(search.get('min_age')):
                result.append(u)

    # nval, aval, lval, cval = False

    # if search["name"] is not None:
    #     nval = True
    # if search["age"] is not None:
    #     aval = True
    # if search["local"] is not None:
    #     lval = True
    # if search["car"] is not None:
    #     cval = True

    # if nval and aval and lval and cval:
    #     for u in users:
    #         if u['name']==search['name'] and u['age']==search['age'] and \
    #            u['local']==search['local'] and u['car']==search['car']:
    #             result.append(u)
    # elif 
        
    return result

search_criteria1 = {"name": "Bob"}
search_criteria2 = {"name": "Alice", "age": 40}
# search_criteria2 = {"name": "Alice"}
search_criteria3 = {"location": "Jeju", "car": "BMW"}
search_criteria4 = {"location": "Jeju", "car": "KS"}
search_criteria2 = {"name": "Alice", "min_age": 20}
search_criteria2 = {"name": "Alice", "min_age": 30}
search_criteria2 = {"name": "Alice", "min_age": 50}

# print(find_user5(search_criteria2))

def find_user6(search):
    result = []

    for u in users:
        if match_criteria(u, search):
            result.append(u)

    return result

def match_criteria(user, criteria):
    for key, value in criteria.items():
        if key == "age":
            if(user["age"]) != value:
                return False
        if key == "name":
            if(user["name"]) != value:
                return False
        if key == "location":
            if(user["location"]) != value:
                return False
        if key == "car":
            if(user["car"]) != value:
                return False
    return True

print(find_user6(search_criteria4))