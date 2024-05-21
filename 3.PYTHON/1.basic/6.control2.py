x = 10

if x < 10:
    print('x가 10보다 작습니다')
else:
    print('x가 10보다 크거나 같습니다')

# ------------------

score = 70

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(score, grade)

print("Name: {}, Grade: {}".format(score, grade))

print("Name: {0}, Grade: {1}".format(score, grade))
print("Name: {1}, Grade: {0}".format(score, grade))

print('점수는 {score}이고, 성적은 {grade}입니다')   # 문자열
print(f'점수는 {score}이고, 성적은 {grade}입니다')  # 포멧팅


math = 90
eng = 80

if math >= 90 or eng >= 90: # 조건을 and/or 바꿔보면서
    print('졸업조건 충족')
else:
    print('졸업 미흡')

