#exercicio105
def notas(*n, sit = False):
    r = dict()
    r['total']=len(n)
    r['maior']=max(n)
    r['menor']=min(n)
    r['media']=sum(n)/len(n)
    if sit:
        if r['media']>7:
            r['situação']='Boa'
        else:
            r['situação']='Ruim'
    return r

resp = notas(5, 7, 3, 9, sit = True)
print(resp)