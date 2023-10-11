#Um codificador/decodificador de inteiros 5 bits
#Baseado nessa resposta> https://stackoverflow.com/questions/20720098/how-does-this-print-hello-world

def Bin5Dec2Long(texto,bits=5):
 texto=''.join([c for c in texto.lower() if c.isalpha()or' '==c])#filtro basico
 bins=[]
 for car in texto:
  if car==' ':
   bins.append('1'*bits)
   continue
  o=ord(car)-32
  o|=64
  o&=31
  bo=bin(o)[2:]
  bins.append(('0'*(bits-len(bo)))+bo)
 return int(''.join(bins[::-1]),2)

def long5Dec(l,bits=5):
 r=[]
 while l>0:
  r.append(((l&31|64)%95)+32)
  l>>=bits
 return r

def printLong5(l,fim='\n',bits=5):
 for car in map(chr,long5Dec(l)):
  print(car,end='')
 print(end=fim)


def long5Enum(l,bits=5):
 lbin=bin(l)[2:][::-1]
 lchr=''.join([m for m in map(chr,long5Dec(l))][::-1])
 lbin=[lbin[i:i+bits]for i in range(0,len(lbin),bits)]
 lbin=[('0'*(bits-len(lb)))+lb for lb in lbin]
 def rev(lb):return lb[::-1]
 lbin=[lb for lb in map(rev,lbin)][::-1]
 for caractere,binario in zip(lchr,lbin):
  print(caractere,binario)

l=Bin5Dec2Long('ola mundo')
printLong5(l)
long5Enum(l)

print()

k=Bin5Dec2Long(' abcdefghijklmnopqrstuvwxyz')
printLong5(k)
long5Enum(k)
