nome = str(input('digite seu nome: ')).strip()
split = nome.split()
print ('seu primeiro nome é {}'.format(split[0]))
print ('seu ultimo nome é {}'.format(split[len(split)-1]))