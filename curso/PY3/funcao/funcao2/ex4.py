#exercicio104
def leiaInt(n):
    strin = str(input(f'{n}')).strip()
    while True:
        if strin == '':
            print('ERRO! Invalido')
            strin = str(input(f'{n}')).strip()
        else:
            if strin.isnumeric():
                strin = int(strin)
                break
            else:
                print('ERRO! Invalido')
                strin = str(input(f'{n}')).strip()
    return strin


n = leiaInt('Digite um numero inteiro: ')
print (f'Voce digitou o numero {n}')