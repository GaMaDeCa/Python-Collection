import os, sys
# Um teste com Zero Fill
# Uso:
#  ZeroFill.py arquivo.txt
try:
    arquivoParaDeletar = sys.argv[1]
except Exception:
    print("A sintaxe do comando esta incorreta!\n")
    quit()

if os.path.exists(arquivoParaDeletar) and os.path.isfile(arquivoParaDeletar):
    tamanhoDoArquivo=os.path.getsize(arquivoParaDeletar)
    if tamanhoDoArquivo <= 1:
        continuar=input("Arquivo com " + str(tamanhoDoArquivo) + " bytes, deseja continuar? (S/N) : ")
        if continuar=="N" or continuar=="n":
            quit()
    arquivo=open(arquivoParaDeletar,'r+')
    arquivo.read()
    arquivo.seek(0)
    for tamanho in range(0, tamanhoDoArquivo+1):
        arquivo.write("0")
    arquivo.truncate()
    arquivo.close()
    os.remove(arquivoParaDeletar)
else:
    print("Arquivo nao encontrado ou e um diretorio!")
