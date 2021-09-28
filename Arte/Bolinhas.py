#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
from random import *
# Gabriel Matheus de Castro
largura = 800
altura = 500

bolinhas=[]

cores = ['red','yellow','orange','green','blue'] # "white", "black", "cyan", "magenta"...
cores_RGB = ['A','B','C','D','E','F','0','1','2','3','4','5','6','7','8','9'] # Para uma maior variedade de cores

quantidade_de_bolinhas=randint(1,100)

janela = Tk(className=' Bolinhas')

def random_rgb():
    cor_rgb=''
    for i in range(0,6):
        cor_rgb+=choice(cores_RGB)
    #print('Cor: '+'#'+cor_rgb+'\n')
    return '#'+cor_rgb

def nova_posicao():
    largura_aleatoria = randint(1,largura)
    altura_aleatoria = randint(1,altura)
    tamanho_da_bolinha=randint(1,35) # Ou radio/raio
    posicao=[largura_aleatoria-tamanho_da_bolinha, altura_aleatoria-tamanho_da_bolinha, largura_aleatoria+tamanho_da_bolinha, altura_aleatoria+tamanho_da_bolinha]
    #print('Posicao: ',posicao)
    return posicao

pintura = Canvas(janela, width=largura, height=altura, background=random_rgb())
pintura.pack(fill='both', expand=True)
print(f'Criando {quantidade_de_bolinhas} bolinhas com tamanhos entre 1 e 35')
# Cria as bolinhas com cores, tamanhos e posicoes diferentes na tela
for i in range(0, quantidade_de_bolinhas):
    #print(f'Criado bolinha ({i}):')
                                                              #choice(cores)
    bolinhas.append(pintura.create_oval(nova_posicao(), fill=random_rgb(),outline=""))
    
# Método criado por Finn Årup Nielsen(fnielsen)
# Visite o github dele em https://github.com/fnielsen
# Original = https://gist.github.com/fnielsen/3810848
class MoverComMouse():
    def __init__(self):
        self.item = 0; self.previous = (0, 0)
    def selecionar(self, event):
        widget = event.widget 
        # Converte coordenadas da tela para coordenadas da pintura(canvas)
        xc = widget.canvasx(event.x); yc = widget.canvasx(event.y)
        self.item = widget.find_closest(xc, yc)[0]        # ID da bolinha mais próxima
        self.previous = (xc, yc)
        print(("Clicou na bolinha",xc, yc, self.item))
    def arrastar(self, event):
        widget = event.widget
        xc = widget.canvasx(event.x); yc = widget.canvasx(event.y)
        pintura.move(self.item, xc-self.previous[0], yc-self.previous[1])
        self.previous = (xc, yc)

# Obtém a instância do objeto MoverComMouse()
mCm = MoverComMouse()

# Vincula os eventos do mouse com os métodos (tambem pode estar no construtor)
pintura.bind("<Button-1>", mCm.selecionar)
pintura.bind("<B1-Motion>", mCm.arrastar)

# Centraliza todas as bolinhas na tela
#def centralizar_Bolinhas():
#    for i in range(0,len(bolinhas)):
#        item_S=bolinhas[i]
#        pintura.move(item_S, largura/2-pintura.coords(item_S)[0],altura/2-pintura.coords(item_S)[1])

#def mover_Bolinha(id_da_bolinha,distancia,direcao,delay_tempo):
#    for i in range(0,distancia):
#        if direcao=='direita':
#            pintura.after(delay_tempo,pintura.move(id_da_bolinha,1,0))#mover_Acao)
#        if direcao=='baixo':
#            pintura.after(delay_tempo,pintura.move(id_da_bolinha,0,1))
#        if direcao=='esquerda':
#            pintura.after(delay_tempo,pintura.move(id_da_bolinha,-1,0))
#        if direcao=='cima':
#            pintura.after(delay_tempo,pintura.move(id_da_bolinha,0,-1))
#mover_Bolinha(bolinhas[3],300,'direita',2000)

mainloop()
