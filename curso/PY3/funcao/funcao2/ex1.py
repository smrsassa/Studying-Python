#exercicio101
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} o voto é proibido'
    elif idade >= 16 and idade < 18 or idade > 65:
        return f'Com {idade} o voto é opcional'
    else:
        return f'Com {idade} o voto é obrigatorio'
        
ano = int(input('Qual o ano do seu nascimento? '))
print(voto(ano))