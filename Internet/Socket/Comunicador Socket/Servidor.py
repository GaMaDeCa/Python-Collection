#coding:latin-1

from socket import *
from os import stat
class Servidor:
    def __init__(instancia,ip=None,porta=8652,servidor=socket(AF_INET,SOCK_STREAM)):
        instancia.servidor=servidor
        instancia.porta=porta
        instancia.QUANTIDADE=1024
        instancia.ip=ip
        instancia.ip_cliente=ip
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
    def enviar(instancia,dados,codificacao='utf-8'):
        if type(dados)!=bytes:dados=bytes(dados,codificacao)
        instancia.servidor.send(dados)
    def receberQuantidade(instancia,QUANTIDADE):
        return instancia.servidor.recv(QUANTIDADE)
    def receber(instancia):
        return instancia.receberQuantidade(instancia.QUANTIDADE)
    def enviarArquivo(instancia,caminho,codificacao='utf-8',split='|'):
        try:
            arquivo=open(caminho,'rb')
            tamanho=instancia.tamanhoArquivo(caminho)
            tamanhoStr=str(tamanho)
            nome=instancia.obterNomeArquivo(caminho,'Desconhecido.bin')
            print('Enviado arquivo>'+nome+' '+tamanhoStr+' bytes')
            conteudo=bytes(nome+split+tamanhoStr+split,codificacao)
            instancia.servidor.send(conteudo)#Envia nome do arquivo!
            instancia.servidor.recv(instancia.QUANTIDADE)#Nome do arquivo recebido!
            total_enviado=0
            MEGA=1024*1024
            print('[EM MEGABYTES]')
            print(f'A---Tamanho Total: \n{tamanho/MEGA}')
            print('A---Enviado')
            while conteudo!=b'':
                print(total_enviado/MEGA,end='\r')
                conteudo=arquivo.read(instancia.QUANTIDADE)
                if conteudo!=b'':instancia.servidor.send(conteudo)
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
            cabecalho=instancia.servidor.recv(instancia.QUANTIDADE).split(split)#Recebido o nome do arquivo!
            nome_do_arquivo=cabecalho[0]
            tamanho=int(cabecalho[1])
            arquivo=open(nome_do_arquivo,"wb")
            print(instancia.formatarMensagem([b'Recebido arquivo> ',nome_do_arquivo,b' ',tamanho,b' bytes']))
            instancia.servidor.send(b'RECEBIDO!')#Recebi o arquivo!
            conteudo=b''
            total_recebido=0
            MEGA=1024*1024
            print('[EM MEGABYTES]')
            print(f'V---Tamanho Total:\n{tamanho/MEGA}')
            print('V---Recebido:')
            while total_recebido<int(tamanho):
                print(tamanho/MEGA,end='\r')
                conteudo=instancia.servidor.recv(instancia.QUANTIDADE)
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
        instancia.servidor.close()

CODIFICACAO='utf-8'
IP_CLIENTE=input('Digite o endereco IP que vc irá conectar> ')
servidor=Servidor(IP_CLIENTE,8652)
PORTA=servidor.getPorta()
servidor.conectar()
print('Conectado com: '+IP_CLIENTE)
print(f'Porta: {PORTA}')
opcao=''
TXT_AJUDA='[Servidor Comunicador Socket]\nGabriel Matheus de Castro(github.com/Alien8652)\n\n M = Enviar Mensagem\n G = Receber Mensagem\n A = Enviar Arquivo\n V = Receber Arquivo\n S = Obter informações do soquete(IP,PORTA)\n H = Este Menu de Ajuda\n E = Fechar Conexão(Sair/Exit)\n\nINSTRUÇÕES:Escolha uma das duas opções entre Envio e Recebimento do MESMO TIPO(Mensagem e Mensagem, Arquivo e Arquivo), no outro lado(Cliente) escolha a opção contrária a que vc escolheu mas sempre do MESMO TIPO(Se escolheu Envio no Servidor escolha Receber no Cliente), insira as especificações exigidas e os dados serão enviados/recebidos!\n\n'
print(TXT_AJUDA)
while opcao!='E':
    opcao=input(f'LocalHost:{PORTA}> ').upper()
    if opcao=='M':
        servidor.enviar(input('Digite sua mensagem: '))
    elif opcao=='G':
        print(f'{IP_CLIENTE}:{PORTA}> ',end='')
        print(servidor.receber())
    elif opcao=='A':
        caminho=input('Caminho do arquivo para enviar> ')
        print('Enviado com sucesso!' if servidor.enviarArquivo(caminho) else 'Falha ao enviar!')
    elif opcao=='V':
        print('Esperando arquivo ser enviado...')
        print('Recebido com sucesso!' if servidor.receberArquivo() else 'Falha ao receber!')
    elif opcao=='S':
        print('Endereço IP conectado: ',end='')
        print(IP_CLIENTE)
        print(f'Porta: {PORTA}')
    elif opcao=='H':
        print(TXT_AJUDA)

servidor.fechar()
print('Saindo...')
