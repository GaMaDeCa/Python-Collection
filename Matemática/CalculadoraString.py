# coding: latin-1

# Avaliador de expressão aritmética por string(Evaluator) - github.com/Alien8652 07/02/2022
# Uso:
#   python CalculadoraString.py "2+34-4*3/5+2"
#   ou apenas inicie o script.
# Simples, suporta apenas operações de adição, subtração, multiplicação, divisão e exponenciação
# + - * / ^
import sys

# ignorar_outros_caracteres - Um filtro customizado que barra caracteres indesejados.
# Ignora qualquer caractere que não esteja na string nao_ignorar e retorna somente os que estão no nao_ignorar(Em ordem),
# e reconhece se a expressão começa com um caractere inválido ou termina com um caractere inválido.
def ignorar_outros_caracteres(expressao_aritmetica, nao_ignorar='0123456789-+/*^',nao_deve_ter_inicio_fim='+-/*^'):
    for err in nao_deve_ter_inicio_fim:
        if expressao_aritmetica.endswith(err) or expressao_aritmetica.startswith(err):
            return 'Erro! Expressão começa ou termina com caracteres inválidos!'
    nova_expressao_aritmetica=''
    for car in expressao_aritmetica:
        if car in nao_ignorar:
            nova_expressao_aritmetica+=car
    if nova_expressao_aritmetica=='':
        return 'Erro! Expressão não reconhecida!'
    return nova_expressao_aritmetica

# splitRegex - Um split regex customizado que retorna o valor em seu tamanho atual(Sem os espaços vazios '', nulos da array)
# Uso:
#   string='2452+3232-3243+433/2222*222'
#   splitRegex(string,'+-/*','int')
#   splitRegex(string,'0-9')
# TODO: Criar suporte a cortes com números diferentes, tipo 3-7 ou G-T.
def splitRegex(stringParaArray,regexString,tipo='str'):
    if regexString=='0-9':
        regexString='0123456789'
    elif regexString=='A-Z':
        regexString='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    elif regexString=='a-z':
        regexString='abcdefghijklmnopqrstuvwxyz'
    arrayStr=[]
    acumuladorStr=''
    for caractere in stringParaArray:
        acumuladorStr+=caractere
        for regexStr in regexString:
            if caractere==regexStr:
                acumuladorStr=acumuladorStr[:-1]
                if acumuladorStr!='':
                    if tipo.lower()=='str':
                        arrayStr.append(acumuladorStr)
                    else:
                        arrayStr.append(int(acumuladorStr))
                    acumuladorStr=''
    if acumuladorStr!='':
        if tipo.lower()=='str':
            arrayStr.append(acumuladorStr)
        else:
            arrayStr.append(int(acumuladorStr))
    return arrayStr


# calcularString - Dada uma lista de números e uma lista de operações('+-*/^') ele calcula usando a regra aritmética em ordem(1:* ou /,2:+ ou -)
# Uso:
#   calcularString(['4','1','2','7','3'],['+','-','*','/'])
def calcularString(n,o):
    dim=0
    for i in range(len(o)):
        if o[i-dim]=='*':
            n[i-dim]*=n[i-dim+1]
            n.pop(i-dim+1)
            o.pop(i-dim)
            dim+=1
        elif o[i-dim]=='^':
            n[i-dim]**=n[i-dim+1] # ou pow(n[i-dim],n[i-dim+1])
            n.pop(i-dim+1)
            o.pop(i-dim)
            dim+=1
        elif o[i-dim]=='/':
            n[i-dim]/=n[i-dim+1]
            n.pop(i-dim+1)
            o.pop(i-dim)
            dim+=1
    dim=0
    for i in range(len(o)):
        if o[i-dim]=='+':
            n[i-dim]+=n[i-dim+1]
            n.pop(i-dim+1)
            o.pop(i-dim)
            dim+=1
        elif o[i-dim]=='-':
            n[i-dim]-=n[i-dim+1]
            n.pop(i-dim+1)
            o.pop(i-dim)
            dim+=1
    return n

# calculadoraString - Usa as funções acima para calcular e trata de algumas exceções.
# Uso:
#   calculadoraString('4+1-2*7/3^2')
def calculadoraString(expressao_aritmetica): # ou String
    expressao_aritmetica=ignorar_outros_caracteres(expressao_aritmetica)
    if expressao_aritmetica.find('Erro')!=-1:
        return expressao_aritmetica
    if expressao_aritmetica==None or expressao_aritmetica=='':
        return 'Erro! Expressão vazia!'
    numeros=splitRegex(expressao_aritmetica,'+-/*^','int') # Do exemplo retornaria o array [2,5,15,2,4] de length 5
    operacoes=splitRegex(expressao_aritmetica,'0-9') # Do exemplo retornaria o array ['*','+','/','*'] de length 4
    return calcularString(numeros,operacoes)

def principal():
    print('Simbologia dos operadores: + Adição,- Subtração,/ Divisão,* Multiplicação,^ Exponenciação\nExemplo de conta: 2*5+3^2-8+15/2*4-10\nResultado: 31.0')
    expressao_aritmetica=input('Digite alguma conta aritmética(Digite S para sair)>>>')
    if expressao_aritmetica.upper()=="S" or expressao_aritmetica.upper()=="SAIR":
        exit()
    resultado=calculadoraString(expressao_aritmetica)
    print(resultado) # ou print(eval(expressao_aritmetica))
    print("\n")
    principal()

if __name__ == "__main__":
    try:
        expressao_aritmetica=sys.argv[1]
        resultado=calculadoraString(expressao_aritmetica)
        print(resultado) # ou print(eval(expressao_aritmetica))
    except Exception:
        principal()

# calculadoraSimples - Usa o eval() do python e o método ignorar_outros_caracteres para calcular as expressões.
# Uso:
#   calculadoraSimples('42+53-2/6*4')
#def calculadoraSimples(string):
#    expressao_aritmetica=ignorar_outros_caracteres(string)
#    return (eval(expressao_aritmetica) if expressao_aritmetica.find('Erro')==-1 else expressao_aritmetica)


# Testes - Código errado, ele calcula sem obedecer a ordem aritmética, mas foi o script base que me guiou.
# calcularString(['2','2'],['+'])
#def calcularString(numeros,operacoes):
#    numi=1
#    conta=numeros[0]
#    for opera in range(0,len(operacoes)):
#        if operacoes[opera]=='+':
#            conta+=numeros[numi]
#            numi+=1
#        elif operacoes[opera]=='-':
#            conta-=numeros[numi]
#            numi+=1
#        elif operacoes[opera]=='/':
#            conta/=numeros[numi]
#            numi+=1
#        elif operacoes[opera]=='*':
#            conta*=numeros[numi]
#            numi+=1
#    resultado=str(conta)
#    if resultado.endswith('.0'):
#        resultado=resultado[:-2]
#    return resultado
