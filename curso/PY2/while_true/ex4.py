#exercicio 69
homems = mulheresvinte = dezoito = 0
while True:
    print ('-'*60)
    print ('Cadastre uma pessoa')
    print ('-'*60)
    idade = int(input('Qual sua idade: '))
    sexo = str(input('Qual seu sexo: [M/F] '))
    print ('-'*60)
    if sexo in 'Mm':
        homems += 1
    elif sexo in 'Ff' and idade < 20:
        mulheresvinte += 1
    if idade > 18:
        dezoito += 1
    cont = str(input('Quer continuar? [S/N]'))
    if cont in 'Nn':
        break
print (f'Tem {homems} homems cadastrados')
print (f'Tem {mulheresvinte} mulheres com menos de 20 anos cadastradas')
print (f'Tem {dezoito} pessoas com mais de 18 anos cadastrados')