from time import sleep

def print_sale():
    text = "Акция! Распродажа выходного дня!"
    for symbol in text:
        print(symbol, end="")
        sleep(0.1)
    print()

print_sale()
