#exercicio 66
c = soma = 0
while True:
    num = int(input('Digite um numero: '))
    print ('(digite 999 quando acabar)')
    if num == 999:
        break
    c += 1
    soma += num
print (f'Foram digitados {c} e a soma entre eles é {soma}')