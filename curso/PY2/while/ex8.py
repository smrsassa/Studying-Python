#exercicio 64
num = 0
soma = 0
numdigitados = 0
while num != 999:
    num = int(input('Digite um numero: '))
    if num != 999:
        soma += num
        numdigitados += 1
print ('A soma de {} numeros digitados foi {}'.format(numdigitados, soma))