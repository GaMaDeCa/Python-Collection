#coding:latin-1

class Ramo:#Node
 def __init__(n,valor,esquerda=None,direita=None):
  n.setValor(valor)       #int ou str
  n.setEsquerda(esquerda) #Node
  n.setDireita(direita)   #Node
 def getValor(n):return n.valor
 def getEsquerda(n):return n.esquerda
 def getDireita(n):return n.direita
 def setValor(n,valor):n.valor=valor
 def setEsquerda(n,esquerda):n.esquerda=esquerda
 def setDireita(n,direita):n.direita=direita

#Arvore Exemplo
#       5
#      / \
#     3   6
#    /   / \
#   2   7   8
#    \     / \
#     9   1   4
#              \
#               0
Arvore=Ramo(5,
        Ramo(3,
            Ramo(2,
                None,
                Ramo(9,None,None)
            ),
            None
        ),
        Ramo(6,
            Ramo(7,None,None),
            Ramo(8,
                Ramo(1,None,None),
                Ramo(4,None,
                    Ramo(0,None,None)
                )
            )
        )
)

#Contar ramos da arvore, somar os valores e criar uma array da arvore
soma=Arvore.getValor()
array=[[Arvore.getValor()]]
subarray=[]
e=Arvore.getEsquerda()
d=Arvore.getDireita()
ramos=[]
if e!=None:
    soma+=e.getValor()
    subarray.append(e.getValor())
    ramos.append(e)

if d!=None:
    soma+=d.getValor()
    subarray.append(d.getValor())
    ramos.append(d)

array.append(subarray)
contador=1+len(ramos) #Esquerda, direita e raiz
while ramos!=[]:
    subarray=[]
    novosRamos=[]
    for ramo in ramos:
        e=ramo.getEsquerda()
        d=ramo.getDireita()
        if e!=None:
            soma+=e.getValor()
            subarray.append(e.getValor())
            novosRamos.append(e)
            contador+=1
        if d!=None:
            soma+=d.getValor()
            subarray.append(d.getValor())
            novosRamos.append(d)
            contador+=1
    array.append(subarray)
    ramos=novosRamos

print(f'Arvore binaria tem {contador} ramos!\nA soma de seus valores é {soma}!')#10,45
for subarray in array:
    for item in subarray:
        print(f'{item} ',end='')
    print()
