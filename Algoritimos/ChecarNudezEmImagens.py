# Instale a lib nude ou nudepy com pip3 install ou pip install
# Arquivos ocultos nao sao reconhecidos
import glob,itertools,sys,nude

# coding: latin-1
# pylint: disable=C0103

caminho=''
try:
    caminho=sys.argv[1]
except:
    print(' ! [Enter vazio se quiser verificar as imagens da pasta atual]')
    caminho=input('Digite o caminho da pasta inicial ou o caminho de uma imagem: ') # Exemplo : /home/pasta_das_imagens

# Verifica o caminho
if caminho.strip()=='':
    caminho=''
else:
    if caminho[::-1][0]!='\\' or caminho[::-1][0]!='/':
        if caminho.find('/')==-1:
            caminho+='\\'
        else:
            caminho+='/'

# Arquivos ocultos que começam com .arquivo.jpg não são reconhecidos, os.walk() pode corrigir isso.
imagens_jpg = glob.glob(caminho+"*.jpg") # - Pode ser os.walk() if extensao=='.jpg', etc.
imagens_png = glob.glob(f'{caminho}*.png')
imagens_gif = glob.glob('%s*.gif'%(caminho))
imagens_tiff = glob.glob('{}*.tiff'.format(caminho))

lista_de_imagens = itertools.chain(imagens_jpg, imagens_png, imagens_gif, imagens_tiff)
# Ou lista_de_imagens=imagens_jpg+imagens_png+imagens_gif+imagens_tiff

def verificar_nudez(imagem):
    ehNude = nude.Nude(imagem)
    ehNude.parse()
    return f'Nudez encontrada? {"Sim" if ehNude.result==True else "Não"}, Motivo: {ehNude.message}\n{ehNude.inspect()}\n'

# Loop pra checar se a imagem contém nudez ou não
#   for index in range(len(lista_de_imagens)):
#           ehNude=nude.Nude(lista_de_imagens[index])
for imagem in lista_de_imagens:
    print("[+] Analisando arquivo : " + imagem)
    print(verificar_nudez(imagem))
