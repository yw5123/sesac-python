from generators.id_generator import IdGenerator

import csv
import random

class OrderGenerator:
    data = []
    sid_lst = []
    uid_lst = []

    def __init__(self):
        self.id_gen = IdGenerator()
        with open("csv/store.csv",'r',encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for r in reader:
                self.sid_lst.append(r)
            # reader = csv.reader(file)
            # for r in reader:
            #     self.sid_lst.append(r[0])
        with open("csv/user.csv",'r',encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for r in reader:
                self.uid_lst.append(r)
        #     reader = csv.reader(file)
        #     for r in reader:
        #         self.uid_lst.append(r[0])
        
        # del self.sid_lst[0]
        # del self.uid_lst[0]
        

    def generate_order(self, num):
        self.data.append(('Id','OrderAt','StoreId','UserId'))
        for _ in range(num):
            oid = self.id_gen.generate_id()

            month = random.randint(1,12)
            if month == 2:
                day = random.randint(1,28)
            elif month == 4 or month == 6 or month == 9 or month == 11:
                day = random.randint(1,30)
            else:
                day = random.randint(1,31)
            o_at = f"2023-{month:02d}-{day:02d} 2023-{random.randint(0,23):02d}-{random.randint(0,59):02d}"

            s_id = random.choice(self.sid_lst)
            u_id = random.choice(self.uid_lst)

            self.data.append((oid, o_at, s_id['Id'], u_id['Id']))
            # self.data.append((oid, o_at, s_id, u_id))



# ----- 확인용 코드 -----
# from printers.output_printer import DataPrinter

# if __name__ == "__main__":
#     orders = OrderGenerator()
#     orders.generate_order(5)

#     my_printer = DataPrinter()
#     my_printer.print_to_screen(orders.data)
#     my_printer.print_to_file(orders.data, "order_output.csv")
