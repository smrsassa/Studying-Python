salario = int(input('seu salario'))
if salario<=1250:
    aumento = salario*1.15
    print ('salario com aumento {:.2f}'.format(aumento))
else:
    aumento = salario*1.1
    print ('salario com almento {:.2f}'.format(aumento))