# https://docs.python.org/ko/3/library/datetime.html
import datetime

# 모둘명.클래스(객체)명.함수명

current_time = datetime.datetime.now()
print(current_time)

my_time = datetime.datetime(2024, 1, 1, 10, 30, 0)
print(my_time)
print(type(my_time))