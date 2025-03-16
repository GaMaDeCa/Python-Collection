#coding:latin-1

#github.com/GaMaDeCa
#Alguns Truques Básicos

#coding:latin-1 no inicio de um script python permite acentos latinos,
#dependendo da codificação, pode ser necessário trocar pelo coding:utf-8,
#que é mais universal

#Iterar uma array calculando o indice e limite
array=['Python','Truque','Programando']
limite=len(array)#=3
for i in range(10):
    #Código eliminada
    #if i>=len(array):
    #   i=0
    print(array[i%limite])#indice=0,1,2,0,1,2,0,1....

#Contar de 1 até 100(101) pulando de dois em dois com For Térnario
nones=[print(i)for i in range(1,101,2)]
#Essa lista 'nones' é o resultado que o print retorna(None) na lista do nosso for ternário

#Filtrar numeros com um For e If Ternário
texto='Testando 123Fim.'
texto=''.join([car for car in texto if not car.isdecimal()])
#''.join junta o texto com uma lista[de textos] adicionando entre os espaços o texto ''
print(texto)

#Operador Ternário(If Else)
idade=17
#Código eliminado
#if idade>=18:
#    print('Maior')
#else:
#    print('Menor')
print('Maior'if idade>=18 else'Menor')

#Ajustar texto com barras dentro de uma caixa
txt=input('Digite qualquer texto com menos de 50 caracteres:')
#if len...>50... raise Exception, etc
distancia=50
vazio='|'+'|'.rjust(distancia,'-')
topoEfundo=' '+''.rjust(distancia-1,'*')
print(topoEfundo)
print(vazio)
txt=txt.rjust(distancia//2+len(txt)//2,'-') #Distancia dividida por 2 mais tamanho do texto dividido por 2 = meio da tela
print('|'+txt+'|'.rjust(distancia-len(txt),'-'))
print(vazio)
print(topoEfundo)
#rjust adiciona caracteres na esquerda do texto, ljust faz o contrário, de padrao rjust(distancia) usa espaços ' ' como caractere padrão
