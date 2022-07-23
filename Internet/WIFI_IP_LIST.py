# coding: latin-1
from subprocess import check_output
import threading

# Usa 10 threads com ping pra verificar endereços IP conectados na rede(Baseado no IP do roteador)
# Testado no Windows 7(PT-BR)

def ping_ip(i):
    try:
        end_ip=check_output(f'ping -n 1 {gate}{i} -l 1')
        if str(end_ip).find('Disparando') != -1 or str(end_ip).find('Resposta') != -1 :
            #print(f'Disparando {gate}{i}')
            if str(end_ip).find('inacess') == -1:
                print(f'IP Encontrado : {gate}{i}')
    except Exception:
        print('Erro')

def um():
    for i in range(0, 25):
        ping_ip(i)
def dois():
    for i in range(25, 50):
        ping_ip(i)
def tres():
    for i in range(50, 75):
        ping_ip(i)
def quatro():
    for i in range(75, 100):
        ping_ip(i)
def cinco():
    for i in range(100, 125):
        ping_ip(i)
def seis():
    for i in range(125, 150):
        ping_ip(i)
def sete():
    for i in range(150, 175):
        ping_ip(i)
def oito():
    for i in range(175, 200):
        ping_ip(i)
def nove():
    for i in range(200, 225):
        ping_ip(i)
def dez():
    for i in range(225, 256):
        ping_ip(i)
try:
    rou=check_output("ipconfig")
    rot=str(rou)
    rgpp=rot.find('Gateway Padr')
    rote=rot[(rgpp+49):]
    rp=rote.find('r')
    ip_do_roteador=rote[:(rp-1)]
except Exception:
    print('Erro! Digite o ip do rotador manualmente :')
    ip_do_roteador=input('')

# Inverte o IP do roteador depois corta os últimos números antes do ".", e inverte novamente.
gate=ip_do_roteador[::-1][ip_do_roteador[::-1].find('.'):][::-1]

print('Aguarde, vai demorar...')
threading.Thread(target=um).start()
threading.Thread(target=dois).start()
threading.Thread(target=tres).start()
threading.Thread(target=quatro).start()
threading.Thread(target=cinco).start()
threading.Thread(target=seis).start()
threading.Thread(target=sete).start()
threading.Thread(target=oito).start()
threading.Thread(target=nove).start()
threading.Thread(target=dez).start()

# Comando ARP -A ja lista todas as maquinas na rede(E é muito mais rápido), isso foi somente um teste com threads.
