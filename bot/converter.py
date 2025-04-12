def show_menu():
    print("\nМеню конвертера единиц:")
    print("1. Длина")
    print("2. Вес")
    print("3. Температура")
    print("4. Выйти")

def convert_length():
    print("\nКонвертация длины:")
    print("1. Метры в километры")
    print("2. Километры в метры")
    print("3. Футы в метры")
    print("4. Метры в футы")
    choice = input("Выберите тип конвертации (1-4): ")
    if choice == "1":
        meters = float(input("Введите метры: "))
        print(f"Результат: {meters / 1000} км")
    elif choice == "2":
        kilometers = float(input("Введите километры: "))
        print(f"Результат: {kilometers * 1000} м")
    elif choice == "3":
        feet = float(input("Введите футы: "))
        print(f"Результат: {feet * 0.3048} м")
    elif choice == "4":
        meters = float(input("Введите метры: "))
        print(f"Результат: {meters / 0.3048} футов")
    else:
        print("Неверный выбор.")

def convert_weight():
    print("\nКонвертация веса:")
    print("1. Килограммы в фунты")
    print("2. Фунты в килограммы")
    choice = input("Выберите тип конвертации (1-2): ")
    if choice == "1":
        kilograms = float(input("Введите килограммы: "))
        print(f"Результат: {kilograms * 2.20462} фунтов")
    elif choice == "2":
        pounds = float(input("Введите фунты: "))
        print(f"Результат: {pounds / 2.20462} кг")
    else:
        print("Неверный выбор.")

def convert_temperature():
    print("\nКонвертация температуры:")
    print("1. Цельсий в Фаренгейт")
    print("2. Фаренгейт в Цельсий")
    choice = input("Выберите тип конвертации (1-2): ")
    if choice == "1":
        celsius = float(input("Введите температуру в Цельсиях: "))
        print(f"Результат: {celsius * 9 / 5 + 32} °F")
    elif choice == "2":
        fahrenheit = float(input("Введите температуру в Фаренгейтах: "))
        print(f"Результат: {(fahrenheit - 32) * 5 / 9} °C")
    else:
        print("Неверный выбор.")

def unit_converter():
    while True:
        show_menu()
        choice = input("Выберите категорию (1-4): ")
        if choice == "1":
            convert_length()
        elif choice == "2":
            convert_weight()
        elif choice == "3":
            convert_temperature()
        elif choice == "4":
            print("Выход из модуля конвертера единиц.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    unit_converter()
