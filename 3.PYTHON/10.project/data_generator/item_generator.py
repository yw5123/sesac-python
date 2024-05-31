from generators.id_generator import IdGenerator
from generators.item_name_generator import InameGenerator


class ItemGenerator:
    data = []

    def __init__(self):
        self.id_gen = IdGenerator()
        self.name_gen = InameGenerator()

    def generate_item(self, num):
        self.data = []
        self.data.append(('Id','Name','Type','UnitPrice'))
        for _ in range(num):
            iid = self.id_gen.generate_id()
            name, itype, price = self.name_gen.generate_type()

            self.data.append((iid, name, itype, price))


# ----- 확인용 코드 -----
# from printers.output_printer import DataPrinter

# if __name__ == "__main__":

#     items = ItemGenerator()
#     items.generate_item(5)

#     my_printer = DataPrinter()
#     my_printer.print_to_screen(items.data)
#     my_printer.print_to_file(items.data, "item_output.csv")
    