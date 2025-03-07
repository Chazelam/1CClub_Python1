import random

def generate_password(length=12):
    if length < 4:
        print("Длина пароля должна быть не менее 4 символов.")
        return None

    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>?'
    password = ''
    password += random.choice('abcdefghijklmnopqrstuvwxyz')
    password += random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    password += random.choice('0123456789')
    password += random.choice('!@#$%^&*()_+-=[]{}|;:,.<>?')

    for i in range(length - 4):
        password += random.choice(characters)

    password = ''.join(random.sample(password, len(password)))
    return password

def password_generator():
    try:
        length = int(input("Введите длину пароля (по умолчанию 12): ") or 12)
        password = generate_password(length)
        if password:
            print(f"Ваш сгенерированный пароль: {password}")
    except ValueError:
        print("Введите корректное число.")

if __name__ == "__main__":
    password_generator()
