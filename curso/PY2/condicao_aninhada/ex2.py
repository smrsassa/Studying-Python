print('''1-converter seu numero para binario
2-converter seu numero para octal
3-converter seu numero para hexadecimal''')
opc = int(input('escolha uma opção: '))
if opc == 1:
    print ('Voce escolheu a opção binario')
    num = int(input('digiti o numero desejado: '))
    print ('{} em binario é {}'.format(num, bin (num)[2:]))
elif opc == 2:
    print ('Voce escolheu a opção octal')
    num = int(input('digiti o numero desejado: '))
    print ('{} em binario é {}'.format(num, oct (num)[2:]))
elif opc == 3:
    print ('Voce escolheu a opção hexadecimal')
    num = int(input('digiti o numero desejado: '))
    print ('{} em binario é {}'.format(num, hex (num)[2:]))
else:
    print ('Erro...')
print ('---FIM---')