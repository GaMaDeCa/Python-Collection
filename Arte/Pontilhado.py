#coding:latin-1

from tkinter import Tk,Canvas,mainloop
from random import choice

largura,altura=510,510

janela = Tk(className=' Pontilhado')

def random_rgb(cores_RGB=['A','B','C','D','E','F','0','1','2','3','4','5','6','7','8','9']):
    return '#'+''.join(choice(cores_RGB) for i in range(0,6))

def draw_point(pintura,x,y,cor):
    pintura.create_rectangle(x,y,x,y,fill=cor,outline="")
    #return pintura.create_oval(x,y,x,y,fill=cor,outline="")

pintura=Canvas(janela, width=largura, height=altura)
pintura.pack(fill='both')

print('Aguarde, vai demorar alguns minutos...')

# A renderização de muitos pixels consome muita memória(me pergunto se threads adiantariam),
# para deixar o inicio mais rápido divida a largura e altura
# pra diminuir o tamanho do quadro de pixels, ou pule com o for.
for x in range(0,largura): # 0,round(largura/4)): ou 0,largura,4):
    for y in range(0,altura): # 0,round(altura/4)): ou 0,altura,4):
        draw_point(pintura,x,y,random_rgb())

# Fim
mainloop()


