import pygame
pygame.init()
# Teste com Joystick(Caso o valor do botao seja diferente, configure)
controle=pygame.joystick.Joystick(0)
controle.init()
try:
    while 1:
        eventos=pygame.event.get()
        for evento in eventos:
            botao_pressionado=''
            if evento.type==pygame.JOYBUTTONDOWN:
                if controle.get_button(0):botao_pressionado+='Triangulo'
                elif controle.get_button(1):botao_pressionado+='Bolinha'
                elif controle.get_button(2):botao_pressionado+='Cruz'
                elif controle.get_button(3):botao_pressionado+='Quadrado'
                elif controle.get_button(4):botao_pressionado+='L1'
                elif controle.get_button(5):botao_pressionado+='R1'
                elif controle.get_button(6):botao_pressionado+='L2'
                elif controle.get_button(7):botao_pressionado+='R2'
                elif controle.get_button(8):botao_pressionado+='Select'
                elif controle.get_button(9):botao_pressionado+='Start'
                elif controle.get_button(10):botao_pressionado+='L3'
                elif controle.get_button(11):botao_pressionado+='R3'
                print(f'Pressionou {botao_pressionado}')#Ou vc pode criar uma classe "Jogo" em outra thread que interage com esse loop em um metodo.
            elif evento.type==pygame.JOYAXISMOTION:
                #print(evento.dict,evento.joy,evento.axis,evento.value)
                axis_x,axis_y=(controle.get_axis(0),controle.get_axis(1))
                if axis_x==-1.0:print('Esquerda')
                elif abs(axis_x)>0.1:print('Direita')
                if axis_y==-1.0:print('Cima')
                elif abs(axis_y)>0.1:print('Baixo')
            elif evento.type==pygame.JOYBUTTONUP:
                print(f'Soltou {botao_pressionado}')
except KeyboardInterrupt:
    print("Saindo...")
    controle.quit()
