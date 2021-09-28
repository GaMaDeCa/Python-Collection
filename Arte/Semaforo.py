from tkinter import *
import threading
import time
# Gabriel Matheus de Castro (28/09/2021)

# ligado=True
# Cores e formato : https://commons.wikimedia.org/wiki/File:Traffic_lights_3_states.png

largura = 350 #175
altura = 700 #350

desativado='#7f7f7f' #grey' # Desativado=cinza

cor_da_caixa='#191919' # Pode ser cinza, preto ou amarelo
vermelho='#ff0000'#red'
amarelo='#ffff00'#yellow'
verde='#00ff00'#green'

semaforo=2
tempo_vermelho=4
tempo_verde=8
tempo_amarelo=3

tamanho_da_bolinha=80 # 160
tamanho_da_caixa=125 # (125+125=250)

# largura=220+atual altura=largura+50
ini=110
fim=50
dista=ini*2

# Rodar um loop que interage com o mainloop do tkinter https://stackoverflow.com/questions/459083/how-do-you-run-your-own-code-alongside-tkinters-event-loop
class Semaforo_Janela(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.start()
    def sair(self):
        print('Aguarde, saindo...')
        self.janela.quit()
    def run(self):
        self.janela = Tk(className=' Semaforo')
        self.janela.protocol("WM_DELETE_WINDOW", self.sair)

        self.pintura = Canvas(self.janela, width=largura, height=altura, background='white')
        self.pintura.pack()
        
        x1=largura/2-tamanho_da_caixa
        y1=5 # Pra se afastar dos cantos
        x2=largura/2+tamanho_da_caixa
        y2=altura-1
        caixa_bola=(tamanho_da_caixa-y1)/4
        radius=45
        points = [x1+radius, y1,x1+radius, y1,x2-radius, y1,x2-radius, y1,x2, y1,x2, y1+radius,x2, y1+radius,x2, y2-radius,x2, y2-radius,x2, y2,x2-radius, y2,x2-radius, y2,x1+radius, y2,x1+radius, y2,x1, y2,x1, y2-radius,x1, y2-radius,x1, y1+radius,x1, y1+radius,x1, y1]
        largura_bola = [largura/2-tamanho_da_bolinha-caixa_bola,largura/2+tamanho_da_bolinha+caixa_bola]

        self.pintura.create_polygon(points, fill="black", smooth=True) # Caixa com cantos arredondados : https://stackoverflow.com/questions/44099594/how-to-make-a-tkinter-canvas-rectangle-with-rounded-corners
        # self.caixa_do_semaforo=self.pintura.create_rectangle(x1,y1,x2,y2,fill=cor_da_caixa) # Caixa com cantos retos
        
        self.semaforo_vermelho=self.pintura.create_oval(largura_bola[0],ini-tamanho_da_bolinha,largura_bola[1],(ini+fim)+tamanho_da_bolinha,fill=vermelho,outline="")
        self.semaforo_amarelo=self.pintura.create_oval(largura_bola[0],(ini+dista)-tamanho_da_bolinha,largura_bola[1],(ini+dista+fim)+tamanho_da_bolinha,fill=amarelo,outline="") 
        self.semaforo_verde=self.pintura.create_oval(largura_bola[0],(ini+dista+dista)-tamanho_da_bolinha,largura_bola[1],(ini+dista+dista+fim)+tamanho_da_bolinha,fill=verde,outline="")
        self.janela.mainloop()
    def mudar_Semaforo(self,semaforo):
        if semaforo==2:
            #atributo=self.pintura.itemcget(self.semaforo_vermelho,'fill')
            #if atributo==desativado: # Ou == vermelho
            self.pintura.itemconfig(self.semaforo_vermelho, fill=vermelho)
            self.pintura.itemconfig(self.semaforo_verde, fill=desativado)
            self.pintura.itemconfig(self.semaforo_amarelo, fill=desativado)
            return 0
        if semaforo==1:
            self.pintura.itemconfig(self.semaforo_amarelo, fill=amarelo)
            self.pintura.itemconfig(self.semaforo_vermelho, fill=desativado)
            self.pintura.itemconfig(self.semaforo_verde, fill=desativado)
            return 2
        if semaforo==0:
            self.pintura.itemconfig(self.semaforo_verde, fill=verde)
            self.pintura.itemconfig(self.semaforo_amarelo, fill=desativado)
            self.pintura.itemconfig(self.semaforo_vermelho, fill=desativado)
            return 1
        return None

semaforo_jan = Semaforo_Janela()

# Espera 5 segundos pro tkinter terminar a inicializacao
time.sleep(5)

while True:
    try:
        semaforo=semaforo_jan.mudar_Semaforo(semaforo)
        if semaforo==0:
            time.sleep(tempo_vermelho) # Semaforo Vermelho
        elif semaforo==1:
            time.sleep(tempo_verde) # Semaforo Verde
        elif semaforo==2:
            time.sleep(tempo_amarelo) # Semaforo Amarelo
    except RuntimeError:
        break
