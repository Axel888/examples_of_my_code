# Квадрат и куб
# Давайте составим сводную информацию о квадратах и кубах интервала чисел.
# В программу входит два натуральных числа a и b (гарантируется, что a <b),
# после чего для каждого целого числа на интервале от a до b необходимо
# вывести фразу следующего вида:

# «Число {число}; его квадрат = {квадрат}; его куб = {куб} »

# Кавычки выводить не нужно и пользуйтесь f-строкой.

# Формат входных данных
# На вход предлагается программа два натуральных числа a и b, каждой отдельной отдельной.
# Формат выходных данных
# Программа должна вывести текст в соответствии с условием задачи.

# Решение:

a, b = int (input ()), int (input ())
для i в диапазоне (a, b + 1):
print (f '' 'Число {i}; его квадрат = {i 2}; его куб = {я 3} '' ')

# (ф-строки, классный инструмент!)
