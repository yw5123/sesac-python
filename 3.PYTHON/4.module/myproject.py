# import mymodule
from mymodule import greet, greet_kor
# from mymodule import *    # 이렇게 사용할 수는 있지만 권장 X

greeting = greet('SESAC')
print(greeting)

greeting2 = greet_kor('John')
print(greeting2)