'''
Банку "Великие проценты" необходима программа для банкомата, 
которая по введенной сумме будет определять количество банкнот для выдачи клиенту. 
В наличии имеются номиналы: 50, 100, 200, 500, 1000, 2000, 5000 рублей. 
Оставшуюся сумму возвращать на карту (Используйте операторы // и %).
'''

def atm_withdrawal(amount):
    # Инициализация переменных для подсчета банкнот каждого номинала
    count_5000 = count_2000 = count_1000 = count_500 = count_200 = count_100 = count_50 = 0

    # Подсчет количества банкнот для каждого номинала
    if amount >= 5000:
        count_5000 = amount // 5000
        amount %= 5000
    if amount >= 2000:
        count_2000 = amount // 2000
        amount %= 2000
    if amount >= 1000:
        count_1000 = amount // 1000
        amount %= 1000
    if amount >= 500:
        count_500 = amount // 500
        amount %= 500
    if amount >= 200:
        count_200 = amount // 200
        amount %= 200
    if amount >= 100:
        count_100 = amount // 100
        amount %= 100
    if amount >= 50:
        count_50 = amount // 50
        amount %= 50

    # Вывод результата
    print("Количество банкнот:")
    if count_5000 > 0:
        print(f"5000 руб.: {count_5000} шт.")
    if count_2000 > 0:
        print(f"2000 руб.: {count_2000} шт.")
    if count_1000 > 0:
        print(f"1000 руб.: {count_1000} шт.")
    if count_500 > 0:
        print(f"500 руб.: {count_500} шт.")
    if count_200 > 0:
        print(f"200 руб.: {count_200} шт.")
    if count_100 > 0:
        print(f"100 руб.: {count_100} шт.")
    if count_50 > 0:
        print(f"50 руб.: {count_50} шт.")

    # Если осталась сумма, которая не может быть выдана банкнотами
    if amount > 0:
        print(f"Остаток ({amount} руб.) возвращается на карту.")

# Ввод суммы для выдачи
amount = int(input("Введите сумму для выдачи: "))
atm_withdrawal(amount)