from math import hypot, log  # Импортируем функции для работы с двумя числами

def add(number_1, number_2):
    """Подсчет суммы двух чисел"""
    return f"{number_1} + {number_2} = {number_1 + number_2}"

def sub(number_1, number_2):
    """Подсчет разности двух чисел"""
    return f"{number_1} - {number_2} = {number_1 - number_2}"

def mul(number_1, number_2):
    """Подсчет произведения двух чисел"""
    return f"{number_1} * {number_2} = {number_1 * number_2}"

def div(number_1, number_2):
    """Подсчет частного двух чисел"""
    if number_2 == 0:
        return "На ноль делить нельзя!"
    return f"{number_1} / {number_2} = {number_1 / number_2}"

# Добавленные функции из модуля math
def hypotenuse(a, b):
    """Вычисление гипотенузы (hypot) по двум катетам"""
    return f"Гипотенуза ({a}, {b}) = {hypot(a, b)}"

def logarithm(number, base):
    """Вычисление логарифма (log) числа по указанному основанию"""
    if number <= 0 or base <= 0 or base == 1:
        return "Недопустимые значения для логарифма!"
    return f"log_{base}({number}) = {log(number, base)}"

def calculator():
    """Расширенный калькулятор с поддержкой новых операций"""
    # Обновленное приглашение с новыми операциями
    operation = input("Действие (+, -, *, /, hyp, log). Для завершения введите 0: ")
    
    while operation != "0":
        # Все операции требуют двух чисел
        number_1 = float(input("Первое число: "))
        number_2 = float(input("Второе число: "))
        
        if operation == "+":
            print(add(number_1, number_2))
        elif operation == "-":
            print(sub(number_1, number_2))
        elif operation == "*":
            print(mul(number_1, number_2))
        elif operation == "/":
            print(div(number_1, number_2))
        elif operation == "hyp":
            print(hypotenuse(number_1, number_2))
        elif operation == "log":
            print(logarithm(number_1, number_2))
        else:
            print("Действие не найдено!")
        
        # Повторный запрос операции
        operation = input("Действие (+, -, *, /, hyp, log). Для завершения введите 0: ")

if __name__ == "__main__":
    calculator()