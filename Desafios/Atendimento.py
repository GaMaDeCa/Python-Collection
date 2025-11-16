import random
import time

class Garcom:
    def __init__(self, nome):
        self.nome = nome
        self.disponivel = True
    def atender(self, cliente):
        if not self.disponivel:
            return False
        self.disponivel = False
        print(f"\nð½ï¸ {self.nome} foi atender {cliente.nome}.")
        # AÃ§Ãµes do garÃ§om
        print(f"{self.nome}: Boa noite, {cliente.nome}! Deseja ver o cardÃ¡pio digital?")
        time.sleep(0.5)
        print(f"{self.nome}: Oi, jÃ¡ decidiu o pedido?")
        time.sleep(0.5)
        # InteraÃ§Ã£o com o cliente
        pedido = cliente.fazer_pedido()
        self.servir_comida(pedido)
        cliente.receber_atendimento()
        time.sleep(0.5)
        self.disponivel = True
        print(f"{self.nome}: Com licenÃ§a. (se afasta da mesa)\n")
        return True
    def servir_comida(self, prato):
        print(f"{self.nome}: Preparando e servindo {prato}...")

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.satisfacao = 100  # comeÃ§a feliz
        self.vezes_sem_atendimento = 0
    def sentar(self):
        print(f"{self.nome} sentou-se Ã  mesa e estÃ¡ aguardando o garÃ§om.")
    def olhar_garcom(self):
        print(f"{self.nome} olha ao redor chamando o garÃ§om...")
    def fazer_pedido(self):
        opcoes = ["rodÃ­zio", "prato executivo", "sobremesa", "bebida", "entrada"]
        pedido = random.choice(opcoes)
        print(f"{self.nome}: Gostaria de pedir {pedido}, por favor.")
        return pedido
    def receber_atendimento(self):
        self.vezes_sem_atendimento = 0
        print(f"{self.nome} foi atendido e parece satisfeito!")
    def passar_tempo(self):
        """Cliente pode ficar esperando e perder satisfaÃ§Ã£o."""
        self.vezes_sem_atendimento += 1
        if self.vezes_sem_atendimento > 1:
            perda = random.randint(5, 15)
            self.satisfacao = max(0, self.satisfacao - perda)
            print(f"{self.nome} estÃ¡ esperando hÃ¡ um tempo... ð (SatisfaÃ§Ã£o: {self.satisfacao}%)")
    def esta_satisfeito(self):
        return self.satisfacao > 60

# --- SIMULAÃÃO ---

garcons = [Garcom("JoÃ£o"), Garcom("Carlos"), Garcom("Ana")]
clientes = [Cliente("Maria"), Cliente("Pedro"), Cliente("Julia"), Cliente("Rafael")]

print("=== ð  INÃCIO DA SIMULAÃÃO DO RESTAURANTE ===\n")
for c in clientes:
    c.sentar()

# Loop principal da simulaÃ§Ã£o
for rodada in range(1, 8):  # 7 rodadas de tempo
    print(f"\n===== RODADA {rodada} =====")
    time.sleep(1)
    # Cliente aleatÃ³rio olha para chamar um garÃ§om
    cliente = random.choice(clientes)
    cliente.olhar_garcom()
    # Escolhe garÃ§om (preferÃªncia aleatÃ³ria)
    garcom_escolhido = random.choice(garcons)
    if garcom_escolhido.disponivel:
        garcom_escolhido.atender(cliente)
    else:
        # tenta outro garÃ§om disponÃ­vel
        outros_disponiveis = [g for g in garcons if g.disponivel]
        if outros_disponiveis:
            substituto = random.choice(outros_disponiveis)
            print(f"{garcom_escolhido.nome} estÃ¡ ocupado! {substituto.nome} vai atender no lugar.")
            substituto.atender(cliente)
        else:
            print("Todos os garÃ§ons estÃ£o ocupados! O cliente precisa esperar.")
            cliente.passar_tempo()
    # Clientes que nÃ£o foram escolhidos nessa rodada tambÃ©m esperam
    for outro_cliente in clientes:
        if outro_cliente != cliente:
            outro_cliente.passar_tempo()

# --- Fim da simulaÃ§Ã£o ---
print("\n=== ð§¾ RESULTADO FINAL ===")
for c in clientes:
    status = "ð Satisfeito" if c.esta_satisfeito() else "ð  Insatisfeito"
    print(f"{c.nome}: SatisfaÃ§Ã£o {c.satisfacao}% - {status}")

print("\n=== FIM DA SIMULAÃÃO ===")