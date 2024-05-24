# 미션1. 계산기 코드 작성하기
# 1. 연산자 및 두개의 숫자 입력받아 결과 출력
# 2. 무한반복

# class OperError(Exception):
#     pass

# class NumError(Exception):
#     pass

class InputError(Exception):
    pass

def insert_value():
    oper_lst = ['+', '-', '*', '/']
    try:
        num1 = float(input("첫번째 숫자를 입력하세요: "))
    except ValueError:
        raise InputError("숫자를 입력해주세요.")
    
    oper = input("연산자(+,-,*,/)를 입력하세요: ")
    if oper not in oper_lst:
        raise InputError("연산자를 입력해주세요.")
    
    try:
        num2 = float(input("두번째 숫자를 입력하세요: "))
    except ValueError:
        raise InputError("숫자를 입력해주세요.")

    return num1, oper, num2
    # num1 = int(input("첫번째 숫자를 입력하세요: "))
    # if num1.isdigit() is False:
    #     raise NumError("숫자를 입력해주세요.")
    # oper = input("연산자(+,-,*,/)를 입력하세요: ")
    # if oper not in ('+','-','*','/'):
    #     raise OperError("연산자를 입력해주세요.")
    # num2 = input("두번째 숫자를 입력하세요: ")
    # if num2.isdigit() is False:
    #     raise NumError("숫자를 입력해주세요.")
    # return int(num1), oper, int(num2)

def calc():
    # err_str = "계산에 실패했습니다."
    try:
        num1, oper, num2 = insert_value()
    # except OperError as e:
    #     print(" ※입력 오류: ", e)
    #     return err_str
    # except NumError as e:
    #     print(" ※입력 오류: ", e)
    #     return err_str
    except InputError as e:
        print(" >> 입력 오류: ",e)
    # except TypeError:
    #     return err_str
    else:
        if oper == '+':
            result = num1 + num2
        elif oper == '-':
            result = num1 - num2
        elif oper == '*':
            result = num1 * num2
        elif oper == '/':
            try:
                result = num1 / num2
            except ZeroDivisionError:
                print(" >> 계산 오류: 0으로 나눌 수 없습니다.")
                return
        return result

while(True):
    print(" >> 연산 결과: ", calc(), end="\n\n")
