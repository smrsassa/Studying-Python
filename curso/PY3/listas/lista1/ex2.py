#exercicio79
lista = []
while True:
    valor = int(input('Digite um valor:'))
    if valor in lista:
        print ('Esse é um valor repitido')
    else:
        lista.append(valor)
    end = str(input('Quer continuar? [S/N]')).strip().lower()
    if end in 'Nn':
        break
lista.sort()
print (lista)