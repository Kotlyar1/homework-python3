# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

print('Чтобы преобразовывать десятичное число в двоичное введите число! ')
num10 = int(input('Введите число: '))
print(f'Двоичное число через функцию bin: {bin(num10)}')

num2 = ''

while num10 > 0:
    num2 = str(num10 % 2) + num2
    num10 = num10 // 2

print(f'Двоичное число через цикл while: {num2}')