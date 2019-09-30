#exercicio 100
import random
def sorteia(lista):
    for c in range(0, 5):
        numeros.append(random.randint(1, 10))
    print (f'Os valores sorteados foram {numeros}')
def somapar(lesta):
    soma = 0
    for valores in numeros:
        if valores %2 == 0:
            soma += valores
    print (f'A soma dos valores pares da lista é {soma}')


numeros = list()
sorteia(numeros)
somapar(numeros)