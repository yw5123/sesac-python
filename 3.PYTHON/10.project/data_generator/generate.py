from user_generator import UserGenerator
from store_generator import StoreGenerator
from item_generator import ItemGenerator
from order_generator import OrderGenerator
from orderitem_generator import OrderItemGenerator

from printers.output_printer import DataPrinter

import os.path

class InputError(Exception):
    pass

if __name__ == "__main__":
    
    try:
        data_type = input('생성할 데이터 종류 입력(user/store/item/order/orderitem): ')
        if data_type.lower()!='user' and data_type.lower()!='store' and data_type.lower()!='item' \
            and data_type.lower()!='order' and data_type.lower()!='orderitem':
            raise InputError("데이터 종류를 정확히 입력하세요.")
        
        # user, store, item csv파일이 없을 때 예외 처리
        if data_type.lower()=='order' and (os.path.isfile("user.csv")==False or os.path.isfile("store.csv")==False):
            raise InputError("user.csv 혹은 store.csv 파일이 없습니다.")
        
        elif data_type.lower()=='orderitem' and (os.path.isfile("item.csv")==False or os.path.isfile("order.csv")==False):
            raise InputError("item.csv 혹은 order.csv 파일이 없습니다.")


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

    elif data_type.lower() == 'order':
        orders = OrderGenerator()
        orders.generate_order(int(data_num))

        my_printer.print_to_screen(orders.data)
        my_printer.print_to_file(orders.data, "order.csv")

    elif data_type.lower() == 'orderitem':
        orderitems = OrderItemGenerator()
        orderitems.generate_orderitem(int(data_num))

        my_printer.print_to_screen(orderitems.data)
        my_printer.print_to_file(orderitems.data, "orderitem.csv")
