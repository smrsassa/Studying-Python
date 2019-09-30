#exercicio88
import random
apostas = []
jogos = int(input('Quantos jogos vc quer fazer: '))
for c in range(1, jogos + 1):
    for p in range(1,6):
        num = random.randint(1, 60)
        while num in apostas:
            num = random.randint(1, 60)
        apostas.append(num)
    print (f'{c}° Jogo: {apostas}')
    apostas.clear()