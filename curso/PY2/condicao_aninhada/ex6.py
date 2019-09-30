idade = int(input('digite sua idade: '))
if idade <= 9:
    print ('Categoria mirim')
elif idade <= 14 and idade > 9:
    print ('Categoria infantil')
elif idade <= 19 and idade > 14:
    print ('Categoria junior')
elif idade <= 20 and idade > 19:
    print ('Categoria senior')
else:
    print ('Categoria master')