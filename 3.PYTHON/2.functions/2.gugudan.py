# dan = int(input('계산을 원하는 단을 입력하시오: '))

def print_gugudan(dan):
    print(f'[ {dan}단 ]')
    for i in range(1,10):
        # print(f'{dan} x {i} = {dan*i}')
        print('{} x {} = {}'.format(dan,i,dan*i))

for dan in range(2, 10):
    print_gugudan(dan)
    print()