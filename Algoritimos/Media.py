#coding:latin-1

#Media.py - github.com/Alien8652
# Algoritimo para criar um dicionário com nomes de alunos, notas e finalizar calculando a média desse aluno.

# Cria um list array com dicionários dentro para mais facilidade no acesso
alunos=[
        {'nome':'João Marcos Antonio','nota1':'nula','nota2':'nula','media':'nula'},
        {'nome':'José Maria Almeida','nota1':'nula','nota2':'nula','media':'nula'},
        {'nome':'Vinícius Henrique da Silva','nota1':'nula','nota2':'nula','media':'nula'},
        {'nome':'Gabriel dos Santos','nota1':'nula','nota2':'nula','media':'nula'}
]

# Itera na lista de array com enumerate(enumerate retorna o dicionário do aluno e um número de índice da lista array)
for indice,aluno in enumerate(alunos):
    print('Número do índice do aluno',indice)
    print('Nome:',aluno['nome'])
    print('Nota 1:',aluno['nota1'])
    print('Nota 2:',aluno['nota2'])
    print('Media:',aluno['media'])
    print('[----------------------->')

# Converte a entrada para inteiro(indíces devem ser números inteiros! 1 pode, 1.3 não pode!
ind=int(input('Digite o número do índice do aluno para alterar as notas:'))

# Obtém o tamanho da lista e verifica se o índice é válido comparando se ele é menor que zero ou maior/igual ao tamanho da lista.
if ind<0 or ind>=len(alunos):
    print('Aluno Não Está no Índice')
    exit(1)

# Troca , por . pq o python reconhece somente pontos como números flutuantes
alunos[ind]['nota1']=input('Digite um novo valor para nota 1:').replace(',','.')
alunos[ind]['nota2']=input('Digite um novo valor para nota 2:').replace(',','.')

# Try pega as exceções caso digitem um valor errado e mostra uma msg de aviso,
# caso esteja certo, ele calcula a média e imprime a média e se foi aprovado ou não
try:
    media=( float(alunos[ind]['nota1'])+float(alunos[ind]['nota2']) ) /2.0 #(nota1 + nota2) / 2 provas
    alunos[ind]['media']=media
    print(f"A média do aluno {alunos[ind]['nome']} foi {alunos[ind]['media']}!")
    print('Aluno Aprovado!' if float(alunos[ind]['media'])>=7 else 'Aluno Reprovado! Deve fazer o exame!')
except:
    print('Digite somente números na nota 1 ou 2!, não foi possível calcular a média!')
