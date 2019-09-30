nome = str(input('digite seu nome: ')).strip().lower()
print ('tem {} letra A no seu nome.'.format(nome.count('a')))
print ('o primeiro A esta na {}° posição'.format(nome.find('a')+1))
print ('a ultima letra A esta na {}° posição'.format(nome.rfind('a')+1))