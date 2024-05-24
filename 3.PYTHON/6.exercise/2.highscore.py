# 미션2. 게임 스코어 저장하기
# 점수와 이름 입력받기 -> 다양한 모드(score, high, history)에 따라 기능 구현

score_lst = []

class InputError(Exception):
    pass

def select_mode():
    print("[ 모드 ]")
    print("1. SCORE")
    print("2. HIGH")
    print("3. HISTORY")

    m_input = input("원하는 모드의 번호를 입력하세요: ")

    if m_input.upper() not in ['1', '2', '3']:
        raise InputError
    return int(m_input)

def m_score():
    print("=== SCORE ===")
    try:
        get_score = int(input("점수를 입력하세요: "))
    except ValueError:
        print(" *입력 오류: 숫자만 입력해주세요.")
        return
    get_name = input("이름을 입력하세요: ")
    score_lst.append([get_name, get_score])
    

def m_high():
    print("=== HIGH ===")
    print("[이름]    [점수]")

    chk_index = []

    try:
        chk_max = score_lst[0][1]
    except IndexError:
        print("")
        return

    for lst in enumerate(score_lst):
        if chk_max < int(lst[1][1]):
            chk_max = int(lst[1][1])
            chk_index = [lst[0]]
        elif chk_max == int(lst[1][1]):
            chk_index.append(lst[0])
    
    for ind in chk_index:
        print(f" {score_lst[ind][0]}       {score_lst[ind][1]}")

def m_history():
    print("=== HISTORY ===")
    print("[이름]    [점수]")
    for lst in score_lst:
        print(f"  {lst[0]}        {lst[1]}")

while(True):
    try:
        mode = select_mode()
    except InputError:
        print(" >> 정확한 번호를 입력해주세요\n")
        continue
    
    if mode == 1:
        m_score()
    elif mode == 2:
        m_high()
    elif mode == 3:
        m_history()
    
    print()