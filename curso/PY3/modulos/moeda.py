def moeda(num=0):
    import locale
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    num = locale.currency(num, grouping=True, symbol=None)
    return 'R$'+num
def aumentar(num=0, aum = 100, m=True):
    num = num * (aum+100) / 100
    return num if not m else moeda(num)
def diminuir(num=0, dim = 0, m=True):
    num = num * (100 - dim) / 100
    return num if m is False else moeda(num)
def dobro(num=0, m=True):
    num = num * 2
    return num if m is False else moeda(num)
def metade(num=0, m=True):
    num = num/2
    return num if m is False else moeda(num)

def resumo(num, aum, dim):
    print('-'*30)
    print('Resumo do valor'.center(30))
    print('-'*30)
    print(f'Preço analisado: \t{moeda(num)}')
    print(f'Dobro do preço: \t{dobro(num)}')
    print(f'Metade do preço: \t{metade(num)}')
    print(f'{aum} de aumento:  \t{aumentar(num, aum)}')
    print(f'{dim} de desconto: \t{diminuir(num, dim)}')
    print('-'*30)