# 5) Реализовать формирование списка, используя функцию range() и возможности генератора. В
# список должны войти четные числа от 100 до 1000 (включая границы). Необходимо получить
# результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce
def my_func(prev_el, el):
    # prev_el - предыдущий элемент
    # el - текущий элемент
    return prev_el * el

list_1 = [ i for i in range (100, 1001, 2)]
print(reduce(my_func, list_1))