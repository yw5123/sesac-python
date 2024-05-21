s = 'Hello World sesac!'
l = 'hello'
u = 'HELLO'
print(s)

print(len(s))
print(type(s))

print(s.lower())
print(s.upper())
print(l.islower())
print(l.isupper())
print(u.islower())
print(u.isupper())
print(s.capitalize())
print(s.title())

s2 = '  hello world      !! '
print(s2.strip())
s3 = 'apple, banana,cherry, orange'
print(s3.split())
print(s3.split(','))

s3_list = s3.split(',')
print(s3_list)

s3_clean_list = []
for fruit in s3_list:
    # clean_name = fruit.strip()
    # s3_clean_list.append(clean_name)
    s3_clean_list.append(fruit.strip())

print(s3_clean_list)

# list comprehension (리스트 컴프리헨션) : 파이썬의 특징이자 장점
# 엄~~청나게 좋은 건데.. 익숙해질 때까지 시간이 걸림

print('list comprehension')
s4_list = [fruit.strip() for fruit in s3.split(',')]
print(s4_list)