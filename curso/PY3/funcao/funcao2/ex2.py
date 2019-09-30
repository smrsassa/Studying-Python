#exercicio102
def fatorial(num=1, show=0):
    """
    -> Função fatorial
    param num: Numero determinado para calcular seu fatorial
    param show: Opção para mostrar ou não o calculo realizado
    """
    resultado = 1
    for c in range(num, 0, -1):
        resultado *= c
        if show:
            print(f'{c}', end=' ')
            if c > 1:
                print(f'x', end=' ')
            else:
                print(f'=', end=' ')
    return resultado


num = int(input('Voce quer saber o fatorial de qual numero? '))
show = str(input(f'Quer que eu mostre o calculo do fatorial de {num}? [S/N]')).strip().lower()
if 's' in show:
    show = True
else:
    show = False
print (fatorial(num, show))