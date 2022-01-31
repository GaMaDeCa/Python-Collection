# coding: latin-1

import os,platform

# Criado por Gabriel Matheus de Castro em 30/01/2022
# Uso:
#   Apenas inicie o script e insira a pasta que vc quer criar a galeria(com as imagens),
#   ou digite 0 para usar a pasta atual(que o script tá rodando),
#   por fim escolha se vai ou não usar imagens de subdiretórios.
# TODO:
#   Slideshow
#   Subdiretórios
#   Animações/Configurações
#   Suporte Criptografias/Codificações['webm','mp4','3gp','base64','md5','sha | aes']

extensoes_permitidas=['gif','jpg','jpeg','png','bmp']

nome_do_arquivo='Galeria.html'
barra=''

if platform.platform().upper().find('WINDOWS')!=-1:
    barra='\\'
else:
    barra='/'

c=input('Insira o caminho da galeria ou digite 0 para usar a pasta atual: ')

def gerar_codigo_html(lista_string,titulo='Galeria Web'):
    return '<html>\n <title>'+titulo+'</title>\n <center>\n  <div id="div_wrapper">\n   <div id="div_header">\n    <h1>'+titulo+'</h1>\n   </div>\n   <div id="div_">\n    <div id="div_esquerda"></div>\n    <div id="div_direita"></div>\n   </div>\n  </div>\n  <script>\n   var itens = '+lista_string+';\n   var contador = 0;\n   function colocarImagens(itens,contador) {\n    var div = document.getElementById("div_direita");\n    div.innerHTML = "";\n    for (i = 0; i < itens.length; i++) {\n     var item=document.createElement("img");\n     item.src=itens[i];\n     item.width="300";\n     item.height="300";\n     item.alt=itens[i];\n     item.id="item"+contador;\n     item.position="relative";\n     item.style.zIndex=contador;\n     div.appendChild(item);\n     contador+=1;\n    }\n   }\n   window.onload = function() {\n    colocarImagens(itens,contador);\n   };\n  </script>\n </center>\n</html>'

def obter_lista_de_imagens(caminho,v_sub):
    lista_de_imagens_obtidas=[]
    init=0
    for pasta,subpastas,arquivos in os.walk(caminho):
        if init==0:
            pastaInit=pasta
            init=-1
        for arquivo in arquivos:
            for extensao in extensoes_permitidas:
                if arquivo.endswith('.'+extensao):
                    if v_sub:
                        if pastaInit+barra+arquivo==pasta+barra+arquivo:
                            lista_de_imagens_obtidas.append(arquivo)
                        else:
                            lista_de_imagens_obtidas.append(pasta.replace(pastaInit,'')[1:]+barra+arquivo)
                    else:
                        if pastaInit+barra+arquivo==pasta+barra+arquivo:
                            lista_de_imagens_obtidas.append(arquivo)
    if len(lista_de_imagens_obtidas)==0:
        print('Arquivos não econtrados!')
        quit()
    return lista_de_imagens_obtidas

def gerar_web_galeria_HTML(caminho,v_sub):
    codigo=gerar_codigo_html(str(obter_lista_de_imagens(caminho,v_sub)))
    if not caminho.endswith(barra):
        caminho=caminho+barra
    with open(caminho+nome_do_arquivo,'w') as arquivo:
        arquivo.write(codigo)
        print(f'{nome_do_arquivo} salvo em:\n    '+caminho)

def gerador(caminho):
    sub=input('\nVerificar subpastas? (S/N) ')
    if sub.upper()=='N':
        gerar_web_galeria_HTML(caminho,False)
    else:
        gerar_web_galeria_HTML(caminho,True)

if c=='0':
    gerador(os.getcwd())
else:
    if os.path.isdir(c):
        gerador(c)
    else:
        print(f'Erro, não é um diretório!')
