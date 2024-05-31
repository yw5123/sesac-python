import random
from datetime import datetime

class BirthdateGenerator:
    def generate_birthdate(self):
        now = datetime.now()
        year = random.randint(1960,2010)
        month = random.randint(1,12)

        if month == 2:
            day = random.randint(1,28)
        elif month == 4 or month == 6 or month == 9 or month == 11:
            day = random.randint(1,30)
        else:
            day = random.randint(1,31)
        
        age = now.year - year

        return age, f"{year}-{month:02d}-{day:02d}"