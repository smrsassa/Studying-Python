###exercicio 53
t = str(input('digite uma palavra: ')).strip().lower()
lista = t.split()
juntos = ''.join(lista)
if juntos[::-1] in juntos:
        print('{} é um palindromo de {}'.format(juntos, juntos[::-1]))
else:
        print('{} não é um palindromo de {}'.format(juntos, juntos[::-1]))