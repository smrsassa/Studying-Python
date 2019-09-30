#exercicio 65
opc = ''
c = soma = maiornum = menornum = 0
while opc in'Ss':
    num = int(input('Digite um numero: '))
    c += 1
    soma += num
    if c == 1:
        maiornum = num
        menornum = num
    elif num > maiornum:
        maiornum = num
    elif num < menornum:
        menornum = num
    opc = str(input('Quer continuar[S/N]? ')).lower().strip()[0]
print ('A media dos numeros é {:.2f}'.format(soma/3))
print ('O maior numero é {} e o menor é {}'.format(maiornum, menornum))