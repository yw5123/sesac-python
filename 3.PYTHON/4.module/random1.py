# 미션1. 랜덤숫자 1~100까지를 생성하는 함수를 찾아 출력

import random

print(random.randrange(1, 100))


# 미션2. 주사위 던지는 함수 작성
def roll_dice():
    return random.randint(1, 6)

print(f'주사위를 던집니다: {roll_dice()}')


# 미션3. 리스트에서 랜덤으로 요소 선택
elements = ['apple', 'banana', 'cherry', 'grape', 'pineapple']

def choose_random_element(elements):
    return random.choice(elements)
    # return elements[random.randint(0, len(elements)-1)]

print("선택된 과일은: ", choose_random_element(elements))


# 미션4. 랜덤으로 숫자 리스트 섞기
elements = ['apple', 'banana', 'cherry', 'grape', 'pineapple']
numbers = [1,2,3,4,5] 
def random_list(elements):
    random.shuffle(elements)
    return elements
    # return random.sample(elements, len(elements))

print('섞인 리스트: ', random_list(elements))
print('섞인 리스트: ', random_list(numbers))


charU = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
charL = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

# 미션5. 랜덤 문자열 생성 (영문 대문자 6자리)
def random_upper6():
    # upper_str = ""
    # for i in range(6):
    #     upper_str += random.choice(charU)
    # return upper_str
    return ''.join(random.choices(charU, k=6))

print('랜덤 문자열(영문 대문자 6자리): ', random_upper6())


# 미션6. 랜덤 초이스에서 가중치 고려
# elements = ['apple', 'banana', 'cherry', 'grape', 'pineapple']    # 위에 선언되어 있음
weight1 = [5, 4, 3, 2, 1]

def choose_random_weight(elements):
    return random.choices(elements, weight1)

print("가중치 랜덤: ", choose_random_weight(elements))


# 미션7. 랜덤 비밀번호 생성 (대소문자, 숫자 포함 8자리)
def rand_pwd():
    pwd = ""
    for i in range(8):
        ran_3 = random.randint(1,3)
        if ran_3 == 1:
            pwd += random.choice(charU)
        elif ran_3 == 2:
            pwd += random.choice(charL)
        else:
            pwd += str(random.randint(0,9))
    return pwd

print("랜덤 비밀번호: ", rand_pwd())


# 미션8. 강력한 비밀번호 생성 (대문자, 소문자, 숫자를 각각 최소 1개 이상)
def strong_pwd():
    return

print("강력한 비밀번호: ", strong_pwd())