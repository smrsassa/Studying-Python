d = int(input('Qual a distancia da sua viagem? '))
if d<=200:
    p = d*0.5
    print ('O preço da sua viagem é de R${}'.format(p))
else:
    p = d*0.45
    print ('O preço da sua viagem é de R${}'.format(p))