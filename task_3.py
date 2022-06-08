# Создайте функцию, которая принимает строку и возвращает строку, зашифрованную с помощью Rot13.
# Если в строку включены числа или специальные символы, они должны быть возвращены как есть.
# Также создайте функцию, которая расшифровывает эту строку обратно (некий начальный аналог шифрования сообщений).


def codingRot13(string):
    stringCode = ''
    for char in string:
        buf = char.upper()
        if ord(buf) >= 65 and ord(buf) <= 90:
            if (ord(buf)+13) <= 90:
                stringCode += chr((ord(buf)+13))
            else:
                stringCode += chr((ord(buf)+13-90+65))
        else:
            stringCode += buf
    return stringCode

def decodingRot13(string):
    stringDecode = ''
    for char in string:
        buf = char.upper()
        if ord(buf) >= 65 and ord(buf) <= 90:
            if (ord(buf)-13) >= 65:
                stringDecode += chr((ord(buf)-13))
            else:
                stringDecode += chr((ord(buf)-13+90-65))
        else:
            stringDecode += buf
    return stringDecode




code = codingRot13('fdk;b; fgs kkg  ADfkk fs')
print(code)
decode = decodingRot13('SQX;O; STG XXT  NQSXX SG')
print(decode)