# list comprehension 리스트 컴프리헨션
# []
# [표현식 for 항목 in 반복 (조건문)]


# 1. 1부터 10까지의 숫자를 담는 리스트 생성
nums = [num for num in range(1, 11)]
print(nums)


# 2. 위 리스트의 각 숫자의 제곱을 구하고 싶으면?
squares = [num**2 for num in range(1, 11)]
print(squares)


# 3. 1부터 20까지의 짝수로 이루어진 리스트
even_nums = [num for num in range(1, 21) if num % 2 == 0]
# even_nums = [num for num in range(2, 21, 2)]
print(even_nums)

odd_nums = [num for num in range(1, 21) if num % 2 == 1]
print(odd_nums)


# 4. 문자열의 각 글자를 대문자로 바꾼 리스트 생성
word = 'hello'
upper_letters = [letter.upper() for letter in word]
print(upper_letters)