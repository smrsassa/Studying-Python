#exercicio87
matriz = [[0, 0, 0,], [1, 1, 1,], [2, 2, 2,]]
somapares = 0
somaterceira = 0
for c in range(0, 3):
    for c2 in range(0,3):
        valor = int(input(f'preencha a celula [{c, c2}] da matriz: '))
        if valor %2 == 0:
            somapares += valor
        if c == 2:
            somaterceira += valor
        if c == 1:
            if valor > matriz[1][c2]:
                maxsegunda = valor
        matriz[c][c2] = valor
print ('-='*50)
print (matriz[0])
print (matriz[1])
print (matriz[2])
print ('-='*50)
print (f'A soma dos valores pares digitados = {somapares}')
print (f'A soma dos valores na terceira coluna = {somaterceira}')
print (f'O maior valor da segunda coluna = {maxsegunda}')