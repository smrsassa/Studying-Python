#exercicio 57
se = str(input('Qual seu sexo [M/F]: ')).lower()
while se != 'm' and se != 'f':
    se = str(input('sexo invalido digite [M/F]: ')).lower()
print ('sexo escolhido foi {}'.format(se))