#exercicio86
matriz = [[0, 0, 0,], [1, 1, 1,], [2, 2, 2,]]
for c in range(0, 3):
    for c2 in range(0,3):
        valor = int(input(f'preencha a celula [{c, c2}] da matriz: '))
        matriz[c][c2] = valor
print (matriz[0])
print (matriz[1])
print (matriz[2])