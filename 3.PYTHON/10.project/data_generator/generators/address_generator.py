import random

class AddressGenerator:
    cities = []

    def __init__(self):
        with open("txt/address.txt",'r',encoding="utf-8") as file:
            self.cities = file.read().splitlines()

    def generate_address(self):
        return f"{random.choice(self.cities)} {random.randint(1, 99)}길 {random.randint(1, 99)}"