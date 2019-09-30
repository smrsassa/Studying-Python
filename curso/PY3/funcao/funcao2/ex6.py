#exercicio106
while True:
    def div_texto():
        print ('-='*40)


    div_texto()
    print ('Sistema de ajuda PyHELP')
    div_texto()
    opc = str(input('Digite a função aqui: '))
    if opc.lower() == 'fim':
        break
    else:
        help(opc)
