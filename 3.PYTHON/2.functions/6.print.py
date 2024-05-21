# 1. 일반 문자열 출력
print(' - 1 - ')
print('hello')
print('hello world')
print('hello', 'world')
print(1,2,3)

# 2. f-문자열 (f-string) 사용
print(' - 2 - ')
print(f"hello {1}")
내변수 ='123'   # 실무에서 한글 쓰면 안 됨ㅋㅋ
print(f"hello {내변수}")
my_variable="456"
print(f"hello {my_variable}")

# 3. 문자열 포멧팅 {} 사용
print(' - 3 - ')
name="홍길동"
print("Hello, {}".format(name))
print("Hello, {} x {} = {}".format(내변수, my_variable, name))

# 4. 문자열 포멧팅에 순번 부여 {0}
print(' - 4 - ')
print("Hello, {0} x {1} = {2}".format(내변수, my_variable, name))
print("Hello, {2} x {0} = {1}".format(내변수, my_variable, name))
print("Hello, {2} x {1} = {0}".format(내변수, my_variable, name))

# 5. 문자열 연결 연산자
print(' - 5 - ')
print('hello', end=" ")
print('world', end=" ")
print('sesac')

# 6. % 연산자 - 예전에 가장 보편적인 방식
print(' - 6 - ')
age = 30
print('Hello, %s' % name)   # %s 는 문자열 (string)
print('Hello, %d' % age)   # %d 는 숫자 (decimal)
print('Hello, %s' % age)