#Retorna uma tupla contendo o valor maximo e o minimo encontrado na array.
#findMaxMin([3,4,5,7,2,9,4,3])
# (9,2)
def findMaxMin(array):
    MAX=array[0]
    MIN=array[0]
    for num in array:
        if num>MAX:MAX=num
        if num<MIN:MIN=num
    return(MAX,MIN)
