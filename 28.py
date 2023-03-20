# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# *Пример:*

# 2 2
#     4

A = int(input("Enter the first number "))
B = int(input("Enter the first number "))


def Sum_(A, B):
    if B == 0:
        return A
    A += 1
    B -= 1
    return Sum_(A, B)


print(Sum_(A, B))