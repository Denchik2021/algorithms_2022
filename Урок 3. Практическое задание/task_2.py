"""
Задание 2.

Ваша программа должна запрашивать пароль
Для этого пароля вам нужно вычислить хеш, используя алгоритм sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно и вновь вычислить хеш
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921
f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Важно: для хранения хеша и соли воспользуйтесь или файлом (CSV, JSON)
или, если вы уже знаете, как Python взаимодействует с базами данных,
воспользуйтесь базой данный sqlite, postgres и т.д.
п.с. статья на Хабре - python db-api
"""

import hashlib
import csv


def passwordhash(password):
    pass_hash = hashlib.sha256('bigbigsalt'.encode('utf-8') + password.encode('utf-8')).hexdigest()
    print(pass_hash)
    return pass_hash


def auth():
    pass_one = input('Введите пароль: ')
    pass_two = input('Введите пароль снова: ')
    pas1 = passwordhash(pass_one)
    pas2 = passwordhash(pass_two)
    if pas1 == pas2:
        with open('data.csv', 'w') as file:
            write = csv.writer(file)
            write.writerow([pas2])
        return 'Пароли идентичны и записаны в файл'
    else:
        return 'Пароли не совпадают'


print(auth())
