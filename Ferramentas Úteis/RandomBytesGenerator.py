#coding:latin-1
from random import choice

hex_chars='ABCDEF0123456789'
hex_array=[a+b for a in hex_chars for b in hex_chars]#Cria um tipo de wordlist com os 255 bytes possíveis em formato hexadecimal(['AA','AB'...'98','99']).

print("\n [TABELA DE UNIDADES DE INFORMAÇÃO]\n   1 Kilobyte = 1024 Bytes(4 Digitos)\n   1 MegaByte = 1048576 Bytes(7 Digitos)\n   1 GigaByte = 1073741824 Bytes(10 Digitos)\n   1 TeraByte = 1099511627776 Bytes(13 Digitos)\n")

tamanho=int(input('Digite o tamanho em bytes(Exemplo: 1024): '))
#bytes_gerados=b''

def gerar_codigo_hex(tamanho,hex_code=''):
    for i in range(0,tamanho):
        hex_code+=choice(hex_array)
    return hex_code

#def byte_generator(t):
#    byte=b''
#    for i in range(0,t):
#        byte+=bytes.fromhex(f'{choice(hex_array)}{choice(hex_array)}')

# TODO: Pelo visto a saída do print() consome muita memória deixando o script lerdo,
#   então vai ser necessário recriar o método pra printar em uma thread separada.

#print('Byte Número 0',end='')
#i_len=1
#back='\b'
#for i in range(0,tamanho):
    #print(f'{back*i_len}{i}',end='')
    #i_len=len(str(i))
bytes_gerados=bytes.fromhex(gerar_codigo_hex(tamanho))

#i+=1
#i_len=len(str(i))
#print(f'{back*i_len}{i}',end='')

salvar_como=input('\nDigite um nome para salvar na pasta atual ou digite print para exibir na tela(Não aconselhado, pode travar): ')
if salvar_como.lower()=='print':
    print(bytes_gerados)
else:
    with open(salvar_como,'wb') as arquivo:
        arquivo.write(bytes_gerados)
