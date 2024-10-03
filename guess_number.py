from random import randint

number = randint(1, 10)
print('Угадай число от 1 до 101')
while True:
    guess = int(input('Введи число: '))
    if guess > number:
        print('Введенное число больше')
    elif guess < number:
        print('Введенное число меньше')
    else:
        print('Угадал!')
        break
print('Отличная интуиция!!!')