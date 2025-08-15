#coding:latin-1
import socket,os
CODIFICACAO='utf-8'
class ComunicadorSocket:
    def __init__(ctx,numero_de_conexoes=None,
                     ip='',
                     porta=8652,
                     soquete=socket.socket(socket.AF_INET,socket.SOCK_STREAM),
                     CODIFICACAO='utf-8',
                     QUANTIDADE=1024):
        ctx.soquete=soquete
        ctx.numero_de_conexoes=numero_de_conexoes
        ctx.setQuantidade(QUANTIDADE)
        ctx.setPorta(porta)
        ctx.setIP(ip)
        ctx.ip_cliente=ip
        ctx.ip_servidor=b''
        ctx.conexao=None
    def conectar(ctx,endereco_ip=None,porta=None):
        if endereco_ip==None:endereco_ip=ctx.ip
        if porta==None:porta=ctx.porta
        if endereco_ip!=None and porta!=None:
            try:
                ctx.soquete.connect((endereco_ip,porta))
                ctx.conexao=ctx.soquete
            except Exception as erro:
                print(f'[E]---{erro}')
                exit(1)
    def escutar(ctx,numero_de_conexoes=None):
        ctx.soquete.bind((ctx.ip,ctx.porta))
        if ctx.numero_de_conexoes!=None:ctx.soquete.listen(ctx.numero_de_conexoes)
        elif numero_de_conexoes!=None:ctx.soquete.listen(numero_de_conexoes)
        else:ctx.soquete.listen()
        ctx.conexao,ctx.ip_servidor=ctx.soquete.accept()
    def envArq(ctx,caminho,codificacao='utf-8',split='|'):
        try:
            caminho=ctx.__remAspas(caminho)
            total_enviado=0
            MEGA=1024*1024
            arquivo=open(caminho,'rb')
            tamanho=ctx.__getTamArq(caminho)
            tamanhoStr=str(tamanho)
            nome=ctx.__getNomeArquivo(caminho,'Desconhecido.bin')
            print(f'[!]---Enviado info do arquivo> {nome} {tamanhoStr} bytes')
            conteudo=bytes(nome+split+tamanhoStr+split,codificacao)
            ctx.conexao.send(conteudo)
            ctx.conexao.recv(ctx.QUANTIDADE)
            print(f'[EM MEGABYTES]\n[A]---Tamanho Total: \n{tamanho/MEGA}\n[A]---Enviado:')
            while total_enviado<tamanho:
                print(total_enviado/MEGA,end='\r')
                ctx.conexao.send(arquivo.read(ctx.QUANTIDADE))
                total_enviado+=ctx.QUANTIDADE
                if total_enviado>tamanho:total_enviado=tamanho
            arquivo.close()
            print()
            return True
        except Exception as MENSAGEM_ERRO:
            print(f'[E]---{MENSAGEM_ERRO}')
            return False
    def recArq(ctx,split=b'|'):
        try:
            cabecalho=ctx.conexao.recv(ctx.QUANTIDADE).split(split)
            nome_do_arquivo=cabecalho[0].decode(CODIFICACAO)
            tamanho=int(cabecalho[1])
            arquivo=open(nome_do_arquivo,"wb")
            print(f'[!]---Recebido arquivo> {nome_do_arquivo} {tamanho} bytes')
            ctx.conexao.send(b'RECEBIDO!')
            conteudo=b''
            total_recebido=0
            MEGA=1024*1024
            print(f'[EM MEGABYTES]\n[V]---Tamanho Total:\n{tamanho/MEGA}\n[V]---Recebido:')
            conteudo=ctx.conexao.recv(ctx.QUANTIDADE)
            arquivo.write(conteudo)
            total_recebido+=ctx.QUANTIDADE
            while total_recebido<tamanho:
                print(total_recebido/MEGA,end='\r')
                arquivo.write(ctx.conexao.recv(ctx.QUANTIDADE))
                total_recebido+=ctx.QUANTIDADE
            arquivo.close()
            print(tamanho/MEGA)
            print(f'[!]---Arquivo salvo como {nome_do_arquivo}!')
            return True
        except Exception as MENSAGEM_ERRO:
            print(f'[E]---{MENSAGEM_ERRO}')
            return False
    def __getNomeArquivo(ctx,caminho,nome=''):
        caminho_invertido=caminho[::-1]
        indice=caminho_invertido.find('/')
        if indice==-1:indice=caminho_invertido.find('\\')
        if indice!=-1:nome=caminho[len(caminho)-indice:]
        else:nome=caminho
        return nome
    def __remAspas(ctx,caminho):return caminho[1:-1]if(caminho.startswith('"')and caminho.endswith('"'))or(caminho.startswith("'")and caminho.endswith("'"))else caminho
    def __getTamArq(ctx,caminho):return os.stat(caminho).st_size
    def fechar(ctx):
        if ctx.conexao!=None:ctx.conexao.close()
        ctx.soquete.close()
    def env(ctx,dados,codificacao='utf-8'):ctx.conexao.send(bytes(dados,codificacao)if type(dados)!=bytes else dados)
    def recQto(ctx,QUANTIDADE):return ctx.conexao.recv(QUANTIDADE)
    def rec(ctx):return ctx.recQto(ctx.QUANTIDADE)
    def getPorta(ctx):return ctx.porta
    def getQuantidade(ctx):return ctx.QUANTIDADE
    def getNumeroConexoes(ctx):return ctx.numero_de_conexoes
    def getIP(ctx):return ctx.ip
    def getIPCliente(ctx):return ctx.ip_cliente
    def getIPServidor(ctx):return ctx.ip_servidor
    def getConexao(ctx):return ctx.conexao
    def setPorta(ctx,porta):ctx.porta=porta
    def setQuantidade(ctx,QUANTIDADE):ctx.QUANTIDADE=QUANTIDADE
    def setNumeroConexoes(ctx,numero_de_conexoes):ctx.numero_de_conexoes=numero_de_conexoes
    def setIP(ctx,ip):ctx.ip=ip

def printAjuda():print('[?]---Ajuda\n[Comunicador Socket]\nGabriel Matheus de Castro(github.com/GaMaDeCa)\n\n M = Enviar Mensagem\n G = Receber Mensagem\n A = Enviar Arquivo\n V = Receber Arquivo\n S = Obter informações do soquete(IP,PORTA)\n H = Este Menu de Ajuda\n E = Fechar Conexão(Sair/Exit)\n\nINSTRUÇÕES:Escolha uma das duas opções entre Envio e Recebimento do MESMO TIPO(Mensagem e Mensagem, Arquivo e Arquivo), no outro lado(Servidor) escolha a opção contrária a que vc escolheu mas sempre do MESMO TIPO(Se escolheu Envio no Cliente escolha Receber no Servidor, caso contrário pode ficar travado a conexão), insira as especificações exigidas e os dados serão enviados/recebidos!\n\n')

def iniciar():
    modo=input('[M]---Modo\n C = Modo Cliente(Escuta)\n S = Modo Servidor(Conexão Direta com o Endereço)\n E = Sair\n\nEscolha o modo: ').strip()[0].lower()
    cs=ComunicadorSocket()
    porta=cs.getPorta()
    ip_cliente=''
    if modo=='c':print(f'[!]---Escutando na porta {porta}...');cs.escutar()
    elif modo=='s':ip_cliente=input('[<]---Insira um endereço: ');cs.conectar(ip_cliente)
    elif modo=='e':exit()
    else:print('Insira uma opção!');iniciar()
    ip_servidor=cs.getIPServidor()
    ip=ip_cliente if ip_cliente!='' else ip_servidor
    ip=ip[0] if type(ip)==tuple and len(ip)>0 else ip
    print(f'[!]---Conectado com {ip} na porta {porta}.')
    opcao=''
    printAjuda()
    while opcao!='E':
        opcao=input(f'Local:{porta}> ').upper()
        if opcao=='M':
            cs.env(input('[<]---Digite sua mensagem: '))
        elif opcao=='G':
            print(f'{ip}:{porta}> {cs.rec().decode(CODIFICACAO)}')
        elif opcao=='A':
            caminho=input('Caminho do arquivo para enviar> ')
            print('[!]---Enviado com sucesso!'if cs.envArq(caminho) else'[E]---Falha ao enviar!')
        elif opcao=='V':
            print('[V]---Esperando arquivo ser enviado...')
            print('[!]---Recebido com sucesso!'if cs.recArq() else'[E]---Falha ao receber!')
        elif opcao=='S':
            print(f'Endereço IP conectado: {ip}\nPorta: {porta}')
        elif opcao=='H':
            printAjuda()
    print('[!]---Saindo...')
    cs.fechar()

if __name__=='__main__':iniciar()

