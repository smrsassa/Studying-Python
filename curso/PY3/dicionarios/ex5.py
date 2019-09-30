#exercicio 94
pessoa = list()
mulheres = list()
acimamedia = list()
grupo  = dict()
c = totalidade = 0
while True:
    c += 1
    pessoa.append(str(input('Nome: ')))
    sexo = str(input('sexo [M/F]: ')).strip().lower()
    while True:
        if sexo in 'mf':
            pessoa.append(sexo)
            break
        else:
            print ('Por favor digite M ou F!!')
            sexo = str(input('sexo [M/F]: ')).strip().lower()
    if sexo == 'f':
        mulheres.append(pessoa[0])
    pessoa.append(int(input('idade: ')))
    totalidade += pessoa[2]
    media = totalidade/c
    grupo[f'pessoa{c}'] = pessoa[:]
    pessoa.clear()
    fim = str(input('Quer continuar? [S/N]')).strip().lower()
    if fim in 'Nn':
        break
media = totalidade/c
for k, v in grupo.items():
    if v[2] > media:
        acimamedia.append(v)
print (grupo)
print (f'foram cadastradas {c} pessoas')
print (f'A media de idade é {media}')
print (f'Mulheres cadastradas {mulheres}')
print (f'Pessoas com idade acima da media de idade {acimamedia}')