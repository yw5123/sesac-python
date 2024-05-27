import random
import csv
from itertools import chain

class NameGenerator:
    names = []

    def __init__(self):
        with open('names.txt','r',encoding="utf-8") as file:
            # self.names = file.read().splitlines()
            csvreader = csv.reader(file)
            csv_list_names = [n for n in csvreader]
            names_list = list(chain(*csv_list_names))
            self.names = [n.strip() for n in names_list]

    def generate_name(self):
        return random.choice(self.names)