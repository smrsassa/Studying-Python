#exercicio 63
termos = int(input('Quantos termos vc quer na sequencia de fibonacci? '))
c = 1
sequencia = 1
sequencia2 = 0
while c != termos:
    fi = (sequencia+sequencia2) - ((sequencia+sequencia2)-sequencia2)
    print ('{}'.format(fi), end='- ')
    sequencia += sequencia2
    sequencia2 = sequencia - sequencia2
    c += 1