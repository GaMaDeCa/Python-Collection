# Teste
# O caule ta meio torto ;_;

a=input('Caractere: ') # '*'
espaco=' '
tamanho=int(input('Tamanho: ')) # 10

for i in range(tamanho):
    print(f'{(espaco*(tamanho-i))}{a if i==0 else a*i*2+a}')
v=round(tamanho/2)+(-1 if tamanho==3 else 2 if tamanho==6 else 2 if tamanho>9 else 1 if tamanho>2 else 0)+(1 if tamanho>10 else 0)
aa=round(tamanho/4)+(1 if tamanho>9 else 0)
print(f'{(espaco*(tamanho+(1 if tamanho==3 else 0)-aa))}{a*v}\n'*(aa+(1 if tamanho>4 else 1 if tamanho==2 else 0)))

# Arvore de Natal ou uma Seta?
