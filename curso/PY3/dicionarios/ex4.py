#exercicio 93
desempenho = dict()
gols = list()
totalgol = 0
desempenho['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {desempenho["nome"]} jogou:'))
for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols {desempenho["nome"]} fez na partida {c+1}: ')))
    desempenho['gols'] = gols[:]
for c2 in range(0, len(desempenho['gols'])):
    totalgol += desempenho['gols'][c2]
desempenho['total'] = totalgol
print ('-='*30)
print (desempenho)
print ('-='*30)