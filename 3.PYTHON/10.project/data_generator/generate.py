from user_generator import UserGenerator
from store_generator import StoreGenerator
from item_generator import ItemGenerator
from order_generator import OrderGenerator
from orderitem_generator import OrderItemGenerator

from printers.output_printer import DataPrinter

import os.path

class InputError(Exception):
    pass

def generate():
    try:
        data_type = input('생성할 데이터 종류 입력(user/store/item/order/orderitem): ')
        if data_type.lower() not in ['user','store','item','order','orderitem']:
            raise InputError("데이터 종류를 정확히 입력하세요.")
        
        # user, store, item csv파일이 없을 때 예외 처리
        if data_type.lower()=='order' and (os.path.isfile("user.csv")==False or os.path.isfile("store.csv")==False):
            raise InputError("user.csv 혹은 store.csv 파일이 없습니다.")
        
        elif data_type.lower()=='orderitem' and (os.path.isfile("item.csv")==False or os.path.isfile("order.csv")==False):
            raise InputError("item.csv 혹은 order.csv 파일이 없습니다.")


        data_num = input('생성할 데이터 개수 입력: ')
        if data_num.isdigit() == False:
            raise InputError("데이터 개수를 정확히 입력하세요.")
        
        prnt_type = input('출력 형식 입력(screen/file): ')
        if prnt_type.lower()!='screen' and prnt_type.lower()!='file':
            raise InputError("출력 형식을 정확히 입력하세요.")

    except InputError as e:
        print(" >>>", e)
        # exit()
        return


    if data_type.lower() == 'user':
        g_datas = UserGenerator()
        g_datas.generate_user(int(data_num))

    elif data_type.lower() == 'store':
        g_datas = StoreGenerator()
        g_datas.generate_store(int(data_num))

    elif data_type.lower() == 'item':
        g_datas = ItemGenerator()
        g_datas.generate_item(int(data_num))

    elif data_type.lower() == 'order':
        g_datas = OrderGenerator()
        g_datas.generate_order(int(data_num))

    elif data_type.lower() == 'orderitem':
        g_datas = OrderItemGenerator()
        g_datas.generate_orderitem(int(data_num))


    my_printer = DataPrinter()

    if prnt_type.lower() == 'screen':
        my_printer.print_to_screen(g_datas.data)
    elif prnt_type.lower() == 'file':
        my_printer.print_to_file(g_datas.data, f"{data_type.lower()}.csv")