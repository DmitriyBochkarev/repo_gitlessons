# 2) Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить
# подсчет количества строк, количества слов в каждой строке.

with open('text2.txt') as my_f:
    content = my_f.readlines()
    print(f"Количество строк {len(content)}")
    my_f.seek(0)
    i = 0
    for line in my_f:
        i +=1
        print (f"Количество символов в {i} строке {len(line)}")

