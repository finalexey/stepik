import sys
import argparse
import os
import tempfile
import json


# функция парсера аргументов cmd
def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--key')  # , action='store_true', default=False)
    parser.add_argument('-v', '--value', default=False)  # , action='store_true', default=False)

    return parser

#функция добавления ключа и значения
def keyandval():
    if os.path.exists('test.txt'):
        with open('test.txt', 'r+') as file:
            print('файл открыт на запись&чтение без создания')
            checkdict = json.loads(file.read())
            print('словарь из файла до обновления: ', checkdict)

            if namespace.key not in checkdict:
                checkdict[namespace.key] = [namespace.value]
            else:
                checkdict[namespace.key].append(namespace.value)
            print('словарь после обновления: ', checkdict)
            file.truncate(0)
            file.seek(0)
            file.write(json.dumps(checkdict))

    else:
        with open('test.txt', 'w') as file:
            print('файл создан')
        with open('test.txt', 'r+') as file:
            print('файл открыт на запись&чтение')
            print(namespace.key, namespace.value)
            checkdict = dict()
            checkdict[namespace.key] = [namespace.value]
            print('словарь после обновления: ', checkdict)
            file.truncate(0)
            file.seek(0)
            file.write(json.dumps(checkdict))

#функция извлечения по ключу
def onlykey():
    if os.path.exists('test.txt'):
        with open('test.txt', 'r+') as file:
            print('файл открыт на запись&чтение без создания')
            checkdict = json.loads(file.read())
            try:
                print(*checkdict[namespace.key])
            except KeyError:
                print(None)
    else:
        print('файл не был создан')



if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args()

    print(namespace)
    print('чтение аргументов')
    if namespace.key != False and namespace.value != False:
        print('ключ и значение введены: ', namespace.key + ':' + namespace.value)
        keyandval()
    elif namespace.key != False and namespace.value == False:
        print('ключ введен: ', namespace.key)
        onlykey()

