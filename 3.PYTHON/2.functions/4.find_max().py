numbers = [-3, -7, -2, -9, -10, -5, -6, -8, -4]

def find_max(numbers):
    max_num = numbers[0]
    for i in numbers[1:]:
        if i > max_num:
            max_num = i
    print(f'가장 큰 수 출력: {max_num}')
    
find_max(numbers)