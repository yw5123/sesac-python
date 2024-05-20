# while True:
#     a = input('숫자를 입력하세요: ') 
#     print(a)

# 미션3. 숫자를 2개 입력 받아서 덧셈 결과

str_a = input('숫자를 입력하세요: ')
str_b = input('다음 숫자를 입력하세요: ')

int_a = int(str_a)  # 형 변환
int_b = int(str_b)

print(f'두 숫자의 합은 {int_a + int_b}입니다')
