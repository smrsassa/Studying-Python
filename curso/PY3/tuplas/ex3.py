###exercicio 74
import random
sorteio = (random.randint(0, 10),random.randint(0, 10),random.randint(0, 10),random.randint(0, 10),random.randint(0, 10))
print (sorteio[0], sorteio[1], sorteio[2], sorteio[3], sorteio[4])
print (f'O menor numero é {sorted(sorteio)[0]}')
print (f'O maior numero é {sorted(sorteio)[4]}')