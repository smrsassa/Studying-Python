#exercicio 70
soma = milreais = maisbarato = prodbarato = compras = 0
print ('-'*60)
print ('Loja')
print ('-'*60)
while True:
    produto = str(input('Nome do produto: '))
    preço = int(input('Qual o preço? R$'))
    soma += preço
    compras += 1
    if preço > 1000:
        milreais += 1
    if compras == 1:
        maisbarato = preço
        prodbarato = produto
    elif preço < maisbarato:
        maisbarato = preço
        prodbarato = produto
    cont = str(input('Quer continuar? [S/N]'))
    if cont in 'Nn':
        break
print (f'O total gasto é R${soma}')
print (f'O produto mais barato foi {prodbarato} e custou {maisbarato}')
print (f'Teve {milreais} que custarau mais de R$1000')