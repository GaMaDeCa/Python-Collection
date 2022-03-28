#coding:latin-1

# FileTypeFind.py - Gabriel Matheus de Castro 28/03/2022
# Identifica o tipo de arquivo pela assinatura dele
# E exibe uma descrição dele.

# Identify the file type by his file sign
# And shows his description.

# Source (https://en.wikipedia.org/wiki/List_of_file_signatures)
import os


# TODO> Ainda não sei como eu poderia resolver isso:
#                    52494646 ?? ?? ?? ?? 41434F4E
# Provavelmente com regex dá, mas não sei usa regex.
# Se cria um loop pra iterar com os valores ABCDEF0123456789...
# if '?' in hex_sign:
#   for ???
#       ...compara hex_sign==arquivo_hex
# else:
#   ...resto do código

def virgula(texto):
    if '<virg>' in texto:
        return texto.replace('<virg>',',')
    else:
        return texto

# readTable()
def lerTabela():
    if os.path.isfile('table'):
        return open('table','r').read()
    else:
        return 'Erro!'

def spliTable(table):
    ta=table.split('\n')
    for i in range(len(ta)):
        ta[i]=ta[i].split(',')
        for j in range(len(ta[i])):
            if '|' in ta[i][j]:
                ta[i][j]=ta[i][j].split('|')
    return ta

# table_array
tabela_array=spliTable(lerTabela())

ASSINATURA_HEXADECIMAL=0
ISO_8859_1=1
OFFSET=2
EXTENSAO=3
DESCRICAO=4

# 5 Itens diferentes em cada array
# Os itens são:
#        Assinatura Hexadecimal,ISO 8859-1,Offset,Extensão,Descrição
#        (           0         )(   1     )(  2  )(   3   )(    4  )
# Tamanho da array: 197 no total(198=='')
# Função lerAtributo(array,int) = Lê um dos atributos(itens diferentes) listados acima e retorna numa array
def lerAtributo(tabela_array,difer=0):
    if difer>=5 or difer<=-1:
        return 'Erro'
    else:
        arrayEx=[]
        for i in range(len(tabela_array)):
            if tabela_array[i]!=['']:
                if tabela_array[i][difer]!='':
                    #if len(tabela_array[i][difer][0])!=1:
                    #    for item in tabela_array[i][difer]:
                    #        arrayEx.append(item)
                    #else:
                        arrayEx.append(tabela_array[i][difer])
                else:
                    arrayEx.append('')
            else:
                arrayEx.append('')
        return arrayEx


def getTableHexSigns():
    return lerAtributo(tabela_array,ASSINATURA_HEXADECIMAL)

# Testes
#lerAtributo(tabela_array,ASSINATURA_HEXADECIMAL)
#lerAtributo(tabela_array,ISO_8859_1)
#lerAtributo(tabela_array,OFFSET)
#lerAtributo(tabela_array,EXTENSAO)
#lerAtributo(tabela_array,DESCRICAO)

# readFileInHexadecimal(file)
def lerArquivoEmHexadecimal(arquivo):
    return open(arquivo,'rb').read().hex() if os.path.isfile(arquivo) else 'Erro'

# Retorna o índice da array após a comparação do código hex(file signature) e o hex do arquivo original, caso não encontre nada ele retorna -1
# AVISO: Se não encontrar o resultado desejado, digite o índice em que parou na variavel contador
def compararHex(tabela_array,arquivo_hex,continuar_indice=0):
    hex_signs=getTableHexSigns()
    for i in range(continuar_indice,len(hex_signs)):
        hex_sign=hex_signs[i]
        if len(hex_sign[0])!=1:
            for multiHex in hex_sign:
                if multiHex==arquivo_hex[:len(multiHex)].upper():
                    return i
        else:
            if hex_sign==arquivo_hex[:len(hex_sign)].upper():
                return i
    return -1

#arquivo_hex=lerArquivoEmHexadecimal('teste.png') # indice=57 == Array[56]
#indice=compararHex(tabela_array,arquivo_hex)

def FindFileType(analisar_arquivo,continuar_indice=0):
    arquivo_hex=lerArquivoEmHexadecimal(analisar_arquivo)
    indice=compararHex(tabela_array,arquivo_hex,continuar_indice)
    if indice==-1:
        print('Tipo de arquivo não encontrado!') # File type not found!
        exit(1)
    if tabela_array[indice]==['']:
        print('Fim da lista!') # End of list!
        exit(0)
    file_info='Assinatura Hexadecimal: '+str(tabela_array[indice][ASSINATURA_HEXADECIMAL])+'\n'+'ISO 8859-1: '+str(tabela_array[indice][ISO_8859_1])+'\n'+'Offset: '+str(tabela_array[indice][OFFSET])+'\n'+'Extensão: '+str(tabela_array[indice][EXTENSAO])+'\n'+'Descrição: '+virgula(str(tabela_array[indice][DESCRICAO]))
    print('------[Informações sobre o arquivo]------\n'+file_info)
    if input('\nCaso as informações não batem com a realidade, digite S para continuar a busca: ').upper()=='S':
            FindFileType(analisar_arquivo,indice+1)
    print('Fim!!!') # End!!!
    exit(0)

# Start()
def Inicio():
    analisar_arquivo=input('Digite o caminho do arquivo a ser analisado: ') # Enter the path of the file that will be analyzed
    if not os.path.isfile(analisar_arquivo):
        print('Caminho inválido!') # Invalid path!
        exit(1)
    else:
        FindFileType(analisar_arquivo)

if __name__=='__main__':
    Inicio()
