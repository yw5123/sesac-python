from generators.id_generator import IdGenerator
from generators.user_name_generator import UnameGenerator
from generators.user_birthdate_generator import BirthdateGenerator
from generators.user_gender_generator import GenderGenerator
from generators.address_generator import AddressGenerator


class UserGenerator:
    data = []

    def __init__(self):
        self.id_gen = IdGenerator()
        self.name_gen = UnameGenerator()
        self.birth_gen = BirthdateGenerator()
        self.gender_gen = GenderGenerator()
        self.address_gen = AddressGenerator()

    def generate_user(self, num):
        self.data = []
        self.data.append(('Id','Name','Gender','Age','Birthdate','Address'))
        for _ in range(num):
            uid = self.id_gen.generate_id()
            name = self.name_gen.generate_name()
            gender = self.gender_gen.generate_gender()
            age, birthdate = self.birth_gen.generate_birthdate()
            address = self.address_gen.generate_address()

            self.data.append((uid, name, gender, age, birthdate, address))



# ----- 확인용 코드 -----
# from printers.output_printer import DataPrinter
# import sys

# class CustomError(Exception):
#     pass
    
# if __name__ == "__main__":
#     num_data = 0

#     if len(sys.argv) == 1:
#         num_data = input('생성 데이터 개수 입력: ')
#     elif len(sys.argv) >= 2:
#         num_data = sys.argv[1]

#     if num_data.isdigit() == False:
#         num_data = 0
#         print('데이터를 생성할 개수를 숫자로 입력하세요')

#     if len(sys.argv) == 3:
#         prnt_type = sys.argv[2]
#     else:
#         prnt_type = input('출력 형식 입력(screen/file): ')

#     users = UserGenerator()
#     users.generate_user(int(num_data))

#     my_printer = DataPrinter()
#     if prnt_type == 'screen':
#         my_printer.print_to_screen(users.data)
#     elif prnt_type == 'file':
#         my_printer.print_to_file(users.data, "user_output.csv")
#     else:
#         print('지원되지 않는 출력 타입입니다 (screen/file)')
