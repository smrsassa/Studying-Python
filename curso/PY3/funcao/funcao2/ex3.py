#exercicio103
def ficha(nome='<desconhecido>', gols = 0):
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    print(f'O jogador {nome} fez {gols} gols')


nome = str(input('Qual o nome do jogodor: ')).strip()
gols = str(input('Quantos gols ele fez? '))
if nome == '':
    ficha(gols = gols)
else:
    ficha(nome, gols)