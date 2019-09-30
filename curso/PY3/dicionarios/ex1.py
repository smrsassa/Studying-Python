#exercicio 90
aluno = dict()
aluno['nome'] = str(input('Nome: ')).strip()
aluno['media'] = float(input(f'Qual a média de {aluno["nome"]}: '))
if aluno['media'] >= 7:
    aluno['situação'] = 'aprovado'
else:
    aluno['situação'] = 'reprovado'
print (f'O aluno {aluno["nome"]} com média de {aluno["media"]} foi {aluno["situação"]}')