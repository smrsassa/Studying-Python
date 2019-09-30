###exercicio 54
maioridade = 0
for c in range(0, 7):
        idade = int(input('digite sua idade: '))
        if idade >= 18:
                maioridade = maioridade + 1
print ('tem {} maiores de idade nesse grupo'.format(maioridade))