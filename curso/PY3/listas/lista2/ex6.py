#exercicio89
aluno = list()
lista = list()
while True:
    aluno.append(str(input('Nome: ')))
    aluno.append(float(input('nota: ')))
    aluno.append(float(input('2° nota: ')))
    lista.append(aluno[:])
    aluno.clear()
    end = str(input('Voce quer continuar? [S/N]')).strip().lower()
    if end in 'Nn':
        break
for c in range(0, len(lista)):
    print (f'[{c+1}] {lista[c][0]} média: {(lista[c][1]+lista[c][2])/2}')
while True:
    opc = str(input('Voce quer ver a nota individual de algum aluno? [S/N]')).strip().lower()
    if opc in 'Nn':
        break
    else:
        opc2 = int(input('qual o numero que pertencente ao aluno?'))
        print (f'O aluno {lista[opc2-1][0]} tem as notas {lista[opc2-1][1]} {lista[opc2-1][2]}')