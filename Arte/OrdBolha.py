#coding:latin-1

# OrdBolha.py - Uma visualização do algoritimo de ordenação em bolha(Bubble Sorting) usando Canvas do tkinter.

#Importa os módulos/bibliotecas necessárias
import tkinter,random
#Configura e inicia a janela e o canvas para desenhar, com o fundo branco
largura,altura=600,630
JanelaRaiz=tkinter.Tk()
JanelaRaiz.title(' Algoritimo de Ordenação em Bolha(github.com/Alien8652)')
canvas=tkinter.Canvas(JanelaRaiz,width=largura,height=altura,bg='white')
canvas.grid()
#Printa na tela uma quantidade de numeros iniciais e finais da lista(io=inicio,fm=fim) para reduzir o excesso da saída
def exibirLista(lista,io,fm):print(f'{io} primeiros numeros da lista e {fm} ultimos numeros>\n  {lista[0:io]}-{lista[-fm:]}\n')
#Cria as linhas dada uma lista numerica variando o valor da altura com o valor dos numeros e retorna uma lista com as linhas
def criarLinhas(listaNum):return[canvas.create_line(x,altura-y,x,altura,width=1,fill='black')for x,y in enumerate(listaNum)]
#Simples swap: troca a posição de dois itens da array dado os indices i e i2
def trocarPosicao(array:list,i,i2):array[i],array[i2]=array[i2],array[i]
#Calcula a diferença da coordenada x1 entre duas linhas e move elas trocando tambem a posição das linhas na lista
def trocarLinha(linhas,i,i2):
    coords=canvas.coords(linhas[i])
    coords2=canvas.coords(linhas[i2])
    c1,c2=0,0
    if coords[0]>coords2[0]:#X1>x1
        c1=coords2[0]-coords[0]#x1-X1=A diferença da distância entre os dois
        c2=-c1#Mesma distância invertida
    elif coords[0]<coords2[0]:
        c2=coords[0]-coords2[0]
        c1=-c2
    canvas.move(linhas[i],c1,0)
    canvas.move(linhas[i2],c2,0)
    trocarPosicao(linhas,i,i2)

print(f'Gerando lista de tamanho {largura} com numeros aleatórios entre 1 a {altura}...')
listaNum=[0]*largura#[0,0,0,0,0...
for i in range(largura):
    listaNum[i]=random.randint(1,altura)#Números aleatórios de 1 a 630(altura)

exibirLista(listaNum,5,5)
listaLinhas=criarLinhas(listaNum)
#Classe para lidar com as variaveis importantes e o loop da ordenação.
class OrdBolhaCanvas:
    def __init__(obc,listaLinhas,listaNum,largura):
        obc.listaLinhas=listaLinhas
        obc.listaNum=listaNum
        obc.largura=largura
    #Loop de ordenação, no Bubble Sorting se usa dois while, o primeiro loop while
    #foi substituido por uma função def que se repete com o canvas.after(tempo,função)
    def ordBolhaLoop(obc):
        fimDaTroca=True
        x=0
        while x<(obc.largura-1):
            if obc.listaNum[x]<obc.listaNum[x+1]:
                fimDaTroca=False
                trocarPosicao(obc.listaNum,x,x+1)
                trocarLinha(obc.listaLinhas,x+1,x)
            x+=1
        #Quando não há nenhuma troca, isso significa que a lista já esta ordenanda, então o loop do canvas para.
        obc.largura-=1
        if fimDaTroca:
            print('(Fim da ordenação)')
            exibirLista(obc.listaNum,5,5)
            print('Segure CTRL+C e aguarde um tempo ou feche a janela para sair!')
        elif obc.largura>1:
            try:
                canvas.after(1,obc.ordBolhaLoop)
            except KeyboardInterrupt:
                pass

print('(Ordenação em Bolha)')
OrdBolhaCanvas(listaLinhas,listaNum,largura).ordBolhaLoop()
#Loops principais>
#   ordBolhaLoop - Repete com um delay de 1 segundo até que a lista seja ordenada(decrescente).
#   mainloop - Loop da janela, sem isso o script fecha antes que a ordenação ocorra.
#Caso vc interrompa com o teclado(CTRL+C), exibe uma mensagem de saída(No mainloop demora um pouco para sair)
try:
    JanelaRaiz.mainloop()
except KeyboardInterrupt:
    print('Loop terminado!')
