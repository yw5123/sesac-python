import db_crud as db
# from db_crud import create_table, insert_user, fetch_users, update_user, delete_user

# 메인 함수
def main():
    # 테이블 생성
    db.create_table()

    # 데이터 삽입
    db.insert_user('Alice', 30)
    db.insert_user('Bob', 25)
    db.insert_user('Charlie', 35)

    # 데이터 조회
    print("--- 삽입 데이터 조회 ---")
    users = db.fetch_users()
    for user in users:
        print(user)

    # 데이터 수정
    db.update_user('Alice', 35)

    # 데이터 조회
    print("--- 수정 후 데이터 조회 ---")
    users = db.fetch_users()
    for user in users:
        print(user)

    # 데이터 삭제
    db.delete_user('Bob')

    # 데이터 조회
    print("--- 삭제 후 데이터 조회 ---")
    users = db.fetch_users()
    for user in users:
        print(user)

if __name__ == "__main__":
    main()