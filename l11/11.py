'''
Клуб по интересам "Шестое чувство" решил проверить свое окружение. 
Человек может продолжить членство в клубе, если его любимое число делится на 6. 
Число делится на 6 только в случае соблюдения двух условий:
 - Последняя его цифра четная
 - Сумма всех цифр делится на 3

Напишите функцию is_divisible_by_6(number), которая возвращает 
Число number делится на 6 или Число number неделимо на 6 в зависимости от того, можно ли его разделить на 6.
 
В качестве аргумента может быть передано любое целое число.
'''

def is_divisible_by_6(number):
    if number < 0:
        number *= -1

    last_digit = number % 10
    digit_sum = 0
    while number > 0:
        digit_sum += number % 10
        number = number // 10

    if last_digit % 2 == 0 and digit_sum % 3 == 0:
        return f"Число {number} делится на 6"
    else:
        return f"Число {number} неделимо на 6"

number = int(input("Введите число: "))
print(is_divisible_by_6(number))
