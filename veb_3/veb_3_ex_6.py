# 6) Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и
# возвращающую его же, но с прописной первой буквой. Например, print(int_func(‘text’)) ->
# Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов,
# разделенных пробелом. Каждое слово состоит из латинских букв в нижнем регистре. Сделать
# вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо
# использовать написанную ранее функцию int_func().


def int_func(x):
    word_list = list(x)
    return word_list[0].upper() + x[1:]
word = input ("Введите слово из маленьких букв ")
print (int_func(word))
string = input ("Введите строку из нескольких слов ")
str_list = string.split(" ")
str_join = []
for i in str_list:
    str_join.append(int_func(i))
print (" ".join(str_join))