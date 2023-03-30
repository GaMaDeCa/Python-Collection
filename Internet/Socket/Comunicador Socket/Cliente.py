#coding:latin-1

from socket import *
from os import stat
class Cliente:
    def __init__(instancia,porta=8652,numero_de_conexoes=None,ip='',cliente=socket(AF_INET,SOCK_STREAM)):
        instancia.cliente=cliente
        instancia.porta=porta
        instancia.QUANTIDADE=1024
        instancia.ip=ip
        instancia.numero_de_conexoes=numero_de_conexoes
        instancia.ip_servidor=b''
        instancia.conexao=None
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
    def enviar(instancia,dados,codificacao='utf-8'):
        if type(dados)!=bytes:dados=bytes(dados,codificacao)
        instancia.conexao.send(dados)
    def receberQuantidade(instancia,QUANTIDADE):
        return instancia.conexao.recv(QUANTIDADE)
    def receber(instancia):
        return instancia.receberQuantidade(instancia.QUANTIDADE)
    def enviarArquivo(instancia,caminho,codificacao='utf-8',split='|'):
        try:
            arquivo=open(caminho,'rb')
            tamanho=instancia.tamanhoArquivo(caminho)
            tamanhoStr=str(tamanho)
            nome=instancia.obterNomeArquivo(caminho,'Desconhecido.bin')
            print(f'Enviado arquivo> {nome} {tamanhoStr} bytes')
            conteudo=bytes(nome+split+tamanhoStr+split,codificacao)
            instancia.conexao.send(conteudo)#Envia nome e tamanho do arquivo!
            instancia.conexao.recv(instancia.QUANTIDADE)#Nome e tamanho do arquivo recebido!
            total_enviado=0
            MEGA=1024*1024
            print('[EM MEGABYTES]')
            print(f'A---Tamanho Total: \n{tamanho/MEGA}')
            print('A---Enviado')
            while conteudo!=b'':
                print(total_enviado/MEGA,end='\r')
                conteudo=arquivo.read(instancia.QUANTIDADE)
                if conteudo!=b'':instancia.conexao.send(conteudo)
                total_enviado+=instancia.QUANTIDADE
                if total_enviado>tamanho:total_enviado=tamanho
            arquivo.close()
            print()
            return True
        except Exception as MENSAGEM_ERRO:
            print(MENSAGEM_ERRO)
            return False
    def receberArquivo(instancia,split=b'|'):
        try:
            cabecalho=instancia.conexao.recv(instancia.QUANTIDADE).split(split)#Recebido o nome do arquivo!
            nome_do_arquivo=cabecalho[0]
            tamanho=int(cabecalho[1])
            arquivo=open(nome_do_arquivo,"wb")
            print(instancia.formatarMensagem([b'Recebido arquivo> ',nome_do_arquivo,b' ',tamanho,b' bytes']))
            instancia.conexao.send(b'RECEBIDO!')#Recebi o arquivo!
            conteudo=b''
            total_recebido=0
            MEGA=1024*1024
            print('[EM MEGABYTES]')
            print(f'V---Tamanho Total:\n{tamanho/MEGA}')
            print('V---Recebido:')
            while total_recebido<tamanho:
                print(total_recebido/MEGA,end='\r')
                conteudo=instancia.conexao.recv(instancia.QUANTIDADE)
                if conteudo==b'':break
                arquivo.write(conteudo)
                total_recebido+=instancia.QUANTIDADE
            print(tamanho/MEGA)
            arquivo.close()
            print(instancia.formatarMensagem(['Arquivo salvo como ',nome_do_arquivo]))
            return True
        except Exception as MENSAGEM_ERRO:
            print(MENSAGEM_ERRO)
            return False
    def obterNomeArquivo(instancia,caminho,nome=''):
        caminho_invertido=caminho[::-1]
        indice=caminho_invertido.find('/')
        if indice==-1:indice=caminho_invertido.find('\\')
        if indice!=-1:nome=caminho[len(caminho)-indice:]
        else:nome=caminho
        return nome
    def tamanhoArquivo(instancia,caminho):
        return stat(caminho).st_size
    def formatarMensagem(instancia,lista,codificacao='utf-8'):
        string=b''
        for item in lista:
            tmp=item
            if type(tmp)==int:tmp=str(tmp)
            if type(tmp)!=bytes:string+=bytes(tmp,codificacao)
            else:string+=tmp
        return string
    def fechar(instancia):
        instancia.conexao.close()
        instancia.cliente.close()

CODIFICACAO='utf-8'

cliente=Cliente(8652)
PORTA=cliente.getPorta()
print(f'Escutando na porta {PORTA}')
cliente.escutar()
IP_SERVIDOR=cliente.getIPServidor()
print('Conectado com: ',end='')
print(IP_SERVIDOR)
print(f'Porta: {PORTA}')
opcao=''
TXT_AJUDA='[Cliente Comunicador Socket]\nGabriel Matheus de Castro(github.com/Alien8652)\n\n M = Enviar Mensagem\n G = Receber Mensagem\n A = Enviar Arquivo\n V = Receber Arquivo\n S = Obter informações do soquete(IP,PORTA)\n H = Este Menu de Ajuda\n E = Fechar Conexão(Sair/Exit)\n\nINSTRUÇÕES:Escolha uma das duas opções entre Envio e Recebimento do MESMO TIPO(Mensagem e Mensagem, Arquivo e Arquivo), no outro lado(Servidor) escolha a opção contrária a que vc escolheu mas sempre do MESMO TIPO(Se escolheu Envio no Cliente escolha Receber no Servidor), insira as especificações exigidas e os dados serão enviados/recebidos!\n\n'
print(TXT_AJUDA)
while opcao!='E':
    opcao=input(f'LocalHost:{PORTA}> ').upper()
    if opcao=='M':
        cliente.enviar(input('Digite sua mensagem: '))
    elif opcao=='G':
        print(f'{IP_SERVIDOR}:{PORTA}> ',end='')
        print(cliente.receber())
    elif opcao=='A':
        caminho=input('Caminho do arquivo para enviar> ')
        print('Enviado com sucesso!' if cliente.enviarArquivo(caminho) else 'Falha ao enviar!')
    elif opcao=='V':
        print('Esperando arquivo ser enviado...')
        print('Recebido com sucesso!' if cliente.receberArquivo() else 'Falha ao receber!')
    elif opcao=='S':
        print('Endereço IP conectado: ',end='')
        print(IP_SERVIDOR)
        print(f'Porta: {PORTA}')
    elif opcao=='H':
        print(TXT_AJUDA)

cliente.fechar()
print('Saindo...')
