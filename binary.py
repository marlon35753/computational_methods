#!/usr/bin/env python3
def binary(z):
    print(__name__)
    b = ''
    while z // 2 != 0:
        b = str(z % 2) + b
        z = z // 2
    return str(z) + b
    
if __name__=='__main__':
    number = int(input('Digita un número: '))
    binary_8b = binary(number)
    print('Su representación binaria es: ' + binary_8b.zfill(8))
