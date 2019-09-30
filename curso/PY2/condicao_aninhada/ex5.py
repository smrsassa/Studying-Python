nota1 = float(input('digite sua nota: '))
nota2 = float(input('digite sua outra nota: '))
media = (nota1 + nota2)/2
if media < 5:
    print ('Reprovado')
elif media > 5 and media < 6.9:
    print ('Recuperação')
else:
    print ('Aprovado, aproveite as ferias')
print ('---FIM---')