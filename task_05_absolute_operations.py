# Задача 5. Сумма, разность, произведение и частное модулей двух чисел.
# По условию оба числа должны быть ненулевыми.

# Ввод исходных данных.
a = float(input("Введите первое ненулевое число a: "))
b = float(input("Введите второе ненулевое число b: "))

# Вычисление модулей чисел.
abs_a = abs(a)
abs_b = abs(b)

# Выполнение арифметических операций с модулями.
absolute_sum = abs_a + abs_b
absolute_difference = abs_a - abs_b
absolute_product = abs_a * abs_b
absolute_quotient = abs_a / abs_b

# Вывод результатов.
print("Сумма модулей =", absolute_sum)
print("Разность модулей =", absolute_difference)
print("Произведение модулей =", absolute_product)
print("Частное модулей =", absolute_quotient)
