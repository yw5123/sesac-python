import random

class StypeGenerator:
    types = []

    def __init__(self):
        with open("txt/store_type.txt",'r',encoding="utf-8") as file:
            self.types = file.read().splitlines()

    def generate_type(self):
        return random.choice(self.types)