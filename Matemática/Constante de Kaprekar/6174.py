
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 #    6174.py - Criado por Gabriel Matheus de Castro 09/04/2021 (22:26)    #
 #                                                                         #
 #       Executa a Rotina de Kaprekar sem limites de digitos,              #
 #       calculando desde o menor ate o maior numero possivel.             #
 #                                                                         #
 #         Constantes de 4 digitos = 6174(Maximo 7 iteracoes)              #
 #               e 3 digitos = 495(Maximo 6 iteracoes)                     #
 #                                                                         #
 #  IMPORTANTE! - 5 digitos ou mais resultam em varias constantes, entao   #
 #   o script entraria em um loop infinito, a cada iteracao sera feita     #
 #    uma pergunta se o usuario deseja continuar ou parar a execucao.      #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

 # Fonte : https://pt.wikipedia.org/wiki/6174

print("\n------Constante Kaprekar 6174------\n\nDigite um numero de 4 ou 3 digitos diferentes.\n\nExemplo : 3321 ou 123, 3322 ou 3333 nao pode.\n")

def fim(iteracoes):
    print("\nFim! Foram feitas " + str(iteracoes) + " iteracoes!")
    quit()

def somente_numeros():
    numero_str=input("Digite o numero : ")
    if numero_str.upper()=='N':
        fim(0)
    try:
        teste_int=(int(numero_str))
        return numero_str
    except ValueError:
        print("\nErro! Digite somente numeros ou digite N para sair!")
        somente_numeros()

numero=somente_numeros()

modo_exibir=input('Exibir somente resultados? (S/N) : ')
    
resultado=""
iteracao=0
listar_numeros_antigos=[numero]

print("\n" + str(iteracao) + " - " + numero)

while True:
    crescente=''
    decrescente=''

    listar_numero=[numero[it] for it in range(0, len(numero))]
    
    listar_numero.sort(key=int)
    for it in range(0, len(numero)):
        crescente+=((str(int(listar_numero[it]))))

    listar_numero.sort(key=int, reverse=True)
    for it in range(0, len(numero)):
        decrescente+=(((str(int(listar_numero[it])))))

    resultado=(int(decrescente) - int(crescente))
    
    numero=str(resultado)
    iteracao+=1

    if modo_exibir.upper()=='S':
        exibir_resultado=("\n" + str(iteracao) + " - " + numero)
    else:
        exibir_resultado=("\n" + str(iteracao) + " - " + numero + "  = " + decrescente + " - " + crescente)

    print(exibir_resultado)
    
    if numero=='0':
        print("\nErro! Digite pelo menos dois numeros diferentes!")
        fim(iteracao)

    for numeros_antigos in range(0, len(listar_numeros_antigos)):
        if numero==listar_numeros_antigos[numeros_antigos]:
            if len(numero)<=4:
                fim(iteracao)
            else:
                print('\nLoop detectado!   : ' + str(numeros_antigos) + ' - ' + str(listar_numeros_antigos[numeros_antigos]) + ' = ' + str(iteracao) + ' - ' + str(numero))
                loopar=input('\nContinuar a execucao? (S/N) : ')
                if loopar.upper()=='N':
                    fim(iteracao)
                break
    listar_numeros_antigos+=[numero]
