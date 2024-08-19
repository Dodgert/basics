from datetime import datetime
import random
import re

# Перше завдання
def get_days_from_today(date):
    try:
        string_to_date = datetime.strptime(date, "%Y-%m-%d").date()
        time_delta = string_to_date - datetime.today().date()
        return (time_delta.days)
    except ValueError:
        print(f"Введені дані {date} мають неправильний формат")

# Друге завдання
def get_numbers_ticket(min, max, quantity):
    numbers = []
    try:
        while quantity > 0 and min <= quantity <= max:
            new_number = random.randint(min, max)
            if numbers.count(new_number) == 0:
                numbers.append(new_number)
                quantity = (quantity - 1)
            else:
                None
        numbers.sort()
        return numbers
    except ValueError:
       return numbers
    except TypeError:
       return numbers

# Третє завдання
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(num):
    for key in num:
        modified_number = "+38" + re.sub(r"\W[^0-9]|[)(;,\-:!\s]|\+38|38", "", num)
    return modified_number

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)