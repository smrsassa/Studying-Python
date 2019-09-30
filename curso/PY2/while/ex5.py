#exercicio 61
numero = int(input('Digite um valor: '))
pa = int(input('Digite sua PA: '))
c = 0
while c != 10:
    numero = numero + pa
    print ('{}'.format(numero), end='- ')
    c += 1
print ('Fim!!!')