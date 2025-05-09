'''
Анатолию в последний месяц удача улыбалась очень плохо. 
У него 3 раза взломали пароль. 
Вот он и задумался над тем, что неправильно подходит к вопросу составления паролей. 
Чтобы не напрягаться больше и опять не попасть впросак, 
молодой человек решил написать программу на Python, которая будет проверять его пароль на надежность. 
Требования к паролю у Анатолия следующие (он внимательно изучил рекомендации знатоков):
 1. Длина – 8 символов (если меньше – то проще взломать, а если длиннее – то сложно запомнить)
 2. В пароле должны быть:
    - заглавные буквы,
    - строчные символы,
    - числа
 3. специальные знаки - из перечня -#!№@#$%^& ()_-; - недопустимы, так как Анатолий их не может запомнить.
'''

def check_password(password):
    if len(password) != 8:
        return "Пароль должен быть длиной 8 символов."
    
    has_upper = False
    has_lower = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        else:
            return "Пароль содержит недопустимые символы."

    if has_upper and has_lower and has_digit:
        return "Пароль надежный."
    else:
        return "Пароль не удовлетворяет требованиям."

password = input("Введите пароль: ")
print(check_password(password))