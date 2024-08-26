from datetime import datetime

def get_days_from_today(date):
    try:
        # Перетворюємо рядок дати у форматі 'РРРР-ММ-ДД' на об'єкт datetime
        given_date = datetime.strptime(date, '%Y-%m-%d').date()
        # Отримуємо поточну дату
        today = datetime.today().date()
        # Розраховуємо різницю між датами
        delta = today - given_date
        # Повертаємо кількість днів як ціле число
        return delta.days
    except ValueError:
        # Якщо формат дати некоректний, повертаємо повідомлення про помилку
        return "Неправильний формат дати. Будь ласка, використовуйте 'РРРР-ММ-ДД'."

# Приклад використання
print(get_days_from_today('2023-08-20'))  # Виведе кількість днів між поточною датою та 20 серпня 2023 року