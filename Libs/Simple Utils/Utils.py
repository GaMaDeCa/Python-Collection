#coding:utf-8
import re

#Classe Texto:
class Texto:#TODO>Adicionar mais funcoes nessa lib ;)
    LETRAS_VOGAIS='aeiou'
    LETRAS_CONSOANTES='bcdfghjklmnpqrstvwxyz'
    LETRAS_ALFABETO='abcdefghijklmnopqrstuvwxyz'
    LETRAS_ALFABETO_COM_ACENTOS='aáàâãäbcçdeéèêëfghiíìîïjklmnñoóòôõöpqrstuúùûüvwxyýÿz'
    LETRAS_ACENTUADAS='áéíóúàèìòùÁÉÍÓÚÀÈÌÒÙãõñÃÕÑâêîôûÂÊÎÔÛäëïöüÄËÏÖÜÿýÝçÇ'
    LETRAS_SEM_ACENTOS='aeiouaeiouAEIOUAEIOUaonAONaeiouAEIOUaeiouAEIOUyyYcC'
    NUMEROS='0123456789'
    NUMEROS_SOBRESCRITOS='⁰¹²³⁴⁵⁶⁷⁸⁹'
    NUMEROS_SUBSCRITOS='₀₁₂₃₄₅₆₇₈₉'
    SINAIS_MATEMATICOS_SIMPLES='+−×÷'
    SINAIS_MATEMATICOS_AVANCADOS='√±Σ'
    SIMBOLOS_SOBRESCRITOS='⁺⁻⁼⁽⁾'
    SIMBOLOS_SUBSCRITOS='₊₋₌₍₎'
    ACENTOS='´`^~¨'
    SIMBOLOS='(){}[]<>.,-_;:|\\/#!?*@&%$=+\'"�'
    ESPACO=' '
    GRAUS='°'
    INDICADOR_ORDINAL_A='ª'
    INDICADOR_ORDINAL_O='º'
    FILTRO=None
    def inverter(self,texto):
        #revertido=''
        #for i in range(1,len(texto)+1):
        #    if (len(texto)-i)>=0:
        #        revertido+=texto[len(texto)-i]
        #    else:
        #        break
        return texto[::-1] #Codigo pode ser resumido em uma linha no python :|
    def titulo(self,texto:str):#str especifica que � aceitavel somente strings na var texto
        #if len(texto)==0:return''
        #txtitulo=texto[0].upper()
        #aum=False
        #for i in range(1,len(texto)):
        # car=texto[i]
        # if car==' ':
        #  aum=True
        # else:
        #  car=car.upper()if aum else car
        #  aum=False
        # txtitulo+=car
        #return txtitulo
        return texto.title() #Somente comandos simples do python, mas caso vc tenha dificuldade em aprender ingles.
    def maiusculo(self,texto): return texto.upper()
    def minusculo(self,texto): return texto.lower()
    def filtrar(self,texto,filtro=''):
        if self.FILTRO!=None and filtro=='': filtro=self.FILTRO
        return ''.join(c if c in filtro else '' for c in texto)
    def getPalavras(self,texto,somente_letras=True):
        if somente_letras:
            texto=self.filtrar(texto,self.LETRAS_ALFABETO_COM_ACENTOS+self.maiusculo(self.LETRAS_ALFABETO_COM_ACENTOS))
        for simbolo in self.SIMBOLOS:
            if simbolo in texto:
                texto=texto.replace(simbolo,' ')
        palavras=texto.split(' ')
        espacos_vazios=True
        while espacos_vazios:
            if '' in palavras:
                palavras.remove('')
            else:
                espacos_vazios=False
        return palavras
    def contarPalavra(self,texto,palavra): return texto.count(palavra)
    def contar_palavras(self,texto):
        total=len(self.getPalavras(texto))
        return total
    def cortar_texto(self,texto,a_cada):
        j1,j2=0,a_cada
        texto_cortado=[]
        while j2<len(texto):
            texto_cortado.append(texto[j1:j2])
            j1+=a_cada
            j2+=a_cada
        final=texto[j1:]
        if final!='':
            texto_cortado.append(final)
        return texto_cortado
    def cortar_texto_por_chave(self,texto,chave):return texto.split(chave)
    def removerCharDuplicado(self,texto):
        sem_dup=''
        for char in texto:
            if not char in sem_dup:
                sem_dup+=char
        return sem_dup
    def mais_comum(self,palavras,qto=-1):
        cont={}
        for palavra in palavras:
            if not palavra in cont:
                cont[palavra]=1
            else:
                cont[palavra]+=1
        chaves,valores=list(cont.keys()),list(cont.values())
        for i,vcListTuple in enumerate(sorted(zip(valores, chaves),reverse=True)):
            valores[i],chaves[i]=vcListTuple[0],vcListTuple[1]
        eQto=len(chaves)-1 if qto==-1 else qto
        return (chaves[0:eQto],valores[0:eQto])
    #sJoin(['ola','mundo']) #Soma os valores da lista numa string.
    def sJoin(self,lista):
        return ''.join(lista)
    def getAsciiTable(self):
        return ''.join(chr(i) for i in range(256))
    def removerAcentos(self,texto,acentos=None,substituir=None):
        if acentos==None:acentos=self.LETRAS_ACENTUADAS
        if substituir==None:substituir=self.LETRAS_SEM_ACENTOS
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
    def removerCaracteresEspeciais(self,texto,especiais=None):
        if especiais==None:
            especiais=self.ACENTOS+self.SIMBOLOS+self.GRAUS+self.INDICADOR_ORDINAL_A+self.INDICADOR_ORDINAL_O
        caractere_trocado=False
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
    def removerNumeros(self,texto,numeros=None):
        if numeros==None:numeros=self.NUMEROS
        for n in numeros:
            texto=texto.replace(n,'')
        return texto
    #Algoritimo para verificar se e ou nao um palindromo)
    def palindromo(self,texto,remover_numeros=False,remover_acentos=True,remover_cars_especiais=True,aumentar_letras=True):
        encontrado=None
        if remover_numeros:
            texto=self.removerNumeros(texto)
        if remover_acentos:
            texto=self.removerAcentos(texto)
        if remover_cars_especiais:
            texto=self.removerCaracteresEspeciais(texto)
        if aumentar_letras:
            texto=self.maiusculo(texto)
        if self.inverter(texto)==texto and texto!='':
            encontrado=True
        else:
            encontrado=False
        return encontrado
    # WordList Generator sem libs
    # Marco Costa(https://stackoverflow.com/questions/21559039/python-how-to-generate-wordlist-from-given-characters-of-specific-length)
    def wordlist(self,texto,profundeza):
        wl=[]
        def geradorWordlist(texto,profu): #Uma funcao definida dentro de outra funcao que esta dentro de uma classe :O
            if profu<1:
                return
            for car in texto:
                if profu==1:
                    yield car
                else:
                    for carGen in geradorWordlist(texto,profu-1):
                        yield car+carGen
        # Chama o Gerador
        for profu in range(1,profundeza):
            for word in geradorWordlist(texto,profu):
                wl.append(word)
        return wl
    def extrairDados(self,texto,regex):
        return re.findall(regex,texto)


import math
class Numero:
    PI=math.pi
    def arredondar(self,numero):
        return round(numero) #Essa funcao arredonda pra baixo se o numero for x.5, se for maior tipo x.6 ele arredonda pra cima.
    def arredondarCima(self,numero):
        return math.ceil(numero)
    def arredondarBaixo(self,numero):
        return math.floor(numero)
    def raizQuadrada(self,numero):
        return math.sqrt(numero)
    def trocar_atributo(self,numero):#Se o numero for positivo vira negativo, e vice-versa.
        return-numero
    def atribuir_positivo(self,numero):#Isso e um operador ternario, que e nada mais nada menos que uma forma de usar o if else na mesma linha.
        return self.trocar_atributo(numero) if numero<0 else numero
    def atribuir_negativo(self,numero):
        return self.trocar_atributo(numero) if numero>0 else numero
    def potencia(self,numero,potencia):
        return pow(numero,potencia) #Ou numero**potencia, math.pow tambem e valido.
    def somar_lista(self,lista):
        acumulador=0
        for numero in lista:
            acumulador+=numero
        return acumulador

class TradutorRapido:
    class LINGUA:
        PADRAO=0
    def __init__(tr,chaves=None,traducoes=None):
        tr.genTrad(chaves,traducoes)
        tr.lingua=0
    def genTrad(tr,chaves,traducoes):
        tr.tsl={}
        if not((chaves==None or traducoes==None)or(type(traducoes[0])!=list or len(chaves)!=len(traducoes))):
            for i,chave in enumerate(chaves):
                tr.tsl[chave]=traducoes[i]
    def setLingua(tr,lingua):tr.lingua=lingua
    def traduzir(tr,chave):
        traducao=''
        try:
            traducao=tr.tsl[chave][tr.lingua]
        except:
            pass
        return traducao

#Classe de Teste
#Quase tudo que uma classe pode fazer:
# t=Teste()
# t.funcao(2) #8
# t=Teste(4)
# t.funcao(2+t.NUM) #14
# t.setNum(2)
# t.funcao(2) #8
# Teste.funcaoEstatica(2) #4

#Documentacao:
# Classe=t.__doc__ ou Teste.__doc__
# Fun�ao=t.__doc__

class Extendeu:
    NUMEXT=2
    def __init__(ctx):pass
    def funcaoExtendida(ctx,arg):
        return ctx.NUMEXT+arg

class Teste(Extendeu):
    '''Documentacao sobre a classe, acessivel com classe.__doc__, Teste aceita argumentos Teste(entradaInicial=Numero)'''
    NUM=3
    #Essa funcao e padrao do python, ela indica como deve ser instanciada a classe
    #E de padrao de argumento, a entradaInicial e 2
    #O primeiro argumento(contexto) e necessario em classes instanciadas, ela indica a propria classe em si, veja que
    #ela mesma executa uma funcao interna da classe, o nome do argumento de contexto recomendado no python e self, mas
    #vai da escolha do programador(contexto,ctx,c,this)
    def __init__(contexto,entradaInicial=2):
        contexto.setNum(entradaInicial)
    def setNum(contexto,num):
        '''Descricao interna da funcao, acessivel com classe.funcao.__doc__, a funcao setNum atribui um valor para variavel NUM da classe Teste'''
        contexto.NUM=num
    #Essa funcao retorna erro se instanciar a classe(Teste()), deve ser executada diretamente com Teste.funcaoEstatica
    #Ela tambem retorna um erro se o argumento nao for um numero inteiro(int), uma classe pode ser feita inteiramente
    #somente com metodos/funcoes estaticas
    def funcaoEstatica(argumento:int):
        return argumento+argumento
    def funcao(contexto,argumento):
        return contexto._funcaoProtegida(argumento)
    def _funcaoProtegida(contexto,argumento):
        return contexto.__funcaoPrivada(argumento)
    def __funcaoPrivada(contexto,argumento):
        return contexto.funcaoExtendida(argumento)+contexto.NUM+contexto.NUMEXT#4+2+2
