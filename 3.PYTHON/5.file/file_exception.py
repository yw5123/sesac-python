contents = ""

try:
    with open("file.txt", 'r') as file:
        # contents = file.read()
        file.write('Hello')
except FileNotFoundError:
    print("파일이 없습니다.")
except PermissionError:
    print("해당 파일에는 쓰기 권한이 없습니다.")
except IOError:
    print("해당 파일의 내용을 읽고/쓰고 할 수 없습니다.")
except:
    print("알 수 없는 오류가 발생했습니다.")    # 모든 오류를 퉁쳐서 잡을 수 있음 (바람직하지 x)

print("파일 내용: ", contents)