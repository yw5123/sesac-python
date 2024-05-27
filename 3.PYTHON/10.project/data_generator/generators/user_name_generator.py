import random

class UnameGenerator:
    fnames = []
    lnames = []

    def __init__(self):
        with open("user_fname.txt",'r',encoding="utf-8") as file:
            self.fnames = file.read().splitlines()
        with open("user_lname.txt",'r',encoding="utf-8") as file:
            self.lnames = file.read().splitlines()

    def generate_name(self):
        return f"{random.choice(self.lnames)}{random.choice(self.fnames)}"