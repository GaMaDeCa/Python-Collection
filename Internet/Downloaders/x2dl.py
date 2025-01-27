#coding:latin-1

import sys
print("""
   ____     _ _     _            __     _     
  / __ \ __| (_)_ _| |_ _  _ __ /  \ __| |___ 
 / / _` / _` | | '_|  _| || / _| () / _` / -_)
 \ \__,_\__,_|_|_|  \__|\_, \__|\__/\__,_\___|
  \____/                |__/                  

Autor Original: imansour12
 >Todos os metodos request e cabecalhos
Mod: GaMaDeCa
 >Traducao
 >Saida do arquivo
 >Menu de ajuda e reducao de codigo
""")

A=sys.argv
if len(A)==1:
    from os import path
    s=path.sep
    print('{} - Baixa musicas MP3 do YouTube.\n\nUso:\n python {} Link [Saida/Opcional]\nExemplos:\n python {} "https://www.youtube.com/watch?v=UkumV_dHbkg" "SH3 OP.mp3"\n "SH3 OP.mp3"\n python {} "https://www.youtube.com/watch?v=UkumV_dHbkg"\n "You\'re Not Here.mp3"'.replace('{}',__file__.split(s)[::-1][0]))
    exit(0)
video=A[1]
saida=None
if len(A)==3:saida=A[2]

import requests,json

url="https://x2download.com/fr58/download-youtube-to-mp3"

print("Buscando URL: ",video)
r=None
try:
 r=requests.get(url)
except Exception as ex:
 print('Erro na hora de requisitar dados da url!\nException:')
 print(ex)
 exit(1)

headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Accept':'text/css,*/*;q=0.1',
    'Accept-Language':'en-US,en;q=0.5',
    'Accept-Encoding':'gzip, deflate, br',
    'DNT':'1',
    'Connection':'keep-alive',
    'Referer':'https://x2download.com/fr54',
    'Sec-Fetch-Dest':'style',
    'Sec-Fetch-Mode':'no-cors',
    'Sec-Fetch-Site':'same-origin',
    'Pragma':'no-cache',
    'Cache-Control':'no-cache',
    'TE':'trailers',
}

def returnStatus(codigo_de_status):return" "+("Sucesso! [200]"if codigo_de_status==200 else"Erro! Status Code=["+codigo_de_status+"]")

print('Baixando arquivos necessarios...\nOrdem: status - arquivo')
response=requests.get('https://x2download.com/x2download/css/style.min.css?v=15',headers=headers)
print(returnStatus(response.status_code),' - '+'style.min.css')

headers["Sec-Fetch-Dest"]="script"
headers["Accept"]="*/*"

response=requests.get('https://x2download.com/x2download/js/app.min.js?v=37',headers=headers)
print(returnStatus(response.status_code),' - '+'app.min.js')

headers["Sec-Fetch-Dest"]="image"
headers["Referer"]="https://x2download.com/fr54"
headers["Accept"]="image/avif,image/webp,*/*"

for ibagem in['time.png','media.png','convert.png','link-solid.png','settings.png','download.png']:
    resposta=requests.get('https://x2download.com/x2download/imgs/'+ibagem,headers=headers)
    print(returnStatus(response.status_code),' - '+ibagem)

response=requests.get('https://x2download.com/Content/default/images/firefox.svg',headers=headers)
print(returnStatus(response.status_code),' - '+'firefox.svg')

headers["Accept"]='text/javascript, application/javascript, application/ecmascript, applicatio    n/x-ecmascript, */*; q=0.01'
headers["X-Requested-With"]="XMLHttpRequest"
headers["Sec-Fetch-Dest"]="empty"
headers["Sec-Fetch-Mode"]="same-origin"

response=requests.get('https://x2download.com/x2download/js/common.min.js?v=7',headers=headers)
print(returnStatus(response.status_code),' - '+'common.min.js')

#AQUI QUE TA A MERDA(imansour12) [Traduzindo]
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Accept':'*/*',
    'Accept-Language':'en-US,en;q=0.5',
    'Accept-Encoding':'gzip, deflate, br',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With':'XMLHttpRequest',
    'Origin':'https://x2download.com',
    'DNT':'1',
    'Connection':'keep-alive',
    'Referer':'https://x2download.com/fr54',
    'Sec-Fetch-Dest':'empty',
    'Sec-Fetch-Mode':'cors',
    'Sec-Fetch-Site':'same-origin',
    'TE':'trailers',
}
response=requests.post('https://x2download.com/api/ajaxSearch',headers=headers,data=f'q={video}&vt=home')
data=json.loads(response.content)
token=data["token"]
vid=data["vid"]
expiration=data["timeExpires"]

def getSequenciaASCII(char1,char2):return''.join([chr(i)for i in range(ord(char1),ord(char2)+1)])
def filtroSimples(entrada,permitido):return''.join([(c if c in permitido else'')for c in entrada])
sequencia=getSequenciaASCII('a','z')+getSequenciaASCII('A','Z')+getSequenciaASCII('0','9')+'.,-_ []()!~^��'

titulo=data["title"]
if saida==None:saida=titulo+'.mp3'
saida=filtroSimples(saida,sequencia)
print('\nTitulo: ',titulo)
print('Com ID: ',vid)
print('Saida: ',saida)

headers.pop("X-Requested-With")
headers.pop("Referer")
headers["X-Requested-Key"]="de0cfuirtgf67a"
headers["Sec-Fetch-Site"]="cross-site"

print(f'\nAguarde, baixando como "{saida}"...')
data=f'v_id={vid}&ftype=mp3&fquality=128&token={token}&timeExpire={expiration}&client=X2Download.com'
response=requests.post('https://backend.svcenter.xyz/api/convert-by-45fc4be8916916ba3b8d61dd6e0d6994',headers=headers,data=data)
data=json.loads(response.content)

try:
    resposta=requests.get(data["d_url"])
    if resposta.status_code!=200:
        raise Exception('Status Code!=200')
    with open(saida,'wb')as stream:
        stream.write(resposta.content)
    print('Arquivo salvo como "'+saida+'"!')
    exit(0)
except Exception as ex:
    print('Nao foi possivel baixar o arquivo!\nException:')
    print(ex)
    exit(1)
