def taxaMensalPraAnual(taxa):return taxa*12
def taxaAnualPraMensal(taxa):return taxa/12

print(taxaAnualPraMensal(taxaMensalPraAnual(30)))

def capitalAplicado(valorJuros,jurosMensalPorcentagem,meses):return valorJuros/((jurosMensalPorcentagem/100)*meses)

print(capitalAplicado(40,7,9))

#1% = /100, 10% = /10, 100% = /1
def gorjeta(total_da_conta,porcentagem=10):return total_da_conta+total_da_conta/porcentagem

conta_restaurante=78.50
print(f'{conta_restaurante} > 10% > {gorjeta(conta_restaurante)}')#78.50+7.85

#A msm conta invertida(+ > -) tbm serve pra aplicar descontos
def desconto(valor,porcentagem=10):return valor-valor/porcentagem

print(desconto(conta_restaurante))

#Formata floats como 123.456789 para 123.45
def formataFloat(nfloat,l=2):
    vfloat=str(nfloat)
    vf=vfloat.find('.')
    if vf==-1:return vfloat
    else:return vfloat[:vf]+vfloat[vf:vf+l+1]

def gerarNotaFiscal(produtos,mercado='Mercadao Utilidades'):
    tela=79
    nota=f'[{mercado}]'.rjust(tela//2+(len(mercado)+2)//2)
    nota+='\n'
    nota+=('-'*tela)+'\n'
    total_compra=0
    for i,nome in enumerate(produtos.keys()):
        i+=1
        preco=produtos[nome]['Preco']
        qto=produtos[nome]['Quantidade']
        pxq=preco*qto
        prod=f'{i} {nome}'
        prod=prod+f'{preco}x{qto}'.rjust(round((tela/100)*67)-len(prod))
        pxqs=formataFloat(pxq)
        nota+=prod+f'{pxqs}\n'.rjust((tela+1)-len(prod))
        total_compra+=pxq
    nota+=('-'*tela)+'\n'
    nota+=f'Total:'+formataFloat(total_compra).rjust(tela-6)
    return nota

produtos={
        'Arroz':{'Preco':18.99,'Quantidade':2},
        'Feijao':{'Preco':10.60,'Quantidade':1},
        'Peito Frango 1kg':{'Preco':13.90,'Quantidade':1},
        'Picanha Acougue KG 78,99':{'Preco':0.07899,'Quantidade':574}#574 gramas
}
print(gerarNotaFiscal(produtos))
