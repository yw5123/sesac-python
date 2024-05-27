import random
import uuid

class IdGenerator:
    def generate_id(self):
        return str(uuid.uuid4())

class NameGenerator:
    names = ['John','Jane','Michael','Emily','William','Olivia']

    def generate_name(self):
        return random.choice(self.names)

class BirthdateGenerator:
    year_start = 1980
    year_end = 2005

    def generate_birthdate(self):
        year = random.randint(self.year_start, self.year_end)
        month = random.randint(1,12)
        day = random.randint(1,28)
        return f"{year}-{month:02d}-{day:02d}"

class GenderGenerator:
    gender = ['Male','Female']

    def generate_gender(self):
        return random.choice(self.gender)

class AddressGenerator:
    cities = ['New York','Los Angeles','Chicago','Houston','Philadelphia']

    def generate_address(self):
        city = random.choice(self.cities)
        street = random.randint(1, 100)
        return f"{street} {city}"

class DataGenerator:
    numbers = 1
    data = []

    def __init__(self, numbers):
        self.numbers = numbers
        self.id_gen = IdGenerator()
        self.name_gen = NameGenerator()
        self.birth_gen = BirthdateGenerator()
        self.gender_gen = GenderGenerator()
        self.address_gen = AddressGenerator()

    def generate_users(self):
        self.data = []
        for _ in range(self.numbers):
            id = self.id_gen.generate_id()
            name = self.name_gen.generate_name()
            birthdate = self.birth_gen.generate_birthdate()
            gender = self.gender_gen.generate_gender()
            address = self.address_gen.generate_address()

            self.data.append((id, name, birthdate, gender, address))


# 메인 함수
if __name__ == "__main__":

    users1 = DataGenerator(5)
    users1.generate_users()
    for d in users1.data:
        print(d)

    users2 = DataGenerator(10)
    users2.generate_users()
    for d in users2.data:
        print(d)

    for d in users1.data:
        print(d[0])

    for d in users2.data:
        print(d[0])
