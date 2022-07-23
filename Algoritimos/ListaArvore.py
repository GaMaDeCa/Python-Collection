#coding:latin-1

# TreeView List - Gabriel Matheus de Castro

def listaArvore(lista,espaco=' '):
    for item in lista:
        if type(item)==list:
            listaArvore(item,espaco*2) # Para ficar mais colado, troque espaco*2) por espaco+espaco)
        else:
            print(f'{espaco}{item}')

lista_exemplo=['Arvore 1',[f'SubArvore {i}' for i in range(1,6)],'Arvore 2',['SubArvore 1',['SubSubArvore 1','SubSubArvore 2',['SubSubSubArvore 1']]]]

print('Estilo 1')
listaArvore(lista_exemplo)
# Saída:
# Arvore 1
#  SubArvore 1
#  SubArvore 2
#  SubArvore 3
#  SubArvore 4
#  SubArvore 5
# Arvore 2
#  SubArvore 1
#    SubSubArvore 1
#    SubSubArvore 2
#        SubSubSubArvore 1

print('\nEstilo 2')
listaArvore(lista_exemplo,'-')
# Saída:
#-Arvore 1
#--SubArvore 1
#--SubArvore 2
#--SubArvore 3
#--SubArvore 4
#--SubArvore 5
#-Arvore 2
#--SubArvore 1
#----SubSubArvore 1
#----SubSubArvore 2
#--------SubSubSubArvore 1

#Experimente usar os caracteres .=_¨~
