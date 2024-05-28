import random

class InameGenerator:
    data = {
        "Coffee": {
            "Americano": 3000,
            "Latte": 4000,
            "Espresso": 2500,
            "Cappuccino": 4500,
            "Mocha": 5000
        },
        "Juice": {
            "Orange": 2000,
            "Apple": 2500,
            "Grape": 3000,
            "Pineapple": 3500,
            "Watermelon": 4000
        },
        "Cake": {
            "Chocolate": 6000,
            "Strawberry": 5500,
            "Vanilla": 5000,
            "Red Velvet": 6500,
            "Carrot": 6000
        }
    }

    def generate_type(self):
        itype = random.choice(list(self.data.keys()))
        name = random.choice(list(self.data[itype].keys()))
        price = self.data[itype][name]

        return name, itype, price
    

if __name__ == "__main__":
    item = InameGenerator()
    print(item.generate_type())