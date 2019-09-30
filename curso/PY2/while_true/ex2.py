#exercicio 67
while True:
    tabuada = int(input('Voce quer ver a tabuada de qual numero? '))
    print ('='*60)
    for c in range (1, 11):
        print (f'{tabuada} x {c} = {tabuada*c}')
    print ('='*60)
    if tabuada < 0:
        break