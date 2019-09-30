#exercicio80
lista = []
for c in range(0, 5):
    valor = int(input('Digite um valor: '))
    if c == 0:
        lista.append(valor)
    for v in range(0, len(lista)):
        if lista[v] > valor:
            lista.insert(v, valor)
            break
    if lista[len(lista)-1] < valor and c != 0:
        lista.append(valor)
print(lista)
print ('Fim!!!')