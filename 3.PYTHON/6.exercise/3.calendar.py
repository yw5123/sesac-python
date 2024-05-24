# 미션3. 달력 만들기 (텍스트로 년/월 입력받아 출력)

month_lst = ['January','February','March','April','May','June','July','August','September','October','November','December']

class InputError(Exception):
    pass

def get_cal():
    try:
        year = int(input("연도를 입력하세요: "))
        month = int(input("월을 입력하세요: "))
    except ValueError:
        raise InputError(" >> 숫자를 입력하세요.")

    if month <= 0 or month > 12:
        raise InputError(" >> 월에 1~12 사이의 숫자를 입력하세요.")
    
    return year, month

def show_cal(year, month):
    print(f' [ {month_lst[month-1]} {year} ]')

while(True):
    try:
        year, month = get_cal()
    except InputError as e:
        print(e)
    else:
        show_cal(year, month)
    print()