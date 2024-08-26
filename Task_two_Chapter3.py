import random

def get_numbers_ticket(min, max, quantity):
    # Перевірка на коректність параметрів
    if min < 1 or max > 1000 or quantity > (max - min + 1) or min > max:
        return []

    # Генерація унікальних випадкових чисел
    numbers = random.sample(range(min, max + 1), quantity)
    
    # Сортування чисел
    numbers.sort()

    return numbers

# Приклад використання
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)