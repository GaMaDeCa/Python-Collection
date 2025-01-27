#coding:latin-1

import hashlib,os,shutil
#XOR Seguro com comparação de hashes SHA-512(beta)
# Secure XOR using SHA-512 to compare both files(beta)
#Autor: GaMaDeCa

def hashFile(fe:open,bufSize=1024*1024):
    sha=hashlib.sha512()
    content=fe.read(bufSize)
    while content!=b'':
        sha.update(content)
        content=fe.read(bufSize)
    return sha.hexdigest()

def xorFile(inStr:open,outStr:open,password:bytes,bufSize:int):
    reading=inStr.read(bufSize)
    x=0
    xp=len(password)
    while reading!=b'':
        data=[]
        for ri in range(len(reading)):
            data.append(reading[ri]^password[x])
            x+=1
            if x==xp:x=0
        outStr.write(bytes(data))
        reading=inStr.read(bufSize)

def secureXOR(filename:str,password:bytes,bufSize=1024*1024,temp='.securexor.tmp',hashCompare=True):
    inStr=open(filename,'rb')
    outStr=open(temp,'wb')
    xorFile(inStr,outStr,password,bufSize)
    outStr.close()
    if hashCompare:
        inStr.seek(0)
        original=hashFile(inStr)
        inStr.close()
        inStr=open(temp,'rb')
        outStr=open(temp+'2','wb')
        xorFile(inStr,outStr,password,bufSize)
        outStr.close()
        inStr.close()
        inStr=open(temp+'2','rb')
        xored=hashFile(inStr)
        inStr.close()
        if original==xored:
            os.remove(filename)
            shutil.move(temp,filename)
            os.remove(temp+'2')
        else:
            print('Something went wrong!\n SHA-512 Hashes are not the same!\n\nInfo:\n-{filename}\n{original}\n\n-{temp}\n{xored}')
            exit(1)
    else:
        inStr.close()
        os.remove(filename)
        shutil.move(temp,filename)


enc='latin-1'
filename=input('Nome do arquivo(-r para entrar em modo recursivo): ')
password=input('Senha: ').encode(enc)
print(password)
usaHash=input('Comparar hashes SHA-512?(y/n)').lower()!='n'

secureXOR(filename,password,hashCompare=usaHash)
