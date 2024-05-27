import random

surname = ['김','이','박','최','정']
middlename = ['민','효','여','인','소']
lastname = ['현','원','운','희','철']

def generate_name():
    name = random.choice(surname)+random.choice(middlename)+random.choice(lastname)
    return name

for _ in range(10):
    print(generate_name())