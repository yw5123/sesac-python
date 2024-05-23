# 파일 입출력할 때 사용하는 함수 open

# with open('example.txt', 'a') as file:
#     file.write("Hello, World2\n")

# print("텍스트 파일 기록을 완료하였습니다.")

# with open('example.txt', 'r') as file:
#     context = file.read()
#     print(context)

# with open('example.txt', 'r') as file:  # 파일에 접근하기 위한 포인터
#     for line in file:
#         print(line, end="")

with open('example.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line, end="")