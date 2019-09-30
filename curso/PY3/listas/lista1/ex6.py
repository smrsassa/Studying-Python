#exercicio83
expressão = input('Digite a sua expressão: ')
pilha = []
for c in expressão:
    if c == '(':
        pilha.append('1')
    elif c == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append('1')
            break
if len(pilha) != 0:
    print ('expressão invalida')
else:
    print ('expressão valida')