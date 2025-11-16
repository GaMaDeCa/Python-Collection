#latin-1

from datetime import datetime as dt
# Documento sem Valor Fiscal

RESTAURANTE, ENDERECO, CLIENTE, MESA, OPERADOR, ITEMS, DATA='nome_do_restaurante', 'endereco', 'nome_cliente', 'mesa', 'operador', 'items_pedido', 'data_entrada'
dados={
  RESTAURANTE: "Cupim Grill",
  ENDERECO: "Rua Aviação, nº 1234",
  CLIENTE: "Consumidor", #Nome padrão
  MESA: "Mesa 1",
  OPERADOR: "Caixa 1 - {}",
  DATA: None,
  ITEMS: [] #Pedidos
}
dados[DATA]=dt.now()
NOME, PRECO, QUANTIDADE='nome_do_item', 'valor', 'quantidade'
#"Sacola" de items/itens???¿¿¿
items={
  0:{NOME: "Suco Copo(300 ml)", PRECO: 7.50, QUANTIDADE: 0},
1:{NOME: "Suco Jarra(1 L)", PRECO: 15.00, QUANTIDADE: 0},
2:{NOME: "Refrigerante Lata(350 ml)", PRECO: 4.00, QUANTIDADE: 0},
3:{NOME: "Refrigerante 600 ml", PRECO: 6.00, QUANTIDADE: 0},
4:{NOME: "Refrigerante 1 Litro", PRECO: 10.00, QUANTIDADE: 0},
5:{NOME: "Refrigerante 2 Litros", PRECO: 17.00, QUANTIDADE: 0},
6:{NOME: "Marmitex(Grande)", PRECO: 24.99, QUANTIDADE: 0},
7:{NOME: "Marmitex(Médio)", PRECO: 20.00, QUANTIDADE: 0},
8:{NOME: "Marmitex(Mini)", PRECO: 18.99, QUANTIDADE: 0}
}

for i in range(8):
  print(items[i][NOME]+" -> "+str(items[i][PRECO]))

escolhas=tuple(map(int, input("\n1,2,3,4,5,6,7,8,9\n9 itens(0,0,0,...+1=Quantidade): ").split(",")))

if len(escolhas)!=9:
  raise Exception("É necessário colocar uma lista de 9 números separados por vírgula!\n0,1,2,3,4,5,6,7,8")

total=0.0
for item, escolha in enumerate(escolhas):
  produto=items[item]
  if escolha>0:
    produto[QUANTIDADE]=escolha
    total+=produto[PRECO]*produto[QUANTIDADE]
    dados[ITEMS].append(produto)


identifica=input("Identificar cliente como:").strip()
if identifica!="":
  dados[CLIENTE]=identifica

dados[OPERADOR]=dados[OPERADOR].format("Anônimo")

dataSaida=dt.now()
tempo=dataSaida - dados[DATA]

itensFormatados=""
for produto in dados[ITEMS]:
  itensFormatados+=f"{produto[QUANTIDADE]}x      "+produto[NOME]+"      "+str(produto[PRECO])+"\n"

taxa=total/10 #10%
total_pag=total+taxa
#Exibir Nota
print(f'''
        {dados[RESTAURANTE]}
        {dados[ENDERECO]}
        (00) 0000-0000
-------------------------------------->
{dados[MESA]}
Data Entrada: {dados[DATA]}
Data Saída: {dataSaida} ({tempo})

Cliente: {dados[CLIENTE]}
Operador: {dados[OPERADOR]}

QTO     ITEMS DO PEDIDO      R$
{itensFormatados}
Total dos itens:     {total}
Taxa de Serviço:       +{taxa}
Total a Pagar:       {total_pag}

Quantidade de itens: {len(dados[ITEMS])}
''')