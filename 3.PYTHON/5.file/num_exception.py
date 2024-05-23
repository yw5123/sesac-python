def div(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "0으로 나눌 수 없습니다."
    except TypeError:
        return "입력값에 숫자가 아닌 값이 입력되었습니다."
    except:
        print("알 수 없는 이유로 나눌 수 없습니다.")
        return "NaN"
    else:
        print("오류가 발생하지 않고 계산을 잘 완료했습니다.")
    finally:
        print("여기는 오류/성공 상관없이 무조건 호출")
    
    return result

print(div(5,3))
print(div(10,0))
print(div(10,'a'))
print(div(15,5))