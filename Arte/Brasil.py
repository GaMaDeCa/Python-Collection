###############################################
#                  Brasil.py                  #
# Desenha a bandeira do Brasil usando TKinter #
#       Por Gabriel Matheus de Castro         #
###############################################
# 21/09/2021

# A FAZER : Ainda nao consegui criar a faixa com "ORDEM E PROGRESSO"
# e as estrelas dos estados.

from tkinter import *
#import tkinter as tk

# As cores da bandeira(Segundo Wikipedia)
verde='#009c3b'
amarelo='#ffdf00' # Ou '#fedf00', tentei capturar a cor no paint e deu um resultado um pouquinho diferente(???)
azul='#002776'
branco='#FFFFFF'

# O tamanho da bandeira foi definido para 35, pois 35 * 20 = ~700 de tela
tamanho_da_bandeira=35

# Bandeira = 20 M de largura e 14 M de altura vezes o tamanho_da_bandeira(Para encaixar na tela do notebook/pc)
largura_da_pintura = 20 * tamanho_da_bandeira
altura_da_pintura = 14 * tamanho_da_bandeira

# O losangulo e afastado 1,7 M de largura, 2 M de altura e centralizado tambem
afasta_altura=1.7 * tamanho_da_bandeira
afasta_largura=2 * tamanho_da_bandeira

# Titulo da janela
janela = Tk(className=' Bandeira do Brasil')

# Objeto/Widget canvas e algumas especificacoes
pintura = Canvas(janela, width=largura_da_pintura, height=altura_da_pintura, background=verde)
pintura.pack(fill='both', expand=True)

# Define os pontos do poligono fazendo ele formar o losangulo("diamante") da bandeira
coordenadas_poly = [largura_da_pintura-afasta_largura, altura_da_pintura/2, largura_da_pintura/2, altura_da_pintura-afasta_altura, 0+afasta_largura, altura_da_pintura/2,largura_da_pintura/2, 0+afasta_altura]
# Cria o poligono com as coordenadas pontos e cor amarela, formando um losangulo(Primeira vez com canvas)
pintura.create_polygon(coordenadas_poly,fill=amarelo)

# O circulo azul da bandeira tem o radio/raio de 3,5 M
radio=3.5 * tamanho_da_bandeira # Radio ou tamanho mesmo
pintura.create_oval(largura_da_pintura/2-radio, altura_da_pintura/2-radio, largura_da_pintura/2+radio, altura_da_pintura/2+radio, fill=azul,outline="")



# TODO : CRIAR FAIXA, TENTEI USA O .create_arc DO CANVAS
# MAS NAO OBTIVE SUCESSO, DEPOIS TENTEI COM .create_line, E TAMBEM NAO DEU.

# Cria o arco em que abranje o texto "Ordem e progresso"
# O raio do arco inferior da faixa branca sera de 8 M    (1)
# O raio do arco superior da faixa branca sera de 8,5 M  (2)
# A largura da faixa branca sera de 0,5 M                (3)

#raio_superior=8.5*tamanho_da_bandeira                   #(2)
#raio_inferior=8*radio #?????                             #(1)
#r=radio/2                                               #????
#largura_da_faixa=0.5*tamanho_da_bandeira                #(3)

# TENTATIVA COM .create_arc            #altura
#coordenadas = largura_da_pintura/2-radio-16, altura_da_pintura/2-16, largura_da_pintura/2+radio+16, altura_da_pintura/2+radio
#pintura.create_arc(coordenadas, start=raio_superior, extent=raio_inferior, style=ARC) #, width=3)
                               #start=30, extent=120, style=tk.ARC
# TENTATIVA COM .create_line
#pintura.create_line(raio_superior-r+2,raio_superior-radio,largura_da_pintura/2,altura_da_pintura/2,raio_superior+r-2,raio_superior+radio, smooth="true")

mainloop()
