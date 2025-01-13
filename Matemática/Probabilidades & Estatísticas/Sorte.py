# coding: latin-1
# [Sorte] - Gabriel Matheus de Castro(github.com/GaMaDeCa)
# Calcula a probabilidade de um evento acontecer baseado
# em dados anteriores(histórico), exibindo em porcentagem
# a chance de outras probabilidades.

# Usa os dados antigos pra obter melhor resultado(Exemplo : Em 10 jogadas caiu 3 vezes em cara e 7 em coroa,
# entao provavelmente tera mais chances de cair coroa(58%))

#Probabilidade de uma moeda(2 lados)
#Uma moeda e lançada 10 vezes pow(2,10)=1024)
#                             2^10/2 = Lados^Jogadas/Lados=512
#                             512/1024=0,5 = 50%
#Caiu 3 vezes em cara
#Caiu 7 vezes em coroa
#Qual e a chance da proxima jogada?
#P=3/7=0,42
#=42% de cair cara e 58% de cair coroa
#Probabilidade de um dado(6 lados)
#Lancou 10 vezes
#Caiu 3 - 2 (3/10=30% = "2")
#Caiu 3 - 5 (3/10=30% = "5")
#Caiu 1 - 6 (1/10=10% = "6")
#Caiu 1 - 1 (1/10=10% = "1")
#Caiu 2 - 4 (2/10=20% = "4")
#P=
# Se for uma moeda entao coloque 2
# Caso seja um dado coloque 6

porcentagens=[]
eventos=0
resultados_possiveis=0
ini=0
while True:
    if ini>0:
        print('Digite somente números! e somente números maiores que 0')
    else:
        ini+=1
    try:
        print('\nExemplo: Um dado têm 6 lados, então são 6 resultados possíveis')
        resultados_possiveis=int(input("Resultados possíveis : "))
        if resultados_possiveis==0:
            continue
        print('\nExemplo : O dado foi lançado 10 vezes, então são 10 eventos/jogadas')
        eventos=int(input("Eventos : "))
        if eventos==0:
            continue
    except ValueError:
        continue
    break

#probabilidade=round(eventos/resultados_possiveis*100)
#possibilidades=pow(resultados_possiveis,eventos)
#chances=possibilidades/resultados_possiveis
#print(f'\nProbabilidade geral: {probabilidade}%')
#print(f'Há {possibilidades} possibilidades para este jogo!')
#print(f'{chances}') TODO
#print(f'Cada jogada representa {round(chances/possibilidades*100)}%')
def contar_dados(resultados_possiveis,eventos,dados=[],contador=0):
    while True:
        try:
            dado=int(input(f"\nResultado do {contador+1}º evento : "))
        except ValueError:
            print('Digite somente números!')
            continue
        if dado==0 or dado>resultados_possiveis:
            print(f'Dado inválido! Digite um valor entre 0 e {resultados_possiveis}')
        else:
            dados.append(dado)
            contador+=1
            if contador>=eventos:
                break
    return dados

dados=contar_dados(resultados_possiveis,eventos)
dados.sort(reverse=True)
dados_sem_duplicata=list(dict.fromkeys(dados))
duplicata_contadas=dict((i, dados.count(i)) for i in dados)

print('\n')

for i in range(0, len(dados_sem_duplicata)-1):
    repetido=duplicata_contadas[dados_sem_duplicata[i]]
    print(f'{dados_sem_duplicata[i]} tem %{round(repetido / eventos * 100)} de chance de sair no próximo evento/jogada')
