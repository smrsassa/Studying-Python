###exercicio 72
extenso = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezzeseis', 'Dezzesete', 'Dezoito', 'Dezzenove', 'Vinte')
while True:
    numd = int(input('Digite um numero de 0 a 20:'))
    while numd < 0 or numd > 20:
        numd = int(input('Tente novamente. Digite um numero de 0 a 20:'))
    print (extenso[numd])
    fim = str(input('Deseja continuar?[S/N] ')).strip()
    if fim in 'Nn':
        break
print ('Fim!!!')