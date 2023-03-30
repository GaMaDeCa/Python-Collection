#C0d1f1c4 0 73x70 c0m 4l6um45 l37r45 7r0c4d45 p0r num3r05, 3 d3c0d1f1c4.
#4u70r: 648r13l M47h3u5 d3 C457r0 (ob/iz/zozz)
#Exemplo de Uso:
# codificar('Algum texto')#'4l6um 73x70'
# decodificar('4l6um 73x70')#'algum texto'
LETRAS='AEIOZSTBG'#len=9
NUMEROS='431025786'
def letraPraNumero(c):return NUMEROS[LETRAS.find(c.upper())]if c.upper()in LETRAS else c
def numeroPraLetra(c):return(LETRAS[NUMEROS.find(c)].lower()if c in NUMEROS else c)
def codificar(texto):return''.join([letraPraNumero(c)for c in texto])
def decodificar(texto):return''.join([numeroPraLetra(c)for c in texto])
if __name__=='__main__':
 i=input('Codificar/Decodificar?').lower()
 print(decodificar(input('Texto para decodificar:'))if i.startswith('d')else codificar(input('Texto para codificar:'))if i.startswith('c')else'')
