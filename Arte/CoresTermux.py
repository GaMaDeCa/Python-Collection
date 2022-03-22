#coding:latin-1
# Só funciona em sistemas linux, testado no Termux.
from random import choice
from time import sleep

caracteres=["0","1"] # [' ','#']

cores=[f'\033[1;{c1}{c2}m' for c1 in range(3,5) for c2 in range(0,8)]

print('Pressione CTRL+C para terminar, começará em 7 segundos...')
sleep(7)

while True:
    print(f'{choice(cores)}{choice(caracteres)}',end='')

# CTRL+C para terminar
