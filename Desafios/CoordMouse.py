import pyautogui
print('Coordenadas do Mouse:')
try:
    while 1:
        x,y=pyautogui.position()
        positionStr='X: '+str(x).rjust(4)+' Y: '+str(y).rjust(4)
        print(positionStr,end="")
        print('\b'*len(positionStr),end='',flush=True) # '\b' = Apaga caracteres anteriores(Back)
except KeyboardInterrupt: # CTRL+C
    pass
