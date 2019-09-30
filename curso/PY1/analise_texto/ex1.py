import time
nome = str(input('digite seu nome'))
print ('analisando seu nome...')
time.sleep(3)
print ('nome em maiuscula: {}'.format(nome.upper()))
print ('nome em maiuscula: {}'.format(nome.lower()))
split1 = nome.split()
print ('quantas letras tem seu nome: {}'.format(len(''.join(split1))))
print ('seu primeiro nome é: {}'.format(split1[0]))