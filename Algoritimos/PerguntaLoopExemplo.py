# coding: latin-1

# Pergunta em loop ao usuário com uma mensagem específica.
def perguntar(acoes,opcoes,mensagem=''):
    if (len(acoes)!=len(opcoes)):
        return 'Erro! A quantidade de ações deve ser igual a de opções!'
    pergunta=input(mensagem)
    for i in range(0,len(acoes)):
        if pergunta==opcoes[i]:
            return eval(acoes[i])
    return perguntar(acoes,opcoes,mensagem)


# Defina as funções primeiro
def funcao0():
    print('Ola Mundo!')
    return 'Fim da funcao0'

def funcao1():
    print(7+7)
    return 'Fim da funcao1'

#Uso:
def exemplo():
    #acoes=['funcao0()','funcao1()']
    #opcoes=['0','1']                   # IMPORTANTE: É melhor usar uma string pra n dar erro
    #mensagem='Digite algum número para executar alguma função\n 0 = funcao0()\n 1 = funcao1()\n>'
    resultado=perguntar(['funcao0()','funcao1()'],
                        ['0','1'],
                        'Digite algum número para executar alguma função\n 0 = funcao0()\n 1 = funcao1()\n>')
    print(resultado)

exemplo()
