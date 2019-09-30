import math
l1 = float(input('digite uma medida em cm: '))
l2 = float(input('digite outra medida em cm: '))
l3 = float(input('digite outra medida em cm: '))
if math.fabs(l3-l2) < l1 < l3+l2 and math.fabs(l1-l2) < l3 < l1+l2 and math.fabs(l3-l1) < l2 < l3+l1:
    print ('Com suas medidas é possivel formar um triangulo!')
    if l1 == l2 and l2 == l3:
        print ('Para ser mais especifico isso é um triangulo equilatero')
        print ('É um triangulo equilatero, pois possui todos os lados iguais')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print ('Para ser mais especifico isso é um triangulo isosceles')
        print ('É um triangulo isosceles, pois possui dois lados iguais')
    else:
        print ('Para ser mais especifico isso é um triangulo escaleno')
        print ('É um triangulo escaleno, pois não possui lados iguais')
else:
    print ('suas medidas não formam um triangulo!')
print ('---FIM---')