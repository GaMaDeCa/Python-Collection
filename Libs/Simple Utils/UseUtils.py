#coding:latin-1

# Utils - Gabriel Matheus de Castro(2020)
# Tem boas utilidades, outras não tão utéis mas que podem servir para o aprendizado, este é um script que mostra como usá-las,
# recomendo para quem está aprendendo analisar o script Utils.py também.

#Exemplos de usos abaixo:

from Utils import Texto
#Ou Utils.Texto()


# Chame a classe primeiramente:
tfun=Texto()


# Verificar se um texto é um palíndromo
tfun.palindromo('Socorram-me, Subi No Ônibus em Marrocos!')

# Inverter um texto
tfun.inverter('Ola Mundo')

# Aumentar, diminuir, transformar em título o texto inserido
tfun.maiusculo('Ola Mundo')
tfun.minusculo('Ola Mundo')
tfun.titulo('ola mundo')

# Filtra o texto inserido permitindo somente os caracteres do filtro
tfun.filtrar('Testando123','0123456789') # Obtém somente os números do texto

# É possível definir um filtro dessa forma também para automatizar a tarefa
tfun.FILTRO='aeiou' # Somente vogais serão válidas
tfun.filtrar('Ola Mundo')


# Obter uma lista de palavras em um texto
lista_palavras=tfun.getPalavras('Ola mundo, testando 123(Isso é um teste!), palavra-chave')

# Obtém a quantidade de palavras em um texto inserido
tfun.contar_palavras('Ola mundo, testando 123(Isso é um teste!), palavra-chave')

# Obtém todos os caracteres da tabela ASCII
AsciiTable=tfun.getAsciiTable()


#Corta o texto a cada numero de caracteres
tfun.cortar_texto('abcdefghijklmnopqrstuv',3)

#Corta o texto a cada caractere-chave
tfun.cortar_texto_por_chave('Ola-Mundo','-')

# Remove caracteres duplicados de um texto
tfun.removerCharDuplicado('aaabbbcccccddefghijkklmnopp')

# Retorna uma tupla com duas listas de palavras mais comuns(repetidas no texto) e quantidade da repetição
maisComuns=tfun.mais_comum(lista_palavras)
maisComuns[0] # Palavras
maisComuns[1] # Contagem

# Também é possível limitar a saída, exemplo, as 3 palavras mais comuns do texto
tfun.mais_comum(lista_palavras,3)




# Junta uma lista em uma única string
tfun.sJoin(['Ola',' ','Mundo'])

# Remove acentos num texto inserido
tfun.removerAcentos('Olá Mûndõ!')

# É possível limitar para apenas alguns acentos
tfun.removerAcentos('Olá Mûndõ!','ûõ','uo')

# Remove caracteres especiais de um texto
tfun.removerCaracteresEspeciais(':^`[Ola]--{Mundo}')

# Remove números do texto
tfun.removerNumeros('Testando 123')

# Extrai dados de um texto retornando uma array de letras de acordo com a expressão REGEX inserida
tfun.extrairDados('ABCDEFGHI',r'[AEI]')


# Gerador de WordList, sem libs, gera palavras começando com a, b, c, aa, ab, ac, etc...
tfun.wordlist('abc',3) # Caracteres, Profundidade



from Utils import TradutorRapido

tr=TradutorRapido()

# Para criar uma tradução insira uma array como as chaves e outra array bidimensional com as arrays de traduções(Devem ter o mesmo tamanho).
tr.genTrad(['msg_ola'],[['Hello World','Ola Mundo']])
#             Chave       Tradução 0    Tradução 1

# Mensagem em inglês
print(tr.traduzir('msg_ola'))#Padrão tr.LINGUA.PADRAO=0

# Configure a tradução manualmente
tr.LINGUA.PORTUGUES=1
tr.setLingua(tr.LINGUA.PORTUGUES)

# Mensagem em português.
print(tr.traduzir('msg_ola')) #Caso ocorra algum erro na tradução, seja por má configuração das linguagens ou a tradução não exista, retornará ''.

# Variáveis acessíveis pela classe Texto e seus valores
LETRAS_VOGAIS='aeiou'
LETRAS_CONSOANTES='bcdfghjklmnpqrstvwxyz'
LETRAS_ALFABETO='abcdefghijklmnopqrstuvwxyz'
LETRAS_ALFABETO_COM_ACENTOS='aÃ¡Ã Ã¢Ã£Ã¤bcÃ§deÃ©Ã¨ÃªÃ«fghiÃ­Ã¬Ã®Ã¯jklmnÃ±oÃ³Ã²Ã´ÃµÃ¶pqrstuÃºÃ¹Ã»Ã¼vwxyÃ½Ã¿z'
LETRAS_ACENTUADAS='Ã¡Ã©Ã­Ã³ÃºÃ Ã¨Ã¬Ã²Ã¹ÃÃ‰ÃÃ“ÃšÃ€ÃˆÃŒÃ’Ã™Ã£ÃµÃ±ÃƒÃ•Ã‘Ã¢ÃªÃ®Ã´Ã»Ã‚ÃŠÃŽÃ”Ã›Ã¤Ã«Ã¯Ã¶Ã¼Ã„Ã‹ÃÃ–ÃœÃ¿Ã½ÃÃ§Ã‡'
LETRAS_SEM_ACENTOS='aeiouaeiouAEIOUAEIOUaonAONaeiouAEIOUaeiouAEIOUyyYcC'
NUMEROS='0123456789'
NUMEROS_SOBRESCRITOS='â°Â¹Â²Â³â´âµâ¶â·â¸â¹'
NUMEROS_SUBSCRITOS='â‚€â‚â‚‚â‚ƒâ‚„â‚…â‚†â‚‡â‚ˆâ‚‰'
SINAIS_MATEMATICOS_SIMPLES='+âˆ’Ã—Ã·'
SINAIS_MATEMATICOS_AVANCADOS='âˆšÂ±Î£'
SIMBOLOS_SOBRESCRITOS='âºâ»â¼â½â¾'
SIMBOLOS_SUBSCRITOS='â‚Šâ‚‹â‚Œâ‚â‚Ž'
ACENTOS='Â´`^~Â¨'
SIMBOLOS='(){}[]<>.,-_;:|\\/#!?*@&%$=+\'"ï¿½'
ESPACO=' '
GRAUS='Â°'
INDICADOR_ORDINAL_A='Âª'
INDICADOR_ORDINAL_O='Âº'
FILTRO=None


#É possível verificar todos os métodos e classes dentro uma classe-lib com o método dir(classe):
import Utils
dir(Utils)

#Classe númerica com alguns métodos da lib math
N=Utils.Numero()

#Número PI
N.PI

#Arredonda o valor pro mais próximo(2.4 arredonda pra 2, 2.6 arredonda pra 3)
N.arredondar(2.6)

#Arredonda o valor para menos independente do valor mais próximo(2.6=2)
N.arredondarBaixo(2.6)

N.arredondarCima(2.4)#3

N.raizQuadrada(4)

#Troca o atributo de menos para mais e mais para menos(-2=2)
N.trocar_atributo(-2)

#Troca qualquer valor para positivo+(-0=+0)
N.atribuir_positivo(-2)

N.atribuir_negativo(2)

#Calcula potencia(2^4=2*2*2*2=16)
N.potencia(2,4)

#Soma números de uma lista(2+3+5=10)
N.somar_lista([2,3,5])
