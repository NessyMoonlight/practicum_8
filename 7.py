n = input('Введите число: ')
if n.isdigit():
    print(f'Введено целое число: {n}')
else:
    while not n.isdigit():
        n = input('Ошибка. Попробуйте еще раз. Введите число: ')
    print(f'Введено целое число: {n}')