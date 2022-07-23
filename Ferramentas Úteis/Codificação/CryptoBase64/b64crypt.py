#coding:latin-1

from base64 import b64encode,b64decode

# Base64Crypto.py v1.0.0 - Criptografia usando base64 e rotação de bytes simples (Gabriel Matheus de Castro) 21/07/2022

#Max value of data+pswd=250=128+122
#                   (256/2=128)+122

def encriptar(dados,senha):
  i=0
  fi=len(senha)
  dados_encriptados=[]
  for dado in preparar_para_encriptar(dados):
    dados_encriptados.append(dado+round(senha[i]/2))
  return bytearray(dados_encriptados)


def decriptar(dados,senha):
  i=0
  fi=len(senha)
  dados_decriptados=[]
  for dado in dados:
    dados_decriptados.append(dado-round(senha[i]/2))
  return voltar_dados_originais(bytearray(dados_decriptados))

def preparar_para_encriptar(dados):
  return b64encode(dados)

def voltar_dados_originais(dados):
  return b64decode(dados)

#   Português do Brasil                          English
msg1='Digite o caminho(entrada): '               #'Enter the path(input): '
msg2='Digite a senha: '                          #'Enter the password: '
msg3=']-Encriptar=0\n]-Decriptar=1\n\nEscolha: ' #']-Encrypt=0\n]-Decrypt=1\n\nChoose: '
msg4='Digite o caminho(saída): '                 #'Enter the path(output): '

#                                Crypt                   Decrypt
en=open(input(msg1),'rb').read() #my_image.png         | encripted_image.png
se=bytes(input(msg2),'utf-8')    #secretpass8652       | secretpass8652
es=input(msg3)                   #0                    | 1
sa=input(msg4)                   #encripted_image.png  | original_image.png

if es=='0':
  open(sa,'wb').write(encriptar(en,se))
elif es=='1':
  open(sa,'wb').write(decriptar(en,se))
