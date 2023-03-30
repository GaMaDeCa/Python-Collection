#Calcula as diferencas entre os valores(se diminuiu ou aumentou), retornando uma array com lenght-1 em relacao a array inserida.
#Ex:
#   calcularDiferencas([5,3,6,2,-5,8,8,3])
#   Retorno>           [-2,3,-4,-7,13,0,-5]
def calcularDiferencas(array):return[array[i+1]-array[i]for i in range(len(array)-1)]
