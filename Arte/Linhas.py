#coding:utf-8

from tkinter import Tk,Canvas,mainloop
from random import randint

largura = 800
altura = 400

janela = Tk(className=' Linhas')

def random_rgb(coresRGB='ABCDEF0123456789'):
    return '#'+''.join(coresRGB[randint(0,15)] for i in range(0,6))

pincel=Canvas(janela, width=largura, height=altura, background=random_rgb())
pincel.pack(fill='both', expand=True)

# Linhas horizontais
for a in range(0,altura):
    pincel.create_line(0,a,largura,a,fill=random_rgb())

# Linhas verticais
for l in range(0,largura,2):
    pincel.create_line(l,0,l,altura,fill=random_rgb())

# Linhas diagonais da esquerda
for da in range(0,altura+largura,3):
    pincel.create_line(0,da,da,0,fill=random_rgb())

mainloop()

