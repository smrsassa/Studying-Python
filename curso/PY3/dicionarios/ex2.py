#exercicio 91
import random
from operator import itemgetter
jogadas = dict()
ranking = dict()
for j in range(1, 5):
    jogadas[f'jogador {j}'] = random.randint(1,6)
for k,v in jogadas.items():
    print (f'{k} tirou {v} no dado.')
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse=True)
for i,v in enumerate(ranking):
    print (f'{i+1}° lugar {v[0]} rolou {v[1]} no dado')