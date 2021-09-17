import base64, sys

def ajuda():
    print(f"Codifica e decodifica um arquivo em Base 64.\n\nUso:\n {__file__} [-c | -d] [ Origem ] [ Destino ]\n\nExemplos:\n\n {__file__} -c Texto.txt TextoCodificado.txt\n\nCodifica o conteudo do arquivo Texto.txt em base 64 e salva o conteudo no arquivo TextoCodificado.txt.\n\n      -c          Codifica o arquivo origem em base 64 e salva no destino.\n      -d          Decodifica o arquivo origem e salva no destino.\n      Origem          Nome ou caminho do arquivo a ser manipulado.\n      Destino          Nome ou caminho do arquivo resultado da operacao.")

try:
    opcao = sys.argv[1]
    incds = sys.argv[2]
except Exception:
    print("A sintaxe do comando esta incorreta!\n")
    ajuda()
    quit()

arquivoinput = incds.replace('\\', '/')

try:
    outcds = sys.argv[3]
except Exception:
    if opcao == '-c' or opcao == '-C':
        outcds = incds + ".Base64"
    elif opcao == '-d' or opcao == '-D':
        outcds = incds[:-7]

arquivooutput = outcds.replace('\\', '/')

if opcao == '-c' or opcao == '-C':
	lendo_arquivo=open(arquivoinput, 'rb')
	conteudo=lendo_arquivo.read()
	arquivo_codificado = base64.b64encode(conteudo)
	dados = open(arquivooutput,"ab")
	dados.write(arquivo_codificado)
	dados.close()
elif opcao == '-d' or opcao == '-D':
        # Decodificando
	lendo_arquivo=open(arquivoinput, 'rb')
	conteudo=lendo_arquivo.read()
	arquivo_codificado = base64.b64decode(conteudo)
	dados = open(arquivooutput,"ab")
	dados.write(arquivo_codificado)
	dados.close()
