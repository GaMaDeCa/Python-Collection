from random import randint
valor=7
def gerarArrayEmSequencia(limite,inicio=1):return[(i,i2)for i,i2 in zip(range(inicio,limite),range(limite-1,-1+inicio,-1))]

def embaralharArray(array):
    for i in range(len(array)):
        i2=randint(0,len(array)-1)
        array[i],array[i2]=array[i2],array[i]
    return array

for n1,n2 in embaralharArray(gerarArrayEmSequencia(valor)):
    print(n1,n2)
