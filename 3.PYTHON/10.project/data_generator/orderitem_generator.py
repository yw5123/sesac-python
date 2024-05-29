from generators.id_generator import IdGenerator

import csv
import random

class OrderItemGenerator:
    data = []
    oid_lst = []
    iid_lst = []

    def __init__(self):
        self.id_gen = IdGenerator()
        with open("order.csv",'r',encoding="utf-8") as file:
            reader = csv.reader(file)
            for r in reader:
                self.oid_lst.append(r[0])
        with open("item.csv",'r',encoding="utf-8") as file:
            reader = csv.reader(file)
            for r in reader:
                self.iid_lst.append(r[0])
        
        del self.oid_lst[0]
        del self.iid_lst[0]

    def generate_orderitem(self, num):
        self.data.append(('Id','OrderId','ItemId'))
        for _ in range(num):
            oiid = self.id_gen.generate_id()

            o_id = random.choice(self.oid_lst)
            i_id = random.choice(self.iid_lst)

            self.data.append((oiid, o_id, i_id))



# ----- 확인용 코드 -----
# from printers.output_printer import DataPrinter

# if __name__ == "__main__":
#     orderitems = OrderItemGenerator()
#     orderitems.generate_orderitem(5)

#     my_printer = DataPrinter()
#     my_printer.print_to_screen(orderitems.data)
#     my_printer.print_to_file(orderitems.data, "orderitem_output.csv")
