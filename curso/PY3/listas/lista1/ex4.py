#exercicio81
lista = []
while True:
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    end = str(input('Quer continuar? [S/N]')).strip().lower()
    if end in 'Nn':
        break
print (f'Foram digitados {len(lista)} numeros')
lista.sort(reverse=True)
print (f'A lista em ordem decrecente {lista}')
if 5 in lista:
    print (f'A lista possui numero 5')
else:
    print (f'A lista não possui o numero 5')