titulo='PingPong.py - github.com/GaMaDeCa'
# Jogo Ping-Pong com suporte a dois jogadores, som(caso tenha instalado a biblioteca playsound e baixado todos os sons),
# as cores da mesa, bola, jogador e caixa de pontos sao aleatorias.

#Controles(Teclado):
# 1 Jogador(Esquerda:Letras):
#       Q=Cima, A=Baixo
# 2 Jogador(Direita:Direcional):
#       UP=Cima, DOWN=Baixo
# Sair do jogo: Esc(Escape)
# Resetar jogo: R

#TODO:Corrigir>
#   - A bolinha pode prender na paleta do jogador, aumentando bastante a velocidade e podendo fazer centenas de pontos contra ate travar.
#   - Teletransportar a bola no meio da tela ao fazer um ponto pode ser a solucao do problema acima.
#   - Velocidade do jogo as vezes se altera(ou nao, sei la).
import tkinter,random,threading
Thread=threading.Thread
tocaSom=None
#Site dos sons: mixkit.co/free-sound-effects/game/
bateuParede='bolaBatendo.wav'   #1 - Game ball tap
bateuRaquete='bateuRaquete.wav' #2 - Player jumping in a video game
acertou='acertou.wav'           #1 - Boxer getting hit
musica='musica.wav'             #1 - Game level music
try:
    import os,playsound
    isfile=os.path.isfile
    if isfile(bateuParede) and isfile(bateuRaquete) and isfile(acertou) and isfile(musica):
        tocaSom=playsound.playsound
except:
    pass

X,Y,X2,Y2=0,1,2,3
class PingPong:
    CONTROLES=[False,False,False,False]#Q,A,UP,DOWN
    Q=81
    A=65
    UP=38
    DOWN=40
    ESCAPE=27
    R=82
    def pressionaTecla(p,evento):
        tecla=evento.keycode
        if tecla==p.R:p.resetar()
        elif tecla==p.ESCAPE:p.sair()
        elif tecla==p.Q:p.CONTROLES[0]=True
        elif tecla==p.A:p.CONTROLES[1]=True
        elif tecla==p.UP:p.CONTROLES[2]=True
        elif tecla==p.DOWN:p.CONTROLES[3]=True
    def soltaTecla(p,evento):
        tecla=evento.keycode
        if tecla==p.Q:p.CONTROLES[0]=False
        elif tecla==p.A:p.CONTROLES[1]=False
        elif tecla==p.UP:p.CONTROLES[2]=False
        elif tecla==p.DOWN:p.CONTROLES[3]=False
    def __init__(p,janela=None,largura=None,altura=None):
        if janela==None:
            janela=tkinter.Tk()
            janela.title(titulo)
            janela.attributes('-fullscreen',True)
            largura,altura=janela.wm_maxsize()[0:2]
        elif largura==None and altura==None:
            largura=janela.winfo_width()
            altura=janela.winfo_height()
        elif type(largura)==str:
            try:
                largura=largura.split('x')
                altura=int(largura[1])
                largura=int(largura[0])
            except:
                pass
        p.largura=largura
        p.altura=altura
        p.janela=janela
        p.janela.bind_all('<KeyPress>',p.pressionaTecla)
        p.janela.bind_all('<KeyRelease>',p.soltaTecla)
        p.pontos=[0,0, #Pontos 1 e Pontos 2
                  0,0] #Ultima Pontuacao 1 e 2
        coresJogador=['#FFFF00','#00FF00','#000000']
        p.cor_bola=random.choice(['#FFA800','#FFFFFF'])
        corMesa=random.choice([('#0000FF','#FFFFFF'),('#FF0000','#FFFF00')])
        p.cor_fundo_mesa=corMesa[0]
        p.cor_linha_mesa=corMesa[1]
        # Se a mesa for vermelha permitir um possivel jogador da cor azul, vice-versa
        if p.cor_fundo_mesa!='#FF0000':coresJogador.append('#FF0000')
        if p.cor_fundo_mesa!='#0000FF':coresJogador.append('#0000FF')
        p.cor_jogador1=random.choice(coresJogador)
        p.cor_jogador2=random.choice(coresJogador)
        p.mTela=p.altura/2
        p.mQuinto=p.mTela/5
        p.Br=p.largura/60
        p.BPadraov=p.largura/230
        p.BLimitev=p.largura/90
        p.canvas=tkinter.Canvas(janela,width=p.largura,height=p.altura,background=p.cor_fundo_mesa,highlightthickness=0)
        p.canvas.focus_set()
        p.canvas.pack()
        #Desenhar mesa
        p.canvas.create_line(4,p.altura/2,p.largura-4,p.altura/2,width=4,fill=p.cor_linha_mesa)
        p.canvas.create_rectangle(4,4,p.largura-4,p.altura-4,width=4,outline=p.cor_linha_mesa)
        #Rede
        p.canvas.create_rectangle(p.largura/2-4,4,p.largura/2+4,p.altura-4,fill=p.cor_linha_mesa,outline='#0000FF')
        #Caixa de pontuacao
        caixaTexto=[p.largura/2-80,40-21,p.largura/2+80,40+21]
        p.canvas.create_rectangle(caixaTexto,fill='#220000'if p.cor_fundo_mesa=='#0000FF'else'#000022',outline='#AAAAAA',width=4)
        p.texto_pontos=None
        p.jogador1=None
        p.jogador2=None
        p.bola=None
        p.resetar()
    def tocarMusica(p):
        if tocaSom!=None:
            while True:
                tocaSom(musica,block=True)
    def tocarSom(p,arquivoSom):
        if tocaSom!=None:
            thread=Thread(target=tocaSom,args=[arquivoSom])
            thread.daemon=True
            thread.start()
    def mainloop(p):p.janela.mainloop()
    def deletar(p,objeto):p.canvas.delete(objeto)
    def move(p,obj,x,y):p.canvas.move(obj,x,y)
    def sair(p):exit(0)
    def getCoord(p,objeto):return p.canvas.coords(objeto)
    def colisaoRetangular(p,coord1,coord2):return (coord1[X2]>coord2[X] and coord1[X]<coord2[X2])and(coord1[Y2]>coord2[Y] and coord1[Y]<coord2[Y2])
    def atualizarCoords(p):
        p.J1=p.getCoord(p.jogador1)
        p.J2=p.getCoord(p.jogador2)
        p.B=p.getCoord(p.bola)
        xv=p.Bxv if p.Bxv>0 else -p.Bxv
        yv=p.Byv if p.Byv>0 else -p.Byv
        p.B[X]-=xv
        p.B[Y]-=yv
        p.B[X2]+=xv
        p.B[Y2]+=yv
    def atualizarPontos(p):
        if p.texto_pontos!=None:p.deletar(p.texto_pontos)
        p.texto_pontos=p.canvas.create_text(p.largura/2,40,fill='#FF0000'if p.cor_fundo_mesa=='#0000FF'else'#0000FF',font='Arial 33',text=f'{p.pontos[0]} x {p.pontos[1]}')
        p.pontos[2]=p.pontos[0]
        p.pontos[3]=p.pontos[1]
    def lancarBola(p):
        p.Bxv=random.choice((p.Bxv,-p.Bxv))
    def resetar(p):
        p.pontos=[0,0,0,0]
        p.Bxv=p.BPadraov
        p.Byv=p.BPadraov
        p.By=p.mTela-p.Br
        p.By2=p.mTela+p.Br
        p.Jv=10#p.altura/10
        p.Jy=p.mTela-p.mQuinto
        p.Jy2=p.mTela+p.mQuinto
        p.B=[p.mTela-p.Br,p.By,p.mTela+p.Br,p.By2]
        p.J1=[0,p.Jy,20,p.Jy2]
        p.J2=[p.largura-20,p.Jy,p.largura,p.Jy2]
        #Jogadores e Bola
        if p.jogador1!=None:p.deletar(p.jogador1)
        if p.jogador2!=None:p.deletar(p.jogador2)
        if p.bola!=None:p.deletar(p.bola)
        p.jogador1=p.canvas.create_rectangle(p.J1,fill=p.cor_jogador1,outline='')
        p.jogador2=p.canvas.create_rectangle(p.J2,fill=p.cor_jogador2,outline='')
        p.bola=p.canvas.create_oval(p.B,fill=p.cor_bola,outline=p.cor_bola)#'')
        p.lancarBola()
        p.atualizarPontos()
    def aumentarVelocidade(p):
        if p.Bxv<p.BLimitev:p.Bxv+=0.5 if p.Bxv>0 else -0.5
        if p.Byv<p.BLimitev:p.Byv+=0.5 if p.Byv>0 else -0.5
    def resetarVelocidade(p):
        p.Bxv=p.BPadraov if p.Bxv>0 else -p.BPadraov
        p.Byv=p.BPadraov if p.Byv>0 else -p.BPadraov
    def loopJogo(p):
        p.move(p.bola,p.Bxv,p.Byv)
        J1Moveu,J2Moveu=False,False
        if p.CONTROLES[0]:
            if p.J1[Y]>0:
                p.move(p.jogador1,0,-p.Jv)
                J1Moveu=True
        if p.CONTROLES[1]:
            if p.J1[Y2]+p.Jv<p.altura:
                p.move(p.jogador1,0,p.Jv)
                J1Moveu=True
        if p.CONTROLES[2]:
            if p.J2[Y]>0:
                p.move(p.jogador2,0,-p.Jv)
                J2Moveu=True
        if p.CONTROLES[3]:
            if p.J2[Y2]+p.Jv<p.altura:
                p.move(p.jogador2,0,p.Jv)
                J2Moveu=True
        # Necessario mover continuamente o jogador para continuar gastando o mesmo fps
        if not J1Moveu:p.move(p.jogador1,0,0)
        if not J2Moveu:p.move(p.jogador2,0,0)
        p.atualizarCoords()
        if p.B[X2]>p.largura:
            p.pontos[0]+=1
            p.Bxv=-p.Bxv
            p.tocarSom(acertou)
            p.resetarVelocidade()
        if p.B[X]<0:
            p.pontos[1]+=1
            p.Bxv=-p.Bxv
            p.tocarSom(acertou)
            p.resetarVelocidade()
        if p.B[Y]<0 or p.B[Y2]>p.altura:
            p.Byv=-p.Byv
            p.tocarSom(bateuParede)
        if p.colisaoRetangular(p.B,p.J1):
            p.Bxv=-p.Bxv
            #Calcula a media da altura do jogador e depois redireciona a bola caso bata nos cantos
            J1ym=p.J1[Y]+(p.J1[Y2]-p.J1[Y])/2
            if p.B[Y2]<J1ym:p.Byv=-p.Byv if p.Byv>0 else p.Byv
            elif p.B[Y]>J1ym:p.Byv=-p.Byv if p.Byv<0 else p.Byv
            p.tocarSom(bateuRaquete)
            p.aumentarVelocidade()
        if p.colisaoRetangular(p.B,p.J2):
            p.Bxv=-p.Bxv
            J2ym=p.J2[Y]+(p.J2[Y2]-p.J2[Y])/2
            if p.B[Y2]<J2ym:p.Byv=-p.Byv if p.Byv>0 else p.Byv
            elif p.B[Y]>J2ym:p.Byv=-p.Byv if p.Byv<0 else p.Byv
            p.tocarSom(bateuRaquete)
            p.aumentarVelocidade()
        #Se o ponto atual for diferente do ultimo ponto salvo, atualizar caixa de texto da pontuacao.
        if p.pontos[2]!=p.pontos[0] or p.pontos[3]!=p.pontos[1]:p.atualizarPontos()
        p.canvas.after(10,p.loopJogo)
    def iniciarJogo(p):
        Thread(target=p.tocarMusica,daemon=True).start()
        p.loopJogo()
        p.mainloop()

#tela='640x480'
#janelaRoot=tkinter.Tk()
#janelaRoot.title(titulo)
#janelaRoot.geometry(tela)
#pong=PingPong(janelaRoot,tela) #Ou tambem PingPong(janelaRoot,640,480)
#pong.iniciarJogo()

#Inicio rapido que cobre a tela inteira(fullscreen)
PingPong().iniciarJogo()
