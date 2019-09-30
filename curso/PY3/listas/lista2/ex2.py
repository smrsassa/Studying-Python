#exercicio85
dados = []
lista = []
lista.append(dados[:])
lista.insert(0, dados[:])
for c in range(0, 7):
    dados.append(int(input('Digite um valor: ')))
    if dados[c] %2 == 0:
        lista[0].insert(0, dados[c])
    else:
        lista[1].insert(0, dados[c])
lista[0].sort()
lista[1].sort()
print (f'Os valores pares digitados foram {lista[0]}')
print (f'Os valores impares digitados foram {lista[1]}')