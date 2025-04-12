from time import time

def keyboard_train():
    start = time()
    text = input("Вводите текст для проверки скорости печати: ")
    finish = time()
    speed = len(text) / (finish - start)*60
    print(f"Скорость печати: {speed} символов в минуту")

keyboard_train()