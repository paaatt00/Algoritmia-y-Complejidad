def inverseNumber(n):
    numberInv = ''
    if (int(n/10) == 0):
        numero = str(n%10);
        numberInv += numero
    else:
        numero = str(n%10);
        numberInv += numero + inverseNumber(int(n/10))
    return numberInv

print(inverseNumber(678))

