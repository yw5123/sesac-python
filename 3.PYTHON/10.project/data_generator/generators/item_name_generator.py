import random

class InameGenerator:
    data = {}
    sub_dict = {}

    def __init__(self):
        with open("txt/category.txt",'r',encoding="utf-8") as file:
            self.types = file.read().splitlines()

        for t in self.types:
            with open(f"txt/{str(t).lower()}.txt",'r',encoding="utf-8") as file:
                self.nameprice = file.read().splitlines()
                
                # txt 파일에서 이름, 가격 불러와서 딕셔너리에 넣음
                for np in self.nameprice:
                    np_data = np.split(',')
                    name = np_data[0].strip()
                    price = np_data[1].strip()
                    self.sub_dict[name] = price

                self.data[t] = self.sub_dict

            self.sub_dict = {}

    def generate_type(self):
        itype = random.choice(list(self.data.keys()))
        name = random.choice(list(self.data[itype].keys()))
        price = self.data[itype][name]

        return name, itype, price
    
