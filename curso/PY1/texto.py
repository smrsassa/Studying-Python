###fatiando###
frase=('aprendendo a programar')
#pegando o 13 caractere | frase[13] |
print('{}'.format(frase[13]))
#pegando do 13 até 21 | frase[13:21] |
print('{}'.format(frase[13:21]))
#pegando do 13 até 21 pulando de 2 em 2 | frase[13:21:2] |
print('{}'.format(frase[13:21:2]))
#pegando do caracter 0 até o 5 | frase[:5] |
print('{}'.format(frase[:5]))
#pegando do caracter 5 até o final | frase[5:] |
print('{}'.format(frase[5:]))
#pegando do caracter 5 até o final pulando 3 em 3 | frase[5::3] |
print('{}'.format(frase[5::3]))

###Analise###
# Comprimento/conta os caracteres 1,2,3 ... | len(frase) |
len(frase)
#contar quantas vezes aparece determinada letra | frase.count('a') |
frase.count('a')
#contar quantas vezes aparece determinada letra em determinado local | frase.count('a', 0, 10) |
frase.count('a', 0, 10)
#procura na frase o conjunto de letras | frase.find('pro') |
#se procurar algo q n tenha na frase ira retornar o valor -1
frase.find('pro')
#verificar se existe o que esta procurando na frase | 'aprendendo' in frase |
'aprendendo' in frase

###Transformação###
#reposicionar | frase.replace('aprendendo', 'ensinando') |
frase.replace('aprendendo', 'ensinando')
#caso vc queira salvar seu replace | frase = frase.replace('aprendendo', 'ensinando') |
frase = frase.replace('aprendendo', 'ensinando')
#trocar todas as letra minusculas por maiusculas | frase.upper() |
frase.upper()
#trocar todas as letra maiusculas por minusculas | frase.lower() |
frase.lower()
#pega toda a str e coloca todas as letra em minusculas e deixa somente a primeira em maiuscula | frase.capitalize() |
frase.capitalize()
#pega a primeira letra de cada palavra e deixa ela maiuscula | frase.title() |
frase.title()
#remove os espaços inuteis | frase.strip() |
#tem tb o rstrip que remove os espaços da direita e tb tem o l strip que remove os da esqueda
frase2=('   aprenda python   ')
frase2.strip()

###divisão###
#divide sua frase de acordo com os espaços dados | frase.split() |
frase.split()
#dividido = frase.split()
#print (dividido[2][3]) 
###Junção###
#junta as palavras | '-'.join.(frase)
j = '-'
print (j.join(frase))
######frase.upper().count('o')
