f_num = int(input('팩토리알을 구할 숫자: '))

def factorial(f_num):
    result = 1
    for i in range(1,f_num+1):
        result *= i
    print(f'{f_num}! = {result}')
    
# def factorial(f_num):
#     result = 1
#     for i in range(f_num, 0, -1):
#         result *= i
#     print(f'{f_num}! = {result}')

factorial(f_num)