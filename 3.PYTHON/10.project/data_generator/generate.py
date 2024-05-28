from user_generator import UserGenerator
from store_generator import StoreGenerator
from item_generator import ItemGenerator

from printers.output_printer import DataPrinter

class InputError(Exception):
    pass

if __name__ == "__main__":
    
    try:
        data_type = input('생성할 데이터 종류 입력(user, store, item): ')
        if data_type.lower()!='user' and data_type.lower()!='store' and data_type.lower()!='item':
            raise InputError("데이터 종류를 정확히 입력하세요.")
        
        data_num = input('생성할 데이터 개수 입력: ')
        if data_num.isdigit() == False:
            raise InputError("데이터 개수를 정확히 입력하세요.")
        
        # prnt_type = input('출력 형식 입력(screen/file): ')
        # if prnt_type.lower()!='screen' and prnt_type.lower()!='file':
        #     raise InputError("출력 형식을 정확히 입력하세요.")

    except InputError as e:
        print(" >>>", e)
        exit()


    my_printer = DataPrinter()

    if data_type.lower() == 'user':
        users = UserGenerator()
        users.generate_user(int(data_num))

        my_printer.print_to_screen(users.data)
        my_printer.print_to_file(users.data, "user.csv")

    elif data_type.lower() == 'store':
        stores = StoreGenerator()
        stores.generate_store(int(data_num))

        my_printer.print_to_screen(stores.data)
        my_printer.print_to_file(stores.data, "store.csv")

    elif data_type.lower() == 'item':
        items = ItemGenerator()
        items.generate_item(int(data_num))
        
        my_printer.print_to_screen(items.data)
        my_printer.print_to_file(items.data, "item.csv")

    