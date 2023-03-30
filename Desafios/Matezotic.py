#coding:latin-1

# Multiplica dois números utilizando somente soma, subtração e a regra de sinais
def multiplicaSoma(n1,n2):
    resultado=0
    n1=-n1 if(n1<0 and n2<0)or(n2<0 and n1>0)else n1
    while n2!=0:
        resultado+=n1
        if n2<0:
            n2+=1
        else:
            n2-=1
    return resultado

# Divide dois números usando somente a subtração, soma e a regra de sinais
# TODO>Suporte a números quebrados, se a o resto da divisão != 0 então retorna um erro(retorna o resultado sem os números quebrados)
def diviSub(n1,n2):
    #n1_t=float(n1)
    bolha=0
    while n1>0:
        bolha+=1
        n1-=n2
    if n1!=0:#dados_para_testes=f'{n1},{n2},{n1_t}'
        return f'{bolha-1}'#-1 arredonda o numero pra baixo(pra ficar "mais certo"),{diviSub(-n1,n1_t)}'
    return bolha

def exponencial(n1,n2):
    r=n1
    for i in range(n2-1):
        r=multiplicaSoma(n1,r)
    return r

def fatorial(n,limite=1):#Exemplo: n=6, limite=3>6*5*4*3
    n_tmp=n
    while n_tmp>limite:
        n_tmp-=1
        n*=n_tmp
    return n

def raiz(n):
    i=0
    c=True
    while c:
        m=i*i
        if n==m:
            c=False
        elif m>n:
            i-=1#TODO>Calcular numero quebrado(Testar:raiz rápida=n**(0.5))
            c=False
        else:
            i+=1
    return i

def multiplicacaoRussa(n,n2):
    tmp=0
    while n>1.0:
        if n%2==0:
            n/=2
            n2*=2
        else:
            tmp=n2
            n-=1
    return n2+tmp

#Método Pitágoras para calcular potências: 5**2 = 1+3+5+7+9 = 25
def potenciaMetodoPitagoras(numero,vezes):
    n=1
    soma=n
    for i in range(numero-1):
        n+=2
        soma+=n
    return soma

# Mega Sena (60 possibilidades)
# Jogada = 6 números
#resultado=analise_combinatoria(60,6) #50.063.860
#possibilidade_de_acertar(resultado) #TODO>Corrigir
def analise_combinatoria(total_possibilidades,eventos):
    return fatorial(total_possibilidades,(total_possibilidades-eventos)+1)/(fatorial(eventos))
#          fatorial(total_possibilidades)/(fatorial(eventos)*fatorial(total_possibilidades-eventos))

def possibilidade_de_acertar(resultado):return(1/resultado)*100

def checaParImpar(n):return'Impar'if n%2 else'Par'

#Calcula a média dada uma lista de inteiros
#media([5,7,2,7,10,3])
def media(lista):return sum(lista)/len(lista)

#Formula do numero triangular:formula_n_triang.txt
def numeroTriangular(n):return sum(range(1,n+1))

def multiploNove(numero):return 12345679*numero if(numero>=9 and numero<=81)and numero%9==0 else'Digite um número entre 9 e 81 que seja múltiplo de 9!'

#Numeros amigaveis(Numeros cuja determinada fórmula resulta em um ao outro):
#220 é dividido sem resto por 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 e 110,
#cuja soma de todos os divisores é 284, e 284 fazendo a mesma conta a soma fica 220(1, 2, 4, 71 e 142).
#Fermat descobriu também o par 17296 e 18416.
#Descartes descobriu o par 9363584 e 9437056.
def numerosAmigaveis(numero):
    e_amigo_de=0
    divisores=1
    for i in range(numero-1):
        if numero%divisores==0:
            e_amigo_de+=divisores
        divisores+=1
    numero_igual=0
    divisores=1
    for i in range(e_amigo_de-1):
        if e_amigo_de%divisores==0:
            numero_igual+=divisores
        divisores+=1
    return numero_igual,e_amigo_de

#print(''.join([f'{n}*{i}={n*i}\n' for i in range(1,11)])) #Função antiga de printar tabuada
#print(gerarTabuada(4,6,3)) #Printa uma tabuada de 3 a 6 da tabuada do 4
def gerarTabuada(numero,repetir_ate=10,minimo=1,msg_inicial='[+]---Resultados---+>:\n',msg_final='[+-------FIM-------+]',marcador='*'):
    tab=msg_inicial
    for i in range(minimo,repetir_ate+1):
        resultado=i*numero
        tab+=marcador+f'{i} x '.rjust(10,' ')+f'{numero} = '+f'{resultado}\n'.rjust(4,' ')
    return tab+msg_final
