try:
    a=int(input('Numerador: '))
    b=int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Problema com os tipos de dados colocados')
except ZeroDivisionError:
    print('Não é possivel dividir por zero')
except KeyboardInterrupt:
    print('O usuario não digitou os dados')
except Exception as erro:
    print (f'Erro, inesperado? {erro.__cause__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre!')