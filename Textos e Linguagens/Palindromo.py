#!/usr/bin/env python
# coding: latin-1

# Gabriel Matheus de Castro (02/10/2021)

# Alguns palíndromos:
# - Socorram-me, subi no ônibus em Marrocos!
# - A babá baba.
# - A base do teto desaba.
# - A cara rajada da jararaca.
# - A cera causa sua careca.
# - A dama admirou o rim da amada.
# - A Daniela ama a lei? Nada!
# - A diva ávida, dádiva à vida.
# - A diva em Argel alegra-me a vida.
# - A droga do dote é todo da gorda.
# - A gorda ama a droga.
# - A grama é amarga.
# - A lupa pula.
# - A mãe te ama.
# - rever;
# - reviver;
# - rir;
# - rodador;
# - sacas;
# - saias;
# - salas;
# - socos;
# - sopapos;
# - Amor a Roma.
# - Lava esse aval.
# - Anotaram a data da maratona.
# Fonte : Flávia Neves (https://www.dicio.com.br/lista-palindromos/)

texto=str(input("Digite o texto : "))

def Inverter_Texto(texto):
    revertido=''
    for i in range(1,len(texto)+1):
        if (len(texto)-i)>=0:
            revertido+=texto[len(texto)-i]
        else:
            break
    return revertido

def Aumentar_Letras(texto):
    letras_grandes='AÁÀÃÂÄBCÇDEÉÈÊËFGHIÍÌÎÏJKLMNÑOÓÒÕÔÖPQRSTUÚÙÛÜVWXYÝZ '
    letras_pequenas='aáàãâäbcçdeéèêëfghiíìîïjklmnñoóòõôöpqrstuúùûüvwxyýz '
    texto_aumentado=''
    t=False
    for i in range(0,len(texto)):
        for w in range(0,len(letras_grandes)):
            if texto[i]==letras_pequenas[w] or texto[i]==letras_grandes[w]:
                texto_aumentado+=letras_grandes[w]
                t=True
        if not t:
            texto_aumentado+=texto[i]
        else:
            t=False
    return texto_aumentado

def Remover_Caracteres_Especiais(texto):
    caractere_trocado=False
    especiais=' ,.!?-_#%(){};:/\\°ºª@&*$´~^¨+'
    resultado=''
    for i in range(0,len(texto)):
        for w in range(0,len(especiais)):
            if texto[i]==especiais[w]:
                caractere_trocado=True
        if caractere_trocado==False:
            resultado+=texto[i]
        else:
            caractere_trocado=False
    return resultado

def Remover_Acentos(texto):
    acentos="áéíóúàèìòùÁÉÍÓÚÀÈÌÒÙãõñÃÕÑâêîôûÂÊÎÔÛäëïöüÄËÏÖÜÿýÝçÇ"
    substituir='aeiouaeiouAEIOUAEIOUaonAONaeiouAEIOUaeiouAEIOUyyYcC'
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

def Encontrar_Palindromo(texto):
    encontrado=None
    palindromo=Remover_Acentos(Remover_Caracteres_Especiais(Aumentar_Letras(Inverter_Texto(texto))))
    if palindromo==Remover_Acentos(Remover_Caracteres_Especiais(Aumentar_Letras(texto))):
        encontrado=True
    else:
        encontrado=False
        #palindromo=None
    return [encontrado,palindromo]

palindromo=Encontrar_Palindromo(texto)
if palindromo[0]==True:
    print(f"Palíndromo Encontrado!\nTexto = {texto}\nPalíndromo = {Inverter_Texto(texto)}")
else:
    print(f"Palíndromo Não Encontrado!\nTexto = {texto}\nResultados = {palindromo}")

# Isso tudo ou simplesmente:
#
#from unicodedata import normalize
#texto=str(input('Digite o texto : '))
#compara=normalize('NFKD', texto.upper().replace(" ","")).encode('ASCII', 'ignore').decode('ASCII')
#if compara[::-1]==compara:
#    print(f"Palíndromo Encontrado!\nTexto = {texto}\nPalíndromo = {texto[::-1]}")
#else:
#    print(f"Palíndromo Não Encontrado!\nTexto = {texto}\nResultados = {texto[::-1]}")
