ï»¿from urllib.request import Request, urlopen
import sys, os

if sys.platform[:3] == 'win':
    os.system('mode con cols=100 lines=40')

url = 'peixe nada'

try:
    url = sys.argv[1]
except Exception:
    print('\n\n ------- uWu ------- \n\n')
    quit()

print(f'\nAnalisando url...\n\n{url}')

if url[-1:]!='/':
    url=url+'/'

animes_online_cc=url.find('animesonline.cc/episodio/')
if animes_online_cc <= -1:
    print('\n\nErro!\n')
    print(f'{url}\n\nEsse script sÃ³ funciona com o site animesonline.cc!\nSe nÃ£o for com este site vai dar erro!')
    continuar=input('Deseja continuar mesmo assim? (S/N) ')
    if continuar.upper() == 'N':
        quit()

nome=url.find('/episodio/')
nome_do=(url[(nome+10):-1])
nome_do_video=nome_do+'.mp4'
nome_do_video=((nome_do_video[:1].upper()) + (nome_do_video[1:])).replace('-', ' ')

navegador = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

print('\nConfigurado Agente Mozilla 5.0!')

def requisitar(url, navegador, decodificar):
    requisitar = Request(url, None, navegador)
    conteudo = urlopen(requisitar).read()
    if decodificar == True:
        conteudo=conteudo.decode('utf_8')
    return conteudo

def primeiraParte(pagina):
    posix=(pagina.find('" class="play-box-iframe fixidtab"> <iframe class="metaframe rptss" src="https://www.blogger.com/video.g?token='))
    gerando_s=(pagina[posix:(posix+650)])
    posixs=(gerando_s.find('src=')+5)
    gerando_st=(gerando_s[posixs:posix+650])
    posixsx=(gerando_st.find('" frameborder="'))
    gerando_str=(gerando_st[:posixsx])
    return gerando_str

def segundaParte(nova_url):
    pagina = requisitar(nova_url, navegador, True)
    posix=(pagina.find('"play_url":"https'))
    gerando_s=(pagina[(posix+12):(posix+900)])
    posixs=(gerando_s.find('","format_id":'))
    gerando_st=(gerando_s[:posixs])
    print(gerando_st+'\n')
    gerando_str=(gerando_st.replace("\\/", "/").encode().decode('unicode_escape'))
    return gerando_str

print('\nAbrindo pÃ¡gina...')
pagina = requisitar(url, navegador, True)

print('\nFazendo os pÄ…rÄ…nÄ…uÃª...\n')
gerado = primeiraParte(pagina)

print(f'\n{gerado}\n\nEncontrado o link codificado em unescape JSON!\n')

link_do_video = segundaParte(gerado)

print(f'\nLink do video decodificado!\n\n{link_do_video}')

print('\nAguarde! o vÃ­deo esta sendo baixado...')

video = requisitar(link_do_video, navegador, False)

print(f'\nSalvando vÃ­deo como "{nome_do_video}"...')

arquivo = open(nome_do_video,"ab")
arquivo.write(video)
arquivo.close()

print(f'\n â–¬â–¬â–¬â–¬â–¬â–¬â–¬[FIM!]â–¬â–¬â–¬â–¬â–¬â–¬â–¬\n\nCaminho da pasta :\n\n {os.getcwd()}')
