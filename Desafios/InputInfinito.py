#coding:latin-1

def inputMap(funcao,mensagem,msg_erro='Erro:\n Entrada inválida! Insira um valor válido pro tipo de dado requerido!\n'):
    try:
        valor=funcao(input(mensagem))
    except ValueError: # Exception:
        if msg_erro!=''or msg_erro!=None:print(msg_erro,end='')
        valor=inputMap(funcao,mensagem,msg_erro)
    return valor

#Possíveis tipos de dados:int,str(esse daqui não precisa),bool,float ou uma função própria definida:
#Função própria: converte entrada pra inteiro e se não for um número par volta um erro(ValueError).
#def intPar(entrada):
# n=int(entrada)
# if n%2!=0:raise ValueError()
# return n
#inputMap(intPar,'....
resultado=inputMap(int,'Digite um número: ',msg_erro='\nInsira somente números inteiros(0-9)!\n\n')
print(resultado)
print(type(resultado))
