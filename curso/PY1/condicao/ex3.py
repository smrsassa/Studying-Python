v = int(input('A que velocidade vc esta? '))
if v>=80:
    multa = (v-80)*7    
    print ('vc foi multado em R${}!'.format(multa))
else:
    print ('vc esta dentro da velocidade permitida')