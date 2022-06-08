# Написать программу вычисления арифметического выражения заданного строкой. Используются операции +,-,/,*.
# приоритет операций стандартный. Функцию eval не использовать!
# Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
# Дополнительно: Добавить возможность использования скобок, меняющих приоритет операций.
# Пример: 1+2*3 => 7; (1+2)*3 => 9;


from copy import copy
from os import remove


def readFile(fileName):
    data = open(fileName, 'r')
    char = ''
    dataList = []
    for line in data:
        for item in line:
            if item.isnumeric():
                char += item
            else:
                dataList.append(char)
                dataList.append(item)
                char = ''
        dataList.append(char)
    data.close
    print(dataList)
    return dataList


def calculation(list):
    listBuf = copy(list)
    i = 0
    j = 0
    while i < len(list):
        if list[i] == '*':
            listBuf[j-1] = int(listBuf[j-1]) * int(list[i+1])
            listBuf.remove(list[i])
            listBuf.remove(list[i+1])
            i += 2
        elif list[i] == '/':
            listBuf[j-1] = int(listBuf[j-1]) / int(list[i+1])
            listBuf.remove(list[i])
            listBuf.remove(list[i+1])
            i += 2
        else:
            i += 1
            j += 1
    i = 0
    j = 0
    list = copy(listBuf)
    while i < len(list):
        if list[i] == '+':
            listBuf[j-1] = int(listBuf[j-1]) + int(list[i+1])
            listBuf.remove(list[i])
            listBuf.remove(list[i+1])
            i += 2
        elif list[i] == '-':
            listBuf[j-1] = int(listBuf[j-1]) - int(list[i+1])
            listBuf.remove(list[i])
            listBuf.remove(list[i+1])
            i += 2
        else:
            i += 1
            j += 1
    return int(listBuf[0])


file = 'txt.txt'
list = readFile(file)
res = calculation(list)
print(res)


#list = [1,2,3,4,5,'*',7]
# list.remove(list[6])
# print(list)
