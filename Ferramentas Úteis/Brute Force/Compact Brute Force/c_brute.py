#coding:latin-1
import time,os,sys,platform

# Gabriel Matheus de Castro 04/04/2022 (#github.com/GaMaDeCa)
# Compact Brute - Brute Force em arquivos compactados, ferramenta simples e com alguns defeitos(Extrair todos os arquivos não é um método seguro, além de deixar tudo bagunçado).
# Uso: python c_brute.py arquivo.zip senhas.txt
# ATENÇÃO: Quando a senha for encontrada, todos os arquivos serão extraídos na pasta atual!

i,d='Indisponível','Disponível'
ziplib,rarlib=i,i
ZipFile=None

isfile=os.path.isfile
try:
    import zipfile
    ZipFile=zipfile.ZipFile
    ziplib=d
except:
    pass

try:
    import rarfile
    rarlib=d
    # Se o sistema for Windows e tiver com problema em achar a ferramenta UnRAR
    if platform.platform().upper().find('WIN')!=-1:
        UNRAR_EXE='C:\\Program Files\\WinRAR\\UnRAR.exe'
        if isfile(UNRAR_EXE):
            rarfile.UNRAR_TOOL=UNRAR_EXE
except:
    pass

def MA():
    print('------{COMPACT BRUTE}------\n\n')
    tipo=input(f' [TIPO DE ARQUIVO]\n0 = .ZIP [zipfile {ziplib}]\n1 = .RAR [rarfile {rarlib}]\nDigite o tipo de arquivo a atacar: ')
    tu=tipo.upper()
    if (tu=='0' or tu.find('ZIP')!=-1) and (ziplib==d):
        brute_zip()
    elif (tu=='1' or tu.find('RAR')!=-1) and (rarlib==d):
        brute_rar()
    else:
        print("Tipo inválido ou não suportado!")
    MA()

def read_wordlist(wordlist,spli='\n'):
    return open(wordlist,'r').read().split(spli)

def getTempoExecucao(inicio_t):
    t2 = time.localtime()
    fim_t = time.strftime("%H:%M:%S", t2)
    horas_t=int(fim_t[:2])-int(inicio_t[:2])
    minutos_t=int(fim_t[-5:5])-int(inicio_t[-5:5])
    segundos_t=int(fim_t[6:])-int(inicio_t[6:])
    if segundos_t < 0:
        segundos_t=60+segundos_t
    if minutos_t < 0:
        minutos_t=60+minutos_t
    if horas_t < 0:
        horas_t=24+horas_t
    return f'\nTempo de execução : {horas_t} horas {minutos_t} minutos e {segundos_t} segundos!'

def getFiles():
    arquivoC=input('Digite o caminho do arquivo compactado: ')
    if not isfile(arquivoC):
        print('Arquivo compactado não encontrado!')
        MA()
    wordlist_input=input('Digite o caminho da wordlist: ')
    if not isfile(wordlist_input):
        print('Wordlist não encontrada!')
        MA()
    wordlist=read_wordlist(wordlist_input)
    return [arquivoC,wordlist]

def zip_extract_with_password(arquivoZip,senhaString):
    retorno=''
    try:
        with ZipFile(arquivoZip) as arquivoZipado:
            arquivoZipado.extractall(pwd=bytes(senhaString, 'utf-8')) #b'')
            retorno=senhaString
    except Exception: #zipfile.BadZipFile: ou Bad Password para o arquivo
        pass
    return retorno

def rar_extract_with_password(arquivoRAR,senha):
    retorno=''
    try:
        with rarfile.RarFile(arquivoRAR, 'r') as arqRAR:
            arqRAR.extractall(pwd=senha)
            retorno=senha
    except Exception:
        pass
    return retorno


def brute_zip(arquivoZip='',wordlist=''):
    if arquivoZip=='':
        a=getFiles()
        arquivoZip,wordlist=a[0],a[1]
    else:
        if not isfile(arquivoZip) and isfile(wordlist):
            print('Arquivo compactado ou wordlist não encontrados!')
            exit(1)
        wordlist=read_wordlist(wordlist)
    inicio_t=time.strftime("%H:%M:%S", time.localtime())
    print(f'Atacando {arquivoZip}, aguarde...\n')
    for passe in wordlist:
        retorno=zip_extract_with_password(arquivoZip,passe)
        if retorno!='':
            print(f'+[Senha encontrada!]\n SENHA = {retorno}')
            if input('Menu principal? (S/N)').upper().find('S')!=-1:
                print(getTempoExecucao(inicio_t))
                MA()
            else:
                exit(0)
    print('[Senha não encontrada!] :(')
    print(getTempoExecucao(inicio_t))
    MA()

# TODO>Método lento,melhorar com threads.
def brute_rar(arquivoRAR='',wordlist=''):
    if arquivoRAR=='':
        a=getFiles()
        arquivoRAR,wordlist=a[0],a[1]
    else:
        if not isfile(arquivoRAR) and isfile(wordlist):
            print('Arquivo compactado ou wordlist não encontrados!')
            exit(1)
        wordlist=read_wordlist(wordlist)
    inicio_t=time.strftime("%H:%M:%S", time.localtime())
    print(f'Atacando {arquivoRAR}, aguarde...\n')
    for senha in wordlist:
        retorno=rar_extract_with_password(arquivoRAR,senha)
        if retorno!='':
            print(f'+[Senha encontrada!]\n SENHA = {retorno}')
            if input('Menu principal? (S/N)').upper().find('S')!=-1:
                print(getTempoExecucao(inicio_t))
                MA()
            else:
                exit(0)
    print('[Senha não encontrada!] :(')
    print(getTempoExecucao(inicio_t))
    MA()

try:
    arquivoCompactado=sys.argv[1]
    wordlist=sys.argv[2]
    if arquivoCompactado.upper().find('RAR')!=-1:
        brute_rar(arquivoCompactado,wordlist)
    else:
        brute_zip(arquivoCompactado,wordlist)
except Exception:
    MA()
