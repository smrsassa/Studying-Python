#exercicio 59
numero1 = int(input('digite um numero: '))
numero2 = int(input('digite um numero: '))
print ("""O que vc deseja fazer\n[1]Somar\n[2]Multiplicar\n[3]Saber o maior
[4]Digitar outros valores\n[5]Sair do programa""")
opc = int(input('Digite a opção desejada: '))
while opc != 5:
    if opc == 1:
        print ('A soma de {} e {} é igual a {}'.format(numero1, numero2, numero1+numero2))
    elif opc == 2:
        print ('A multiplicação de {} vezes {} é igual a {}'.format(numero1, numero2, numero1*numero2))
    elif opc == 3:
        if numero1 > numero2:
            print ('{} é maior do que {}'.format(numero1, numero2))
        elif numero2 > numero1:
            print ('{} é maior do que {}'.format(numero2, numero1))
        elif numero1 == numero2:
            print ('Os numeros digitados são iguais')
    elif opc == 4:
        print ('Os valores atuais são {}, {}'.format(numero1, numero2))
        numero1 = int(input('digite um numero: '))
        numero2 = int(input('digite um numero: '))
    opc = int(input('O que vc quer fazer agora? '))
print ('Fim!!!')