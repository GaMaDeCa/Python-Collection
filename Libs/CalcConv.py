#coding:latin-1

#Calcula e Converte vários tipos de informações de diversas áreas.
#TODO>Testar tudo, principalmente na classe Dados, mudar alguns métodos tbm
import time,datetime
from math import floor
# * = Multiplicação
# / = Divisão
class Tempo:
    '''Conversor de unidades de tempo, mili(milissegundos), seg(segundos), minu(minutos), horas, etc.'''
    def mili_pra_seg(mili):return mili/1000
    def mili_pra_minu(mili):return mili/(1000*60)
    def mili_pra_horas(mili):return mili/(1000*60*60)
    def mili_pra_dias(mili):return mili/(1000*60*60*24)
    def seg_pra_mili(seg):return seg*1000
    def seg_pra_minu(seg):return seg/60
    def seg_pra_horas(seg):return seg/3600
    def seg_pra_dias(seg):return seg/86400
    def minu_pra_mili(minu):return minu*60*1000
    def minu_pra_seg(minu):return minu*60
    def minu_pra_horas(minu):return minu/60
    def minu_pra_dias(minu):return minu/1440
    def horas_pra_mili(horas):return horas*3600*1000
    def horas_pra_seg(horas):return horas*3600
    def horas_pra_minu(horas):return horas*60
    def horas_pra_dias(horas):return horas/24
    def horas_pra_anos(horas):return horas/8760
    def dias_pra_mili(dias):return dias*24*60*60*1000
    def dias_pra_seg(dias):return dias*24*60*60
    def dias_pra_minu(dias):return dias*24*60               # Ou 1440
    def dias_pra_horas(dias):return dias*24
    def dias_pra_anos(dias):return dias/365
    def meses_pra_anos(meses):return meses/0.0833334
    def anos_pra_minu(anos):return anos*525600
    def anos_pra_horas(anos):return anos*8760
    def anos_pra_dias(anos):return anos*365
    def anos_pra_semanas(anos):return anos*52.1429
    def anos_pra_meses(anos):return anos*12
    #Algoritimo de Zeller
    dias_da_semana=['Sabado','Domingo','Segunda','Terca','Quarta','Quinta','Sexta']
    def dia_semana(dia:int,mes:int,ano:int):
        if mes<3:
            mes+=12
            ano-=1
        ano1=floor(ano/100)
        ano2=ano%100
        dia_da_semana=floor((dia+floor((13*(mes+1))/5)+ano2+floor(ano2/4)+floor(ano1/4)+(5*ano1))%7)
        return dia_da_semana
    def hora(retornoString=False):#locale.setlocale(locale.LC_ALL,'pt_BR.UTF-8')
        ret=datetime.datetime.now().strftime("%d,%m,%Y").split(',')#"%A, %d de %B de %Y")
        return ret if retornoString else[int(item)for item in ret]
    #Calcula a passagem do tempo
    def passagem_tempo(nascimento:str,data_atual=None):#Insira a data de nascimento seguindo o padrao brasileiro e com barras separadoras("Dia/Mes/Ano")
        agora=time.strftime('%d/%m/%Y').split('/') if data_atual==None else data_atual
        nascimento=nascimento.split('/')
        dia,mes,ano=int(agora[0])-int(nascimento[0]),int(agora[1])-int(nascimento[1]),int(agora[2])-int(nascimento[2])
        if dia<0:
            mes-=1
            dia+=31
        if mes<0:
            ano-=1
            mes+=12
        return f'{ano} Anos\n{mes} Meses\n{dia} Dias'

class Comprimento:
    def micrometros_pra_nanometros(micrometos):
        return micrometos*1000
    def milimetros_pra_micrometos(milimetros):
        return milimetros*1000
    def metros_pra_milimetros(metros):
        return metros*1000
    def metros_pra_centimetros(metros):
        return metros*100
    def quilometros_pra_metros(quilometros):
        return quilometros*1000
    def quilometros_pra_milhas(quilometros):
        return quilometros/1.61
    def milhas_pra_metros(milhas):
        return milhas*1609.34
    def milhas_pra_quilometros(milhas):
        return milhas*1.61
    #Ex:velocidade_media(100,40,['Metro','Segundo']) # '100 Metro / 40 Segundo = 2.5 Metro por Segundo'
    def velocidade_media(distancia,tempo,nomes=['Distancia','Tempo']):
        return f'{distancia} {nomes[0]} / {tempo} {nomes[1]} = {(distancia/tempo)} {nomes[0]} por {tempo}'

class Temperatura:
    '''Conversor de temperatura com suporte a Celsius, Kelvin e Fahrenheit.'''
    def celsius_pra_kelvin(celsius):
        return celsius+273
    def celsius_pra_fahrenheit(celsius):
        return celsius*1.8+32 # Talvez? F = ((9 * celsius) / 5) + 32
    def kelvin_pra_celsius(kelvin):
        return kelvin-273
    def kelvin_pra_fahrenheit(kelvin):
        return (kelvin-273)*1.8+32
    def fahrenheit_pra_celsius(fahrenheit):
        return (fahrenheit-32)/1.8
    def fahrenheit_pra_kelvin(fahrenheit):
        return (fahrenheit-32)*5/9+273

class UnidadeInformacao:
    string_hex='0123456789ABCDEF'
    #string_dec='0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15'.split(',')
    def decimal_pra_hexadecimal(decimal):
        return UnidadeInformacao.string_hex[int(decimal/16)]+UnidadeInformacao.string_hex[int(decimal%16)]
    def hexadecimal_pra_decimal(hexadecimal):
        return (UnidadeInformacao.string_hex.find(hexadecimal[0].upper())*16)+(UnidadeInformacao.string_hex.find(hexadecimal[1].upper())*1)
    def bits_pra_bytes(bits):
        return bits/8
    def bytes_pra_bits(bytesV):
        return bytesV*8
    def bytes_pra_kilobytes(bytesV):
        return bytesV/1024
    def kilobytes_pra_bytes(kilobyte):
        return kilobyte*1024
    def kilobytes_pra_megabytes(kilobyte):
        return kilobyte/1024
    def megabytes_pra_kilobytes(megabyte):
        return megabyte*1024

import hashlib,time,binascii
class Dados:
    """paraHex('L') # b'4c'
    paraString(b'4c') # 'L'
    StringHEX('L') # 0x4c
    HEXString('0x4c') # L
    HEXINT('0x4c') # 76
    HexByte(b'\xde\xad\xbe\xef') # 'deadbeef'
    ByteHex('deadbeef') # b'\xde\xad\xbe\xef'
    ArquivoHex('Semaforo.png') #"""
    def texto_pra_bytes(texto,codificacao='utf-8'):
        return bytes(texto,encoding=codificacao)
    def bytes_pra_texto(byteA,codificacao='utf-8'):
        return byteA.decode(codificacao)
    def paraHex(string,codificacao='utf-8'):
        return binascii.hexlify(string.encode(codificacao))
    def paraString(hexadecimal,codificacao='utf-8'):
        return binascii.unhexlify(hexadecimal).decode(codificacao)
    def char_pra_Hex(string):
        return hex(ord(string))
    def hex_pra_Char(hexadecimal):
        return chr(int(hexadecimal,16))
    def hexInt(Hexa):
        return int(str(Hexa),16)
    def HexByte(byte):
        return byte.hex()
    def ByteHex(string):
        return bytes.fromhex(string)
    def texto_para_MD5(entrada,codificacao='utf-8'):
        return hashlib.md5(entrada.encode(codificacao)).hexdigest()
    def bin_to_dec(binario):
        return int(str(binario),2)
    def ano_pra_binario(separador=' '):
        bin_ano=''
        for c in time.strftime('%Y'):
            bin_ano+=Dados.ascii_to_bin(c)+separador
        return bin_ano[:len(bin_ano)-1]
    def ascii_to_bin(asciiS):
        bi=bin(ord(asciiS))[2:]#Ou apenas return bin(ord(asciiS))
        if len(bi)==8:
            return bi
        while len(bi)!=8:
            bi='0'+bi
        return bi
    def bin_to_dec(binario):
        return int(str(binario),2)
    def texto_pra_binario(texto,retorno=str,separador=' '):
        binarios=[Dados.ascii_to_bin(car) for car in texto]
        return ''.join(binarios[i]+separador if i!=len(binarios)-1 else binarios[i] for i in range(len(binarios))) if retorno==str else retorno(binarios)
    def binarios_para_texto(binarios,separador=' '):
        return ''.join([chr(Dados.bin_to_dec(binario)) for binario in (binarios.split(separador) if type(binarios)==str else binarios)])


class Aritmetica:
    def ano_bissexto(ano):
        return ano%4==0 if str(ano)[::-1][:2][::-1]!='00' else ano%400==0
    def numeroPerfeito(numero):
        soma=1
        i=2
        while i*i<=numero:
            if numero%i==0:
                soma+=i+numero/i
            i+=1
        return soma==numero and numero!=1
    def primo(numero,divisor=2):
        resultado=''
        while resultado=='':
            if numero%divisor==0:
                resultado=f'{numero} é múltiplo de {numero/divisor} (Não é primo)'
            elif divisor>=numero:
                resultado=f'{numero} é primo'
            else:
                divisor+=2
        return resultado
    def resto_divisao(numero,divisor):
        return numero%divisor#math.fmod(numero,divisor)
    def impar(numero):
        return bool(numero%2)#!=0
    def par(numero):
        return numero%2==0#not bool(numero%2)
    def regra_de_tres(cima_1,cima_2,baixo_1):#Retorna o valor de baixo_2
        return baixo_1*cima_2/cima_1
    def porcentagem(porcento,numero):
        return numero/100*porcento
    def aumentar_porcentos(numero,para__porcentos):# 30 aumenta 10%==
        return numero/100*para__porcentos+numero
    def diminuir_porcentos(numero,para__porcentos):# 30 diminui 10%==
        return numero/100*para__porcentos-numero
    def mudanca_percentual(numero,n_subiu_para):#+ = aumento percentual, - = diminuicao percentual
        n=numero/100
        return -(n-n_subiu_para/100)/n*100
    def mmc(lista_numeros): #Entre com um array de numeros [19,6,2,56,7]
        calculou=False
        continuar=True
        resultado=1
        d=2     #Divisor
        lenght=len(lista_numeros)
        while continuar:
            for i in range(lenght):
                n=lista_numeros[i]
                if n%d==0 and n>1.0:
                    lista_numeros[i]=n/d
                    calculou=True
            if calculou:
                calculou=False
                resultado*=d
            else:
                d+=1    #Se nao calculou, aumentar o divisor ate conseguir calcular
            if sum(lista_numeros)/(lenght)<=1.0: #Verifica se todos os numeros foram calculados ate ou menor que 1
                continuar=False#break
        return resultado
    def mdc(lista_numeros):
        calculou=False
        continuar=True
        resultado=1
        d=2
        lenght=len(lista_numeros)
        while continuar:
            dividiu_todos=True
            for i in range(lenght):
                n=lista_numeros[i]
                if n%d==0 and n>1.0:
                    lista_numeros[i]=n/d
                    calculou=True
                else:
                    dividiu_todos=False
            if dividiu_todos:
                resultado*=d
            if calculou:
                calculou=False
            else:
                d+=1
            if sum(lista_numeros)/(lenght)<=1.0:
                continuar=False#break
        return resultado
    def fatorar(numero):
        fatorado=''
        divisor=2
        dividir=True
        while dividir:
            if numero%divisor==0 and numero>1.0:
                numero=numero/divisor
                fatorado+=f'{divisor}.'
            elif numero>1.0:
                divisor+=1
            else:
                dividir=False
        return fatorado[:-1]
    def triangulo_pascal(n): #Retorna uma string formatada do triangulo de pascal(Use print)
        return ''.join([('' if k else ' '*(n-i+1))+str(factorial(i)//(factorial(k)*factorial(i-k)))+' '+('\n' if k>=i else '') for i in range(n) for k in range(i+1)])

class Area:
    def diametro_pra_raio(diametro):
        return diametro/2
    def raio_pra_diametro(raio):
        return raio*2
    def circulo(diametro=None,raio=None):#-1 = Erro
        return (Constantes.pi*pow(diametro,2)/4) if diametro!=None else Constantes.pi*pow(raio,2) if raio!=None else -1
    def quadrado(lado):
        return lado*lado
    def retangulo(lado_maior,lado_menor):
        return lado_maior*lado_menor
    def triangulo(base,altura):
        return (base*altura)/2
    def pentagono(lado):
        return (5*(pow(lado,2)))/(4*tan(36))
    def hexagono(lado):
        return (6*pow(lado,2))/(4*tan(30))
    def poligono_regular(quantidade_lados,lado):
        return ((pow(lado,2)*quantidade_lados)/(4*tan(Constantes.pi/quantidade_lados)))
    def losango(diagonal_1,diagonal_2):
        return (diagonal_1*diagonal_2)/2
    def trapezio(base_maior,base_menor,altura):
        return (base_maior+base_menor)*altura/2
    def paralelogramo(base,altura):
        return base*altura
    def elipse(semi_eixo_maior,semi_eixo_menor):
        return Constantes.pi*semi_eixo_maior*semi_eixo_menor
    def coroa_circular(raio_maior,raio_menor):
        return Constantes.pi*(pow(raio_maior,2)-pow(raio_menor,2))
    def setor_circular(raio,angulo):
        return Constantes.pi*(pow(raio,2)*angulo)/360

#r = Raio; a = Aresta; h = Altura; d = Diâmetro; V = Volume
class Volume:
    def cilindro(raio,altura):
        return Constantes.pi*(raio**2)*altura
    def cone_cortado(altura,RAIO_MAIOR,raio_menor):#Ou copo/caneca
        return Constantes.pi*altura/3*(RAIO_MAIOR**2+RAIO_MAIOR*raio_menor+raio_menor**2)
    def cubo(aresta):
        return aresta**3#Ou aresta*aresta*aresta
    def paralelepipedo(largura_base,comprimento_base,altura):
        return largura_base*comprimento_base*altura
    def cone(raio,altura):
        return 1/3*Constantes.pi*(raio**2)*altura
    def prisma_triangular(altura,base):
        return 1/2*base*altura
    def piramida_base_triangular(altura,base):
        return 1/6*base*altura
    def piramide_base_quadrada(altura,comprimento_lado_base_quadrada):
        return 1/3*area_base(comprimento_lado_base_quadrada)*altura
    def piramide_base_hexagonal(altura,base):
        return sqrt(3)/2*area_base(base)*altura
    def area_base(comprimento_lado_base):
        return comprimento_lado_base**2
    def esfera(raio):
        return 4/3*Constantes.pi*(raio**3)

#Sequencia Fibonacci(Diferentes formas)
#fibo=CalcConv.Fibonacci()
class Fibonacci:
    def lista(s,termos):
        a,c=0,1
        sequencia=[]
        for i in range(termos+1):
            sequencia.append(a)
            c,a=a+c,c
        return sequencia
    def recursiva(s,n):
        if n<2:
            return n
        else:
            return s.recursiva(n-1)+s.recursiva(n-2)
    def iterativa(s,n):
        j,i=1,0
        for k in range(1,n):
            t=i+j
            i=j
            j=t
        return i


from math import sqrt
class EquacaoQuadratica:
    def delta(a,b,c):
        return b*b-4*a*c
    def bhaskara(a,b,c):
        a,b,c=(float(n) for n in (a,b,c))
        c,a=sqrt(EquacaoQuadratica.delta(a,b,c)),2*a #Raiz quadrada falha em numeros negativos
        return {'+':(-b+c)/a,'-':(-b-c)/a}

class Quilometragem:
    def quilometragem(litros,km_por_litro):
        return litros*km_por_litro
    def litros(valor,preco_p_litro):
        return valor/preco_p_litro
    def reais_gastos(litros,preco_p_litro):
        return litros*preco_p_litro
    def preco_por_litro(valor,litros):
        return valor/litros

#def calcularSobraConjunto(total,conjunto_1,conjunto_2,interseccao_dos_conjuntos):return total-(conjunto_1-interseccao_dos_conjuntos)+interseccao_dos_conjuntos+(conjunto_2-interseccao_dos_conjuntos)???
