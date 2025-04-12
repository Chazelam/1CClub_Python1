from time import time

def keyboard_train():
    # Предопределенный текст для проверки скорости печати
    sample_text = "Привет, мир! Это пример текста для измерения скорости печати."
    
    print("Ваша задача — ввести следующий текст:")
    print(sample_text)
    input("Нажмите Enter, чтобы начать...")
    
    start = time()
    user_input = input("Введите текст: ")
    finish = time()
    
    # Вычисляем скорость печати (символов в минуту)
    speed = len(user_input) / (finish - start) * 60
    
    # Округляем результат до двух знаков после запятой
    rounded_speed = round(speed, 2)
    
    print(f"Скорость печати: {rounded_speed} символов в минуту")

# Запускаем программу
keyboard_train()