class CustomError(Exception):
    # 속성
    # 메소드 넣을 수 있음
    pass

def check_value(value):
    if value < 0 or value >= 100:
        raise CustomError("입력값은 0보다 작거나 100보다 클 수 없습니다")
    return value

try:
    result = check_value(50)
    result = check_value(20)
    result = check_value(100)
except CustomError as e:
    print(e)

print(result)

