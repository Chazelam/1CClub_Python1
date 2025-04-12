# Импортируем функцию randint из модуля random для генерации случайных чисел
from random import randint

# Настройки
lower_limit = 1         # Минимальное случайное число
upper_limit = 100       # Максимальное случайное число
number_of_attempts = 5  # Количество попыток

# Генерируем случайное число
win_number = randint(lower_limit, upper_limit)
attemts_counter = 0 # счетчик попыток

# Получаем первое число от пользователя
user_number = int(input(f"Введите число в пределах от {lower_limit} до {upper_limit}: "))

# Основной игровой цикл - работает пока число не угадано
while win_number != user_number:
    print("Неверно!")
    attemts_counter += 1 # Увеличиваем счетчик попыток

    # Проверяем, не исчерпал ли игрок все попытки
    if attemts_counter > number_of_attempts:
        print("Проигрыш.")
        break # Выходим из цикла если попытки закончились

    # Запрашиваем у пользователя новое число
    user_number = int(input(f"Введите число в пределах от {lower_limit} до {upper_limit}: "))
else:
    # Этот блок выполнится только если цикл завершился не через break,
    # то есть если пользователь угадал число
    print(f"Поздровляем! Победа!\nВы отгадали с {attemts_counter} попытки")