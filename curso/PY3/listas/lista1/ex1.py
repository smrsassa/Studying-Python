#exercicio78
lista = []
for c in range (0, 5):
    valor = int(input(f'Digite um valor para a possição {c}: '))
    lista.insert(c, valor)
print (f'Voce digitou os valores {lista}')
print (f'O maior valor foi digitado foi {max(lista)} na possição {lista.index(max(lista))}')
print (f'O menor valor foi digitado foi {min(lista)} na possição {lista.index(min(lista))}')