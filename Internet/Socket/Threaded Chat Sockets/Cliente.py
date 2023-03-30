#coding:latin-1

# [TCS] Threaded Chat Sockets - Gabriel Matheus de Castro(25/01/2023)
# sair - Closes the connection and finish the current script(Exit).
from socket import *
from os import stat
from threading import Thread

class Cliente:
    def __init__(instancia,porta=8652,numero_de_conexoes=None,ip='',cliente=socket(AF_INET,SOCK_STREAM),codificacao='utf-8'):
        instancia.cliente=cliente
        instancia.porta=porta
        instancia.QUANTIDADE=1024
        instancia.ip=ip
        instancia.numero_de_conexoes=numero_de_conexoes
        instancia.ip_servidor=b''
        instancia.conexao=None
        instancia.NOME=''
        instancia.NOME_SERVIDOR=''
        instancia.CODIFICACAO=codificacao
    def setPorta(instancia,porta):
        instancia.porta=porta
    def getPorta(instancia):
        return instancia.porta
    def setQuantidade(instancia,QUANTIDADE):
        instancia.QUANTIDADE=QUANTIDADE
    def getQuantidade(instancia):
        return instancia.QUANTIDADE
    def setNumeroConexoes(instancia,numero_de_conexoes):
        instancia.numero_de_conexoes=numero_de_conexoes
    def getNumeroConexoes(instancia):
        return instancia.numero_de_conexoes
    def setIP(instancia,ip):
        instancia.ip=ip
    def getIP(instancia):
        return instancia.ip
    def escutar(instancia,numero_de_conexoes=None):
        origem=(instancia.ip,instancia.porta)
        instancia.cliente.bind(origem)
        if instancia.numero_de_conexoes!=None:
            instancia.cliente.listen(instancia.numero_de_conexoes)
        elif numero_de_conexoes!=None:
            instancia.cliente.listen(numero_de_conexoes)
        else:
            instancia.cliente.listen()
        conexao,ip_servidor=instancia.cliente.accept()
        instancia.conexao=conexao
        instancia.ip_servidor=ip_servidor
    def getIPServidor(instancia):
        return instancia.ip_servidor[0]
    def getConexao(instancia):
        return instancia.conexao
    def enviar(instancia,*dados,codificacao='utf-8'):
        dados=dados[0]
        if type(dados)!=bytes:dados=bytes(dados,codificacao)
        try:
            instancia.conexao.send(dados)
        except:
            print('Erro de rede, mensagem não enviada, reinicie sua conexão!(sair)')
    def receberQuantidade(instancia,QUANTIDADE):
        resposta=instancia.conexao.recv(QUANTIDADE)
        pad=b'\x08\x06\x05\x02'
        if pad in resposta:
            resposta=resposta.split(pad)
            instancia.NOME_SERVIDOR=resposta[0].decode(instancia.CODIFICACAO)
            resposta=resposta[1]
        print(f'\r\n{instancia.NOME_SERVIDOR}:{instancia.porta}> '+resposta.decode(instancia.CODIFICACAO)+f'\n{instancia.NOME}:{instancia.porta}> ',end='')
    def receber(instancia):
        instancia.receberQuantidade(instancia.QUANTIDADE)
    def enviarNome(instancia,nome):
        instancia.NOME=nome
        instancia.enviar((bytes(instancia.NOME,instancia.CODIFICACAO)+b'\x08\x06\x05\x02'))
    def getNomeServidor(instancia):
        return instancia.NOME_SERVIDOR
    def fechar(instancia):
        instancia.conexao.close()
        instancia.cliente.close()

thread_exec=print
def sempreReceber(*cliente):
    while True:
        try:
            cliente[0].receber()
        except:
            break

def ModoChat():
    cliente=Cliente(8652)
    PORTA=cliente.getPorta()
    print(f'\nAguardando conexão pela porta {PORTA}...\n')
    cliente.escutar()
    IP_SERVIDOR=cliente.getIPServidor()
    print('\n[!]==Conectado com: ',end='')
    print(IP_SERVIDOR)
    print(f'[!]==Porta: {PORTA}')
    mensagem=''
    nome=input('\nInsira um nome para iniciar a conversa(Enter your nickname)> ')
    cliente.enviarNome(nome)
    t=Thread(target=sempreReceber,args=[cliente])
    try:
        t.start()
    except:
        exit(1)
    print('\n[!]==[CHAT INICIADO]\n')
    while mensagem!='sair':
        print(f'{nome}:{PORTA}> ',end='')
        mensagem=input()
        if mensagem=='sair':
            cliente.fechar()
            print('Saindo...')
            exit(0)
        try:
            t=Thread(target=cliente.enviar,args=[mensagem])
            t.start()
        except:
            pass

def threads_count(): thread_exec(bytes.fromhex('5448524541444544204348415420534F434B4554535B5365727665725D202D20446576206279204761627269656C204D6174686575732064652043617374726F2832352F30312F32303233290A0A205B736169725D202D204665636861206F2073637269707420656E63657272616E646F206F20736F71756574652E').decode('UTF-8')) 

threads_count()
ModoChat()
