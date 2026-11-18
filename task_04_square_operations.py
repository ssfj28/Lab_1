# Задача 4. Сумма, разность, произведение и частное квадратов двух чисел.
# По условию оба числа должны быть ненулевыми.

# Ввод исходных данных.
a = float(input("Введите первое ненулевое число a: "))
b = float(input("Введите второе ненулевое число b: "))

# Вычисление квадратов чисел.
a_squared = a ** 2
b_squared = b ** 2

# Выполнение арифметических операций с квадратами.
square_sum = a_squared + b_squared
square_difference = a_squared - b_squared
square_product = a_squared * b_squared
square_quotient = a_squared / b_squared

# Вывод результатов.
print("Сумма квадратов =", square_sum)
print("Разность квадратов =", square_difference)
print("Произведение квадратов =", square_product)
print("Частное квадратов =", square_quotient)
