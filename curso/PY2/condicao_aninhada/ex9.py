preço = int(input('Digite o proço do produto'))
print ('1 - A vista com 10/100 de desconto')
print ('2 - A vista no cartão com 5/100 de desconto')
print ('3 - 2x no cartão')
print ('4 - 3x com 30/100 de juros')
opc = int(input('Escolha uma opção'))
if opc == 1:
    preçof = preço * 0.9
    print ('O valor final vai ficar {}'.format(preçof))
elif opc == 2:
    preçof = preço * 0.95
    print ('O valor final vai ficar {}'.format(preçof))
elif opc == 3:
    parcela = preço/2
    print ('O valor final vai ficar 2 parcelas de {}'.format(parcela))
else:
    preçof = preço * 1.3
    parcela = preçof/3
    print ('O valor final vai ficar 3 parcelas de {}'.format(parcela))
print ('---FIM---')