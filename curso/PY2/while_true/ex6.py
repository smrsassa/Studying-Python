#exercicio 71
sobras10 = sobras1 = sobras20 = sobras5 = sobras = 0
print ('-'*60)
print ('{:^60}'.format('BANCO'))
print ('-'*60)
while True:
    dinheiro = int(input('Quanto você quer sacar? R$'))
    if dinheiro//50 != 0:
        print (f'Total de {dinheiro//50} cédulas de R$50')
        sobras = dinheiro - (dinheiro//50) * 50
    elif dinheiro//20 != 0:
        if dinheiro//20 != 0:
            print (f'Total de {dinheiro//20} cédulas de R$20')
            sobras20 = dinheiro - (dinheiro//20) * 20
    elif dinheiro//10 != 0:
        if dinheiro//10 != 0:
            print (f'Total de {dinheiro//10} cédulas de R$10')
            sobras10 = dinheiro - (dinheiro//10) * 10
    elif dinheiro//5 != 0:
        if dinheiro//5 != 0:
            print (f'Total de {dinheiro//5} cédulas de R$5')
            sobras5 = dinheiro - (dinheiro//5) * 5
    elif dinheiro//1 != 0:
        if dinheiro//1 != 0:
            print (f'Total de {dinheiro//1} cédulas de R$1')
            sobras1 = dinheiro - (dinheiro//1)
    if sobras//20 != 0:
        print (f'Total de {sobras//20} cédulas de R$20')
        sobras20 = sobras - (sobras//20) * 20
    elif dinheiro//10 != 0:
        if sobras//10 != 0:
            print (f'Total de {sobras//10} cédulas de R$10')
            sobras10 = sobras - (sobras//10) * 10
    elif dinheiro//5 != 0:
        if sobras//5 != 0:
            print (f'Total de {sobras//5} cédulas de R$5')
            sobras5 = sobras - (sobras//5) * 5
    elif dinheiro//1 != 0:
        if sobras//1 != 0:
            print (f'Total de {sobras//1} cédulas de R$1')
            sobras1 = sobras - (sobras//1)
    if sobras20//10 != 0:
        print (f'Total de {sobras20//10} cédulas de R$10')
        sobras10 = sobras20 - (sobras20//10) * 10
    elif dinheiro//5 != 0:
        if sobras20//5 != 0:
            print (f'Total de {sobras20//5} cédulas de R$5')
            sobras5 = sobras20 - (sobras20//5) * 5
    elif dinheiro//1 != 0:
        if sobras20//1 != 0:
            print (f'Total de {sobras20//1} cédulas de R$1')
            sobras1 = sobras20 - (sobras20//1)
    if sobras10//5 != 0:
        print (f'Total de {sobras10//5} cédulas de R$5')
        sobras5 = sobras10 - (sobras10//5) * 5
    elif dinheiro//1 != 0:
        if sobras10//1 != 0:
            print (f'Total de {sobras10//1} cédulas de R$1')
            sobras1 = sobras10 - (sobras10//1)
    if sobras5//1 != 0:
        print (f'Total de {sobras5//1} cédulas de R$1')
        sobras1 = sobras5 - (sobras5//1)
    cont = str(input('Quer sacar outra quantia? [S/N]'))
    if cont in 'Nn':
        break

##exercicio 71 Guanabara
#valor = int(input("informe o valor a ser sacado : "))
#nota50 = valor // 50
#valor %=  50
#nota20 = valor // 20
#valor %= 20
#nota10 = valor // 10
#valor %= 10
#nota1 = valor // 1
#print(f"notas de 50 = {nota50}")
#print(f"notas de 20 = {nota20}")
#print(f"notas de 10 = {nota10}")
#print(f"notas de 1 = {nota1}")
