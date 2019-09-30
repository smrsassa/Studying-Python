###exercicio 75
num1 = int(input('digite:'))
num2 = int(input('digite:'))
num3 = int(input('digite:'))
num4 = int(input('digite:'))
numdigitados = (num1, num2, num3, num4)
print (f'foram digitados {numdigitados.count(9)} o numero 9')
if 3 in numdigitados:
    print (f'O primeiro numero 3 esta no {numdigitados.index(3)+1}° possição')
else:
    print ('O numero 3 não foi digitado')
for c in range (0, 4):
    if numdigitados[c] %2 == 0:
        print (f'O numero {numdigitados[c]} é par')