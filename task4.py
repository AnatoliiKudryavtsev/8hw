"""
4) Задание на закрепление знаний по модулю json. Есть файл orders
в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
его заполнение данными.
Для этого:
Создать функцию write_order_to_json(), в которую передается
5 параметров — товар (item), количество (quantity), цена (price),
покупатель (buyer), дата (date). Функция должна предусматривать запись
данных в виде словаря в файл orders.json. При записи данных указать
величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json()
с передачей в нее значений каждого параметра.
ПРОШУ ВАС НЕ УДАЛЯТЬ ИСХОДНЫЙ JSON-ФАЙЛ
ПРИМЕР ТОГО, ЧТО ДОЛЖНО ПОЛУЧИТЬСЯ
{
"orders": [
{
"item": "принтер",
"quantity": "10",
"price": "6700",
"buyer": "Ivanov I.I.",
"date": "24.09.2017"
},
{
"item": "scaner",
"quantity": "20",
"price": "10000",
"buyer": "Petrov P.P.",
"date": "11.01.2018"
},
]
}
вам нужно подгрузить JSON-объект
и достучаться до списка, который и нужно пополнять
а потом сохранять все в файл
"""
import json


def write_order_to_json(item, quantity, price, buyer, date):
    with open("orders.json", 'w', encoding='utf-8') as j_file:
        order_list.append({
            "item": item,
            "quantity": quantity,
            "price": price,
            "buyer": buyer,
            "date": date
        })
        json.dump({"orders": order_list}, j_file)


try:
    with open("orders.json", 'r', encoding='utf-8') as jsonfile:
        orders = json.load(jsonfile)
except IOError:
    print('Сохраненных заказов нет!')
    order_list = []
else:
    order_list = list(orders.get("orders"))

while input('Добавить заказ? (1-да): ') == '1':
    write_order_to_json(input('Ведите название товара: '),
                        input('Ведите количество: '),
                        input('Ведите цену товара: '),
                        input('Ведите покупателя: '), input('Ведите дату: '))
print(order_list)
