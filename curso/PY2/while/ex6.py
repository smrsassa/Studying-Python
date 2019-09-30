#exercicio 62
numero = int(input('Digite um valor: '))
pa = int(input('Digite sua PA: '))
termos = 10
while termos != 0 :
    c = 0
    while c != termos:
        numero = numero + pa
        print ('{}'.format(numero), end='- ')
        c += 1
    print ('Acabou\n')
    termos = int(input('Deseja mostrar mais quantos termos?'))
print ('Fim!!!')