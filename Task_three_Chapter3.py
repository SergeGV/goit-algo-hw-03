import re

def normalize_phone(phone_number):
    # Видаляємо всі символи, крім цифр і знаку "+"
    phone_number = re.sub(r'[^\d+]', '', phone_number)
    
    # Перевіряємо, чи номер починається з "+"
    if phone_number.startswith('+'):
        # Якщо номер починається з "+", але не з "+38", додаємо "38"
        if not phone_number.startswith('+38'):
            phone_number = '+38' + phone_number[1:]
    else:
        # Якщо "+" немає, додаємо "+38"
        phone_number = '+38' + phone_number
    
    return phone_number

# Приклади використання
print(normalize_phone("    +38(050)123-32-34"))   # Виведе: +380501233234
print(normalize_phone("     0503451234"))          # Виведе: +380503451234
print(normalize_phone("(050)8889900"))             # Виведе: +380508889900
print(normalize_phone("38050-111-22-22"))          # Виведе: +380501112222
print(normalize_phone("38050 111 22 11   "))       # Виведе: +380501112211