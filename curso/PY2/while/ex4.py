#exercicio 60
numero = int(input('Digite um valor: '))
fatorial = 2
resultado = 1
while fatorial <= numero:
    resultado = resultado * fatorial
    fatorial = fatorial + 1
print ('O fatorial de {} é igual a {}'.format(numero, resultado))