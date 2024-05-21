
# for i in range(6):
#     for j in range(i):
#         print("*", end="")
#     print()

# row = int(input('출력을 원하는 높이를 입력하세요: '))
# for i in range(1,row+1):
#     print('*' * i)

# for i in range(1,6):
#     print(' ' * (5-i) + '*' * i)

# row = int(input('출력을 원하는 높이를 입력하세요: '))
# for i in range(1,row+1):
#     print(' ' * (row-i) + '*' * i)

row = 5

for i in range(1,row+1):
    print(' ' * (row-i) + '*' * (2*i-1))
# for i in range(1,row):
#     print(' ' * i + '*' * (2*(row-i)-1))
for i in range(row-1,0,-1):
    print(' ' * (row-i) + '*' * (2*i-1))