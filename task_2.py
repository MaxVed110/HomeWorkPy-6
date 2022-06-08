# Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных файлах
# (в одном файлике отрывок из какой-то книги, а втором файлике — сжатая версия этого текста).


from itertools import count


def compression(file):  # разобраться!!!
    data = open(file, 'r')
    dataFile = ''
    for line in data:
        dataFile += line
    data.close
    
    count = 1
    coding = ''
    cutoff = ''
    for char in dataFile:
        if char != cutoff:
            if cutoff:
                coding += str(count) + cutoff
            count = 1
            cutoff = char
        else:
            count += 1
    else:
        coding += str(count) + cutoff

    data = open('Coding.txt', 'w')
    data.writelines(coding)
    data.close


def regain(file):
    data = open(file, 'r')
    for line in data:
        dataFile = [char for char in line]
    data.close
    decoding = ''
    char = ''
    for i in range(len(dataFile)):
        if dataFile[i].isnumeric():
            char += dataFile[i]
        else:
            decoding += dataFile[i] * int(char) 
            char =''
    data = open('Decoding.txt', 'w')
    data.writelines(decoding)
    data.close


fileForCoding = 'txtTask_2.txt'
compression(fileForCoding)
fileForDecoding = 'Coding.txt'
regain(fileForDecoding)
