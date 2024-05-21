class Person:
    # 명사, Property를 정의할 수 있음
    name =""
    age = 0
    status = ""

    def __init__(self, name, age):     # 이 객체의 초기화 함수
        self.name = name
        self.age = age

    # 메소드 (함수 = 행위 지정하는 동사)
    def speak(self):
        print(f'[{self.name}]: 안녕하세요')
    
    def walk(self):
        print(f'[{self.name}]: 저는 걸어가는 중입니다')
        self.status = "walking"

    def run(self):
        print(f'[{self.name}]: 저는 뛰어가는 중입니다')
        self.status = "running"

    def motion(self):
        print(f'[{self.name}]: 나의 현재 상태는 {self.status} 중입니다')

    def introduce(self):
        print(f'안녕하세요, 저는 {self.name}이고, {self.age}살입니다.')

# 사람(Person) 이라는 객체를 만들고
# 사람이 할 수 있는 행위 (method)인 speak과 walk 정의

# alice = Person()
# alice.name = 'Alice'
# alice.age = 30

alice = Person('Alice', 30)

alice.introduce()
alice.speak()
alice.walk()
alice.motion()

# bob = Person()
# bob.name = 'Bob'
# bob.age = 40

bob = Person('Bob', 40)

bob.introduce()
bob.speak()
bob.run()
bob.motion()