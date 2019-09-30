#exercicio 99
def maior(*num):
    maior = 0
    l = len(num)
    if l == 0:
        print ('-=' * 30)
        print ('Não tem nenhum valor na lista')
    else:
        print ('-=' * 30)
        for valor in num:
            print (f'{valor}', end = ' ')
            if valor > maior:
                maior = valor
        print (f'foram informados {l} valores e o maior é {maior}')


maior(2, 4, 5, 7, 9)
maior(2)
maior(2, 4)
maior()