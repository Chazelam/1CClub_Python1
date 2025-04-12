from random import randint

def lottery():
    win_ticket = randint(1, 1000000)
    if int(input("Номер билета: ")) == win_ticket:
        print("Автомобиль в студию!")

    else:
        print("Повезет в следующий раз!")

lottery()
