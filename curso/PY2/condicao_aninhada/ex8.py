altura = float(input('Digite sua altura em metros'))
peso = float(input('Digite seu peso em Kg'))
imc = (altura * altura)/peso
if imc < 18.5:
    print ('Abaixo do peso')
elif imc < 25 and imc >= 18.5:
    print ('Peso ideal')
elif imc < 30 and imc >= 25:
    print ('Sobrepeso')
elif imc < 40 and imc >= 30:
    print ('Obesidade')
else:
    print ('Obesidade morbida')