import math
l1 = float(input('digite uma medida em cm: '))
l2 = float(input('digite outra medida em cm: '))
l3 = float(input('digite outra medida em cm: '))
if math.fabs(l3-l2) < l1 < l3+l2 and math.fabs(l1-l2) < l3 < l1+l2 and math.fabs(l3-l1) < l2 < l3+l1:
    print ('com suas medidas é possivel formar um triangulo!')
else:
    print ('suas medidas não formam um triangulo!')