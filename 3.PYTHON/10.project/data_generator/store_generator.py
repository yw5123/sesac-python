from generators.id_generator import IdGenerator
from generators.store_type_generator import StypeGenerator
from generators.address_generator import AddressGenerator

import random


class StoreGenerator:
    data = []

    def __init__(self):
        self.id_gen = IdGenerator()
        self.type_gen = StypeGenerator()
        self.address_gen = AddressGenerator()

    def generate_store(self, num):
        self.data = []
        self.data.append(('Id','Name','Type','Address'))
        for _ in range(num):
            sid = self.id_gen.generate_id()
            stype = self.type_gen.generate_type()
            address = self.address_gen.generate_address()
            name = f"{stype} {address[:2]}{random.randint(1, 15)}호점"

            self.data.append((sid, name, stype, address))



# ----- 확인용 코드 -----
# from printers.output_printer import DataPrinter

# import sys

# class CustomError(Exception):
    # pass

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

#     stores = StoreGenerator()
#     stores.generate_store(int(num_data))

#     my_printer = DataPrinter()
#     if prnt_type == 'screen':
#         my_printer.print_to_screen(stores.data)
#     elif prnt_type == 'file':
#         my_printer.print_to_file(stores.data, "store_output.csv")
#     else:
#         print('지원되지 않는 출력 타입입니다 (screen/file)')