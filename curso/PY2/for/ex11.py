###exercicio 56
mediai = 0
homemvelho = ''
ihomemvelho = 0
fmenor = 0
for p in range (1,5):
        print ("----- {}° Pessoa -----".format(p))
        nomes = str(input('Qual seu nome: ')).strip()
        idade = int(input('Qual sua idade: '))
        sexo = str(input('Sexo [M/F]: ')).strip()
        mediai = mediai + idade
        if p == 1 and sexo in 'Mm':
                homemvelho = nomes
                ihomemvelho = idade
        if sexo in 'Mm' and idade > ihomemvelho:
                homemvelho = nomes
                ihomemvelho = idade
        if sexo in 'Ff' and idade < 20:
                fmenor += 1
print ('A media de idade do grupo é {}'.format(mediai/4))
print ('O homem mais velho tem {} anos e se chama {}'.format(ihomemvelho, homemvelho))
print ('No grupo tem {} mulheres com menos de 20 anos'.format(fmenor))