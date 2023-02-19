"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""

with open("file2.txt") as my_file:
    content = my_file.readlines()
    print("Всего строк:", len(content))
    i = 0
    for line in content:
        i += 1
        words_list = line.split()
        print(f"Длина строки {i}: ", len(words_list))
