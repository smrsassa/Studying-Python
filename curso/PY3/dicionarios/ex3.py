#exercicio 92
from datetime import datetime
usuario = dict()
nome = str(input('Nome:'))
usuario['nome'] = nome
idade = int(input('Ano de nascimento: '))
idade = datetime.now().year - idade
usuario['idade'] = idade
cdt = int(input('Carteira de trabalho: (0 caso não tenha) '))
usuario['carteira de trabalho'] = cdt
if cdt != 0:
    anocontrato = int(input('Ano de contratação: '))
    usuario['ano de contratação'] = anocontrato
    salario = float(input('salario: '))
    usuario['salario'] = salario
    aposentadoria = idade + 35
    usuario['aposentadoria'] = aposentadoria
    print(f"""Nome tem valor {usuario["nome"]}\nidade tem o valor {usuario["idade"]}
ctps tem o valor {usuario["carteira de trabalho"]}\nano de contrato {usuario["ano de contratação"]}
salario tem o valor {usuario["salario"]}\naposentadoria tem o valor de {usuario["aposentadoria"]}""")
else:
    print(f'Nome tem valor {usuario["nome"]}\nidade tem o valor {usuario["idade"]}\nctps tem o valor {usuario["carteira de trabalho"]}')