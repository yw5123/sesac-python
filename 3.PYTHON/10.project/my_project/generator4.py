from generators.address_generator import AddressGenerator
from generators.birthdate_generator import BirthdateGenerator
from generators.gender_generator import GenderGenerator
from generators.id_generator import IdGenerator
from generators.name_generator import NameGenerator

from printers.output_printer import DataPrinter

import sys


class DataGenerator:
    numbers = 1
    data = []

    def __init__(self, numbers):
        self.numbers = numbers
        self.id_gen = IdGenerator()
        self.name_gen = NameGenerator()
        self.birth_gen = BirthdateGenerator()
        self.gender_gen = GenderGenerator()
        self.address_gen = AddressGenerator()

    def generate_users(self):
        self.data = []
        for _ in range(self.numbers):
            id = self.id_gen.generate_id()
            name = self.name_gen.generate_name()
            birthdate = self.birth_gen.generate_birthdate()
            gender = self.gender_gen.generate_gender()
            address = self.address_gen.generate_address()

            self.data.append((id, name, birthdate, gender, address))


# 메인 함수
if __name__ == "__main__":
    if len(sys.argv) <= 1:
        num_data = input('생성을 원하는 데이터 개수 입력: ')
    else:
        num_data = sys.argv[1]

    # 데이터 생성
    users1 = DataGenerator(int(num_data))
    users1.generate_users()
    
    # 데이터 출력
    my_printer = DataPrinter()
    if len(sys.argv) == 3:
        if sys.argv[2] == 'screen':
            my_printer.print_to_screen(users1.data)
        elif sys.argv[2] == 'file':
            my_printer.print_to_file(users1.data)
        else:
            print('지원되지 않는 출력 타입입니다 (screen/file)')
