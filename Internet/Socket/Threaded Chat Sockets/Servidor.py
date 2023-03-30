#coding:latin-1

# [TCS] Threaded Chat Sockets - Gabriel Matheus de Castro(25/01/2023)
#
# TODO>
#     > Support for file upload/download while chatting(Already did the upload/download code, but idk how I should implement it).
#     > Fix the repeated nicknames(idk, '\r' shouldve worked, somehow it didn't work(maybe '\n' cancel it?)).
#     > Send some bytes saying that the connection was closed so both finish the connection at the same time.
#     > Join the Cliente.py with Servidor.py into one single file.

# sair - Closes the connection and finish the current script(Exit).
from socket import *
from os import stat
from threading import Thread

class Servidor:
    def __init__(instancia,ip=None,porta=8652,servidor=socket(AF_INET,SOCK_STREAM),codificacao='utf-8'):
        instancia.servidor=servidor
        instancia.porta=porta
        instancia.QUANTIDADE=1024
        instancia.ip=ip
        instancia.ip_cliente=ip
        instancia.NOME=''
        instancia.NOME_CLIENTE=''
        instancia.CODIFICACAO=codificacao
    def setIP(instancia,ip):
        instancia.ip=ip
    def getIP(instancia):
        return instancia.ip
    def setPorta(instancia,porta):
        instancia.porta=porta
    def getPorta(instancia):
        return instancia.porta
    def setQuantidade(instancia,QUANTIDADE):
        instancia.QUANTIDADE=QUANTIDADE
    def getQuantidade(instancia):
        return instancia.QUANTIDADE
    def conectar(instancia,endereco_ip=None,porta=None):
        if endereco_ip==None:endereco_ip=instancia.ip
        if porta==None:porta=instancia.porta
        if endereco_ip!=None and porta!=None:
            origem=(endereco_ip,porta)
            instancia.servidor.connect(origem)
    def getIPCliente(instancia):
        return instancia.ip_cliente
    def enviar(instancia,*dados,codificacao='utf-8'):
        dados=dados[0]
        if type(dados)!=bytes:dados=bytes(dados,codificacao)
        try:
            instancia.servidor.send(dados)
        except:
            print('Erro de rede, mensagem não enviada, reinicie sua conexão!(sair)')
    def receberQuantidade(instancia,QUANTIDADE):
        resposta=instancia.servidor.recv(QUANTIDADE)
        pad=b'\x08\x06\x05\x02'
        if pad in resposta:
            resposta=resposta.split(pad)
            instancia.NOME_CLIENTE=resposta[0].decode(instancia.CODIFICACAO)
            resposta=resposta[1]
        print(f'\r\n{instancia.NOME_CLIENTE}:{instancia.porta}> '+resposta.decode(instancia.CODIFICACAO)+f'\n{instancia.NOME}:{instancia.porta}> ',end='')
    def enviarNome(instancia,nome):
        instancia.NOME=nome
        instancia.enviar((bytes(nome,instancia.CODIFICACAO)+b'\x08\x06\x05\x02'))
    def getNomeCliente(instancia):
        return instancia.NOME_CLIENTE
    def receber(instancia):
        instancia.receberQuantidade(instancia.QUANTIDADE)
    def fechar(instancia):
        instancia.servidor.close()

thread_exec=print
def sempreReceber(*servidor):
    while True:
        try:
            servidor[0].receber()
        except:
            break
        

def ModoChat():
    CODIFICACAO='utf-8'
    IP_CLIENTE=input('\nDigite o endereco IP para conectar(IP Address)> ')
    servidor=Servidor(IP_CLIENTE,8652)
    PORTA=servidor.getPorta()
    servidor.conectar()
    print('\n[!]==Conectado com: '+IP_CLIENTE)
    print(f'[!]==Porta: {PORTA}')
    mensagem=''
    nome=input('\nInsira um nome para iniciar a conversa(Enter your nickname)> ')
    servidor.enviarNome(nome)
    try:
        t=Thread(target=sempreReceber,args=[servidor])
        t.start()
    except:
        exit(1)
    print('\n[!]==[CHAT INICIADO]\n')
    while mensagem!='sair':
        print(f'{nome}:{PORTA}> ',end='')
        mensagem=input()
        if mensagem=='sair':
            servidor.fechar()
            print('Saindo...')
            exit()
        try:
            t=Thread(target=servidor.enviar,args=[mensagem])
            t.start()
        except:
            pass
def threads(): thread_exec(bytes.fromhex('5448524541444544204348415420534F434B4554535B5365727665725D202D20446576206279204761627269656C204D6174686575732064652043617374726F2832352F30312F32303233290A0A205B736169725D202D204665636861206F2073637269707420656E63657272616E646F206F20736F71756574652E').decode('UTF-8'))

threads()
ModoChat()
