# Найдите сумму цифр трехзначного числа.
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

input_number = int(input("Введите число: "))
first_number = input_number % 10
last_two_numbers = input_number // 10
second_number = last_two_numbers % 10
last_number = last_two_numbers // 10
print (f'Сумма трёх чисел равна: {first_number+second_number+last_number}')