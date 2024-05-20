def hello():
    print('hello1')
    print('hello2')
    print('hello3')

# hello()


def numbers(num1):
    result = num1 + 4
    return result

num1 = numbers(3)
num2 = numbers(4)

# print(num1)
# print(num1, num2)

# -------------

# 미션1. 덧셈을 하는 함수 작성
#   숫자 2개를 입력받아, 해당 숫자의 합산 반납

def add(num1, num2):
    sum = num1 + num2
    return sum

# print(add(3, 5))
# print(add(10, 20))

def add2(num1, num2):
    return num1+num2

# print(add2(2,3))

def add3(num1, num2):
    return num1, num2, num1+num2

# print(add3(1,2))

# 미션2. 뺄셈, 곱셈, 나눗셈 함수 만들어보기
#   덧셈처럼 2개의 인자를 입력받아 하나의 결과 반환

def sub(num1, num2):
    if num1 > num2:
        return num1-num2
    else:
        return num2-num1
    
def mul(num1, num2):
    return num1+num2

def div(num1, num2):
    return num1/num2

print(sub(5,3))
print(mul(2,3))
print(div(5,3))

print(sub(5,0))
print(mul(2,0))
print(div(5,0))