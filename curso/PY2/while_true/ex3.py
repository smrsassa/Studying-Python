#exercicio 68
import random
soma = vitorias = 0
while True:
    num = int(input('Digite um numero: '))
    aposta = str(input('Par ou impar? [P/I]')).strip()[0]
    pcaposta = random.randint(1, 10)
    if aposta in 'Pp':
        soma = num + pcaposta
        if soma%2 == 0:
            print (f'Voce venceu {soma} é par')
            vitorias += 1
        else:
            print (f'Voce perdeu {soma} é impar')
            break
    elif aposta in 'Ii':
        soma = num + pcaposta
        if soma%2 == 0:
            print (f'Voce perdeu {soma} é par')
            break
        else:
            print (f'Voce venceu {soma} é impar')
            vitorias += 1
    else:
        print ('Comando invalido, digite novamente.')
print (f'Voce venceu {vitorias} seguidas!!!')