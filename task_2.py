# Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных файлах
# (в одном файлике отрывок из какой-то книги, а втором файлике — сжатая версия этого текста).


from itertools import count


#def compression(file):
#    data = open(file, 'r')
#    dataFile = ''
#    count = 1
#    coding = ''
#    cutoff = ''
#    for line in data:
#        dataFile += line
#    data.close
#    for char in dataFile:
#        if char != cutoff:
#            if cutoff:
#                coding += str(count) + cutoff
#
#            else:
#                count += 1


def compression(file):
    data = open(file, 'r')
    dataFile = ''
    count = 1
    coding = ''
    cutoff = ''
    for line in data:
        dataFile += line
    data.close

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
        return coding

f = 'txxt.txt'
a = compression(f)
print(a)