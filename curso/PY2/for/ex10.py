###exercicio 55
maior = 0
menor = 0
for c in range(1,6):
        peso = int(input('qual é o peso da {}° pessoa: '.format(c)))
        if c == 1:
                maior = peso
                menor = peso
        else:
                if maior < peso:
                        maior = peso
                elif menor > peso:
                        menor = peso
print ('A pessoa mais pessada tem {}kg'.format(maior))
print ('A pessoa mais leve tem {}kg'.format(menor))
print ('Fim!!!')