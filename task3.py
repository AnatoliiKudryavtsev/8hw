"""
3) Создать(не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
translator = [['One', 'Один'], ['Two', 'Два'], ['Three', 'Три'], ['Four', 'Четыре'],
              ['Five', 'Пять'], ['Six', 'Шесть'], ['Seven', 'Семь']]

with open('file3.txt', 'r', encoding='utf-8') as data:
    lines = data.read()
    for i in range(len(translator)):
        lines = lines.replace(translator[i][0], translator[i][1])

with open('file4.txt', 'w', encoding='utf-8') as data:
    data.write(lines)
