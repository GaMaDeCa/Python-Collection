from random import randint as rint
def gerarNovaPlaca(mercosul=False,carro=True):
 placa=''
 if mercosul:
  n=str(rint(0,9))
  letra=chr(rint(65,90))
  nums=''.join([str(rint(0,9))for i in range(2)])
  placa=''.join([chr(rint(65,90))for i in range(3)])+((n+letra+nums)if carro else(nums+letra+n))
 else:
  letras=''.join([chr(rint(65,90))for i in range(3)])
  numeros=''.join([str(rint(0,9))for i in range(4)])
  placa=letras+numeros
 return placa

def isMotoMercosul(placa):return placa[5].isalpha()
def isMercosul(placa):return placa[4].isalpha()or placa[5].isalpha()

banco_de_placas=[]
#Gerar 100 placas de estilos aleatorios: antigo, mercosul novo, de carro e de moto
for i in range(100):
 estilo=bool(rint(0,1))
 carro=bool(rint(0,1))
 placa=gerarNovaPlaca(estilo,carro)
 while placa in banco_de_placas:
     placa=gerarNovaPlaca(estilo,carro)
 banco_de_placas.append(placa)

for placa in banco_de_placas:
 print('Carro? '+('Nao'if isMotoMercosul(placa)else'Sim')+', Mercosul? '+('Sim'if isMercosul(placa)else'Nao')+', Placa:'+(placa if isMercosul(placa)else placa[0:3]+'-'+placa[3:]))
