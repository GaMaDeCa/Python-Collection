#coding:latin-1

# pyBase64 - Implementação de Base64 sem lib e explicativo(Gabriel Matheus de Castro)
# TODO>Criar método para decodificar(Se quiser decodificar use a lib base64.b64decode).
#     >Passar funções para uma classe(class b64Encoder).

# Codifica bytes para base64 seguindo as normas oficiais.
# O processo para codificar os bytes em base64 é:
#   1 Pegar os bytes em binário bruto(00000000) e cortar em 6 dígitos cada parte(Use uma lista array).
#   2 Agora pegue o inteiro de cada item binário nessa lista(Que agora que tem somente 6 bits, ou seja, ~63 variações) e use a tabela de base64 para codificar cada um(Que também tem ~63 variações).
#   3 Adicione o padding('=','==') no final conforme necessário e pronto, já está codificado!
def b64(conteudo_bytes):
    tabela="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    base64=''
    byte_len=len(conteudo_bytes)
    for binarioSeis in binarioParaListaSeisBinario(bytesParaBinario(conteudo_bytes)): # Obtém uma lista de conjunto de bits cortados em 6 dígitos
        base64+=tabela[binarioSeisParaDecimal(binarioSeis)] # Obtém o inteiro desses bits de 6 dígitos e usa eles na tabela de base64 para codificar.
    m=byte_len%3
    # Verifica a necessidade/quantidade do padding de '=', TODO> Não sei se está inteiramente correto, parece funcionar.
    if len(base64)<2 or m==1:
        base64+='=='
    elif m==2:
        base64+='='
    return base64

# Corta o texto de chunk binário gerado pela função bytesParaBinario(), cortando em 6 partes os conjuntos de bits de 8 dígitos retornando uma lista de binarios de seis bits.
# (Exemplo: 10010011, retornaria [100100, 11])
def binarioParaListaSeisBinario(binario):
    binario_chunked=[]
    for i in range(0,len(binario)-1,6):
        binario_chunked.append(binario[i:i+6])
    return binario_chunked

# Converte binários cortados em 6 partes(010110) para seu valor inteiro(22) dentro de 63 variações.
def binarioSeisParaDecimal(binario):
    dec,i=0,5
    for bina in list(int(bi) for bi in binario):
        dec+=bina*(2**i)
        i-=1
    return dec

# Converte inteiros decimais tipo 128/32 para seus respectivos valores binários de 8 bits 10000000/00100000.
def inteiroParaBinario(inteiro): # 8 bits(variações=255)
    string_binaria=''
    n_div=inteiro
    for i in range(8):
        string_binaria+=f'{n_div%2}'
        n_div//=2
    return string_binaria[::-1] # Reverte a string, TODO> Corrigir?

# Usa a função inteiroParaBinario(inteiro) para converter cada inteiro gerado pela lista int de bytes em binario(Formando uma longa string de binario).
def bytesParaBinario(bytes_conteudo):
    binario=''
    if type(bytes_conteudo)!=type(bytes()):
        bytes_conteudo=bytes(bytes_conteudo,'utf-8')
    for inteiro in list(bytes_conteudo):
        binario+=inteiroParaBinario(inteiro)
    return binario



# Para pegar argumentos ou iniciar um menu:
from sys import argv

caminho=argv[1] if len(argv)>1 else input('Digite o caminho do arquivo: ')
conteudo_arquivo=open(caminho,'rb').read()
with open(caminho+'.base64','a') as b64file:
    b64file.write(b64(conteudo_arquivo))
