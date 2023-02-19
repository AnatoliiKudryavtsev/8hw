"""
1. Создать программно файл в текстовом формате,
записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

while True:
    input_file_1 = input("Введите данные для записи в файл или введите пустую строку для завершения >>>")
    if input_file_1 != "":
        try:
            with open("file1.txt", "a") as my_file:
                print(input_file_1, file=my_file)
        except IOError:
            print("IOError")
    else:
        break
