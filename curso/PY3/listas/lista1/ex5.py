#exercicio82
lista = []
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    end = str(input('Quer continuar? [S/N]')).strip().lower()
    if end in 'Nn':
        break
pares = list()
impares = list()
for c in range(0, len(lista)):
    if lista[c] %2 == 0:
        pares.append(lista[c])
    else:
        impares.append(lista[c])
print (f'Voce digitou os valores {lista}')
print (f'Os valores pares na lista são {pares}')
print (f'Os valores impares na lista são {impares}')