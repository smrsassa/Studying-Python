salario = int(input('digite seu salario: '))
preço = int(input('digite o valor da casa: '))
prest = int (input('em quanstas vezes vai pagar: '))
vprest = preço/prest
vnps = salario * 0.30
if vnps <= vprest:
    print ('A compra foi aprovada')
else:
    print ('Compra negada')