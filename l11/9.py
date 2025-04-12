'''
Вклад в банке составляет money рублей. 
Ежегодно он увеличивается на percent процентов, 
после чего дробная часть отбрасывается. 
Определите, через сколько лет вклад составит не менее wish рублей.
Выражение «дробная часть копеек отбрасывается» означает, 
что если у вас оказалось 123.4567 рублей, т.е. 123 рубля и 45.67 копеек, 
то после округления у вас получится 123 рубля.

Значения money, percent, wish запросить у пользователя.
'''

def calculate_deposit_years(money, percent, wish):
    years = 0
    while money < wish:
        money += money * percent / 100
        money = int(money)  # Отбрасываем дробную часть
        years += 1
    return years

money = float(input("Введите начальную сумму вклада (руб.): "))
percent = float(input("Введите годовой процент (%): "))
wish = float(input("Введите желаемую сумму (руб.): "))

years_needed = calculate_deposit_years(money, percent, wish)
print(f"Через {years_needed} лет вклад составит не менее {wish} рублей.")