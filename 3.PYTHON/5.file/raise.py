def input_age(age):
    if age < 0:
        raise ValueError("음수를 입력할 수 없습니다")
    print(age)
    return age

try:
    input_age(10)
    input_age(15)
    input_age(17)
    input_age(-2)
except ValueError as e:
    print("입력값에 오류가 있습니다: ", e)