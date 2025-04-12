from random import randint

def guess_number():
    win_number = randint(1, 10)
    user_number = int(input("Введите число: "))
    while user_number != win_number:
        print("Неверно", end=" ")
        if user_number > win_number:
            print("Ваше число больше!")
        else:
            print("Ваше число меньше!")

        user_number = int(input("Введите число: "))
    print("Поздравляем! Победа! \nВы отгадали число!")


guess_number()