#exercicio 98
from time import sleep
def contador(i, e, p):
    print ('-' * 30)
    for c in range(i, e, p):
        print (f'{c}', end = ' ')
        sleep(0.5)
    print ('')


contador(1, 10, 1)
contador(10, 0, -2)
start = int(input('Digite o numero de partida: '))
end = int(input('Digite o numero em que deseja chegar: '))
passo = int(input('Digite o numero de passo: '))
if start > end and passo > 0:
    passo *= -1
if passo == 0:
    passo += 1
contador(start, end, passo)