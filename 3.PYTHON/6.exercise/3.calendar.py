# 미션3. 달력 만들기 (텍스트로 년/월 입력받아 출력)

month_lst = ['January','February','March','April','May','June','July','August','September','October','November','December']
month_day = [31,28,31,30,31,30,31,31,30,31,30,31]

class InputError(Exception):
    pass

def get_cal():
    try:
        year = int(input("연도를 입력하세요: "))
        month = int(input("월을 입력하세요: "))
    except ValueError:
        raise InputError(" >> 숫자를 입력하세요.")

    if year < 1:
        raise InputError(" >> 1년 이후의 달력만 조회 가능합니다.")
    if month < 1 or month > 12:
        raise InputError(" >> 월에 1~12 사이의 숫자를 입력하세요.")
    
    return year, month

def cal_cal(year, month):
    lyear = False
    cal_days = (year-1)*365 + (year-1)/4 - (year-1)/100 + (year-1)/400
    for i in range(month-1):
        cal_days += month_day[i]
    if year%4==0 and year%100!=0 or year%400==0:
        lyear = True
        if month > 2:
            cal_days += 1
    cal_days += 1
    find_1day = int(cal_days % 7)    # 1일의 요일 구하기
    print(f'       [ {month_lst[month-1]} {year} ]')
    print("SUN MON TUE WED THU FRI SAT")

    show_cal(find_1day, month, lyear)
            

def show_cal(day1, month, lyear):
    if lyear == True:
        month_day[1] = 29

    print('   '*day1+' '*day1, end="")
    for i in range(month_day[month-1]):
        if i < 9:
            print(f' {i+1}  ', end="")
        else:
            print(f'{i+1}  ', end="")

        if (i+1+day1)%7 == 0:
            print()

    if lyear == True:
        month_day[1] = 28


while(True):
    try:
        year, month = get_cal()
    except InputError as e:
        print(e)
    else:
        cal_cal(year, month)
    print()

