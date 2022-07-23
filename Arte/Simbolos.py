from tkinter import *
from random import choice

largura=700
altura=600

janela=Tk()

pincel=Canvas(janela, width=largura, height=altura, background='#FFFFFF')
pincel.pack(fill='both', expand=True)

def Asterisco(pincel,x,y,largura,altura,cor='#000000'):
    pincel.create_line(x+largura/2,y,x+largura/2,y+altura,fill=cor)
    pincel.create_line(x+largura,y+altura/4,x,y+altura-altura/4,fill=cor)
    pincel.create_line(x,y+altura/4,x+largura,y+altura-altura/4,fill=cor)

#Ou Estrela de Davi
def Hexagrama(pincel,x,y,largura,altura,cor='#000000'):
    pincel.create_line(x,y+altura/4,x+largura,y+altura/4,fill=cor)          # -
    pincel.create_line(x+largura,y+altura/4,x+largura/2,y+altura,fill=cor)  # /
    pincel.create_line(x+largura/2,y+altura,x,y+altura/4,fill=cor)          # \
    pincel.create_line(x,y+altura-altura/4,x+largura,y+altura-altura/4,fill=cor)    # -
    pincel.create_line(x+largura,y+altura-altura/4,x+largura/2,y,fill=cor)          # \
    pincel.create_line(x+largura/2,y,x,y+altura-altura/4,fill=cor)                  # /

def Hexagrama_Thelemita(pincel,x,y,largura,altura,cor='#000000'):
    pincel.create_line(x+largura,y+altura/4,x,y+altura-altura/4,fill=cor)
    pincel.create_line(x+largura,y+altura/4,x+largura/2,y+altura,fill=cor)
    pincel.create_line(x+largura/2,y+altura,x,y+altura/4,fill=cor)
    pincel.create_line(x,y+altura/4,x+largura,y+altura-altura/4,fill=cor)
    pincel.create_line(x+largura,y+altura-altura/4,x+largura/2,y,fill=cor)
    pincel.create_line(x+largura/2,y,x,y+altura-altura/4,fill=cor)

def Pentagrama(pincel,x,y,largura,altura,cor='#000000',cor_fundo='#ff0000',cor_borda=None):
    if cor_borda==None:
        cor_borda=cor
    pincel.create_oval(x,y,x+largura,y+altura,fill=cor_borda)
    pincel.create_oval(x,y,x+largura,y+altura,fill=cor_fundo,width=6)
    pincel.create_line(x+largura/14,y+altura/4,x+largura-largura/14,y+altura/4,fill=cor)
    pincel.create_line(x+largura/14,y+altura/4,x+largura-largura/4,y+altura-altura/14,fill=cor)
    pincel.create_line(x+largura-largura/14,y+altura/4,x+largura/4,y+altura-altura/14,fill=cor)
    pincel.create_line(x+largura/4,y+altura-altura/14,x+largura/2,y,fill=cor)
    pincel.create_line(x+largura-largura/4,y+altura-altura/14,x+largura/2,y,fill=cor)

def Cruz(pincel,x,y,largura,altura,grossura=2,cor='#000000',cor_borda=None):
    if cor_borda==None:
        cor_borda=cor
    pincel.create_rectangle(x+largura/2-grossura,y,x+largura/2+grossura,y+altura,fill=cor,outline=cor_borda)
    pincel.create_rectangle(x,y+altura/3-grossura,x+largura,y+altura/3+grossura,fill=cor,outline=cor_borda)

#Usando as funcoes acima:
Hexagrama(pincel,18,18,333,333,'#0000ff')

pincel.create_oval(largura/4+largura/2-1,20-1,largura/4+largura/2+50+1,20+50+1,fill='black') #Fundo do Asterisco(Devido a cor ser muito clara)
Asterisco(pincel,largura/4+largura/2,20,50,50,'yellow')

Hexagrama_Thelemita(pincel,20,350,220,220,'#ff00ff')

Pentagrama(pincel,300,300,280,280,cor='blue',cor_fundo='red',cor_borda='yellow')

pincel.create_rectangle(500-1,150-1,500+100+1,150+130+1,fill='black') #Fundo do Cruz
Cruz(pincel,500,150,100,130,4,'#00ffff')

mainloop()

