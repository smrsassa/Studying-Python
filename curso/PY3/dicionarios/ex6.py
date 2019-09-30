#exercicio 95
desempenho = dict()
time = list()
gols = list()
totalgol = ind =0
while True:
    desempenho.clear()
    gols.clear()
    totalgol = 0
    desempenho['nome'] = str(input('Nome do jogador: '))
    partidas = int(input(f'Quantas partidas {desempenho["nome"]} jogou:'))
    for c in range(0, partidas):
        gols.append(int(input(f'Quantos gols {desempenho["nome"]} fez na partida {c+1}: ')))
        desempenho['gols'] = gols[:]
    for c2 in range(0, len(desempenho['gols'])):
        totalgol += desempenho['gols'][c2]
    desempenho['total'] = totalgol
    time.append(desempenho.copy())
    while True:
        end = str(input('Voce quer continuar: [S/N]')).strip().lower()
        if end in 'sn':
            break
    if end in 'n':
        break
print ('-='*30)
print ('O Desempenho do time foi:')
print ('-='*30)
for c in range (0, len(time)):
    print (f'{c} {str(time[c]["nome"]):.<10}{str(time[c]["gols"]):.>10}')
while ind != 999:
    ind = int(input('Quer ver o desempenho individual de algum jogador: [999 para parar]'))
    if ind > len(time) and ind != 999:
        print ('Erro, jogador não encontrado')
    else:
        print (time[ind])