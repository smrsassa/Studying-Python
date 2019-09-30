#exercicio84
galera = []
dado = []
cadastros = maxpeso = minpeso = 0
nomemaxp = nomeminp = ''
while True:
    dado.append(str(input('Nome :')))
    dado.append(int(input('peso :')))
    galera.append(dado[:])
    dado.clear()
    if len(galera) == 1:
        maxpeso = galera[0][1]
        minpeso = galera[0][1]
        nomemaxp = galera[0][0]
        nomeminp = galera[0][0]
    elif maxpeso < galera[len(galera)-1][1]:
        maxpeso = galera[len(galera)-1][1]
        nomemaxp = galera[len(galera)-1][0]
    elif minpeso > galera[len(galera)-1][1]:
        minpeso = galera[len(galera)-1][1]
        nomeminp = galera[len(galera)-1][0]
    cadastros += 1
    end = str(input('Voce quer continuar? [S/N]')).strip().lower()
    if end in 'Nn':
        break
print (f'Foram cadastradas {cadastros} pessoas')
print (f'A pessoa mais pessada é {nomemaxp} com {maxpeso}Kg')
print (f'A pessoa mais leve é {nomeminp} com {minpeso}Kg')