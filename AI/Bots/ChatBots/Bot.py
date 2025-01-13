# coding: latin-1
import time,os,platform,random

# Criado por Gabriel Matheus de Castro(05/11/2021)
# github.com/GaMaDeCa

# Funções do bot:
#       Cumprimento inicial baseado no horário do computador
#       Opção de registrar respostas
#       Comando sair = 'exit'
#       Formatador de texto com acentos(â vira a)
# TODO:
#   Implementar aleatoriedade
#   Melhorar banco de dados e adicionar controle de opções
#   Adicionar mais funções

nome_do_usuario='User: '

if platform.platform().upper().find('WINDOWS')!=-1:
    nome_do_usuario=os.environ['USERNAME']


#funcoes=['escolha um numero de {n} a {n2}','que horas sao?']

#cortador=chr(254)

#resposta_temporizada=''
#resposta_pergunta=''
#conversa_armazenada=''

responder='Bot: '

#temporizador_esgotado=False
#temporizador=3 # Min


hora=int(time.strftime('%H'))
if hora>=6 and hora<12:
    responder+='Bom dia'
elif hora>=12 and hora<18:
    responder+='Boa tarde'
else:
    responder+='Boa noite'

responder+=' '+nome_do_usuario+'!'

print(responder)

def ler_dados(dat):
    arq=open(dat,'r')
    conte=arq.read()
    arq.close()
    return conte

def splitContent(cont):
    return cont.split('<-SPLIT_BOT->')

def perguntar(conteudo_split,pergunta_do_usuario):
    resposta='Pergunta não encontrada!'
    pergunta_do_usuario=filtrar(pergunta_do_usuario.lower())
    for conta in conteudo_split:
        pergunta=conta[:conta.find('/:;:\\')]
        if pergunta_do_usuario==pergunta:
            resposta=conta[conta.find('/:;:\\')+5:]
    return resposta

def salvar_dados(lista_split,arquivo):
    cont=lista_split[0]
    for item in lista_split[1:]:
        cont+=f'<-SPLIT_BOT->\n{item}'
    with open(arquivo,'w') as arq:
        arq.write(cont)

def bot(arquivo='Bot_arquivo.dat'):
    conteudo=ler_dados(arquivo).replace('\n','')
    conteudo_split=splitContent(conteudo)
    while True:
        entrada=input(f'{nome_do_usuario}: ')
        resposta=perguntar(conteudo_split,entrada)
        if entrada=='exit':
            if input('Deseja sair? (S/N) ').upper()=='S':
                break
        print(f'Bot: {resposta}')
        if resposta=='Pergunta não encontrada!':
            insr=input(f' [Pergunta: {entrada}]\nDeseja inserir resposta pra essa pergunta? (S/N)')
            if insr.upper()=='S':
                conteudo_split.append(f'{entrada}/:;:\\{input("Resposta: ")}')
                salvar_dados(conteudo_split,arquivo)


def filtrar(texto):
    return Remover_Acentos(Remover_Caracteres_Especiais(texto))

def Remover_Caracteres_Especiais(texto):
    caractere_trocado=False
    especiais='-_#%(){};:/\\°ºª@&*$´~^¨+'
    resultado=''
    for i in range(0,len(texto)):
        for w in range(0,len(especiais)):
            if texto[i]==especiais[w]:
                resultado+=''
                caractere_trocado=True
        if caractere_trocado==False:
            resultado+=texto[i]
        else:
            caractere_trocado=False
    return resultado

def Remover_Acentos(texto):
    acentos="áéíóúàèìòùãõñâêîôûäëïöüÿýç"
    substituir='aeiouaeiouaonaeiouaeiouyyc'
    caractere_trocado=False
    resultado=''
    for i in range(0, len(texto)):
        for w in range(0,len(acentos)):
            if texto[i]==acentos[w]:
                resultado+=substituir[w]
                caractere_trocado=True
        if caractere_trocado==False:
            resultado+=texto[i]
        else:
            caractere_trocado=False
    return resultado


bot('Bot_arquivo.dat')
