#CAP 1.1
#Questão 1
class Jogo:
    def iniciar(self):
        print("O jogo começou!")
meu_jogo = Jogo()
meu_jogo.iniciar()

#Questão 2
class Personagem:
    def pular(self):
        print("O personagem pulou!")
personagem = Personagem()
personagem.iniciar()

#Questão 3
class Inimigo:
    def atacar(self):
        print("O inimigo atacou!")
inimigo = Inimigo()
inimigo.iniciar()

#Questão 4
class Pontuacao:
    def zerar_pontos(self):
        print("Pontuação zerada!")
pontuacao = Pontuacao()
pontuacao.iniciar()

#Questão 5
class Menu:
    def iniciar_jogo(self):
        print("O jogo está começando!")
    def mostrar_opcoes(self):
        print("Opções disponíveis: [1] Jogar, [2] Configurações, [3] Sair")
    def sair(self):
        print("Saindo do jogo. Até mais!")

menu = Menu()
menu.iniciar_jogo()
menu.mostrar_opcoes()
menu.sair()

#CAP. 1.2
#QUESTÃO 6
class Personagem:
    def __init__(self, nome):
        self.nome = nome

    def dizer_nome(self):
        print(self.nome)

meu_personagem = Personagem("João")
meu_personagem.dizer_nome()

#QUESTÃO 7
class Pontuacao:
    def __init__(self):
        self.pontos = 0
    def adicionar_pontos(self, quantidade):
        self.pontos += quantidade
    def mostrar_pontos(self):
        print(self.pontos)

pontuacao = Pontuacao()
pontuacao.adicionar_pontos(10)
pontuacao.mostrar_pontos()

#QUESTÃO 8
class Personagem:
    def __init__(self):
        self.vida = 100

    def tomar_dano(self, dano):
        self.vida -= dano
        if self.vida <= 0:
            self.vida = 0
            print("Game Over!")
personagem = Personagem()
print(personagem.vida)
personagem.tomar_dano(30)
print(personagem.vida)
personagem.tomar_dano(80)
print(personagem.vida)

#QUESTÃO 9
class Jogador:
    def __init__(self):
        self.energia = 50
    def recuperar_energia(self, quantidade):
        self.energia += quantidade
        print(self.energia)
    def usar_energia(self, quantidade):
        if self.energia - quantidade < 0:
            print("Sem energia suficiente!")

jogador = Jogador()
jogador.usar_energia(20)
jogador.usar_energia(40)
jogador.recuperar_energia(30)

#QUESTÃO 10
class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100
class Inimigo:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100
    def atacar(self, alvo):
        if alvo.vida > 0:
            alvo.vida -= 10
            print(f"{self.nome} atacou {alvo.nome}! A vida de {alvo.nome} agora é {alvo.vida}.")
        else:
            print(f"{alvo.nome} já está sem vida!")

personagem = Personagem("Herói")
inimigo = Inimigo("Vilão")
inimigo.atacar(personagem)
inimigo.atacar(personagem)

#11 Simulação de Combate entre Personagem e Inimigo
import random

class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100

    def atacar(self, alvo):
        dano = random.randint(5, 20)
        alvo.vida -= dano
        print(f"{self.nome} ataca {alvo.nome} causando {dano} de dano!")

class Inimigo:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100

    def atacar(self, alvo):
        dano = random.randint(5, 20)
        alvo.vida -= dano
        print(f"{self.nome} ataca {alvo.nome} causando {dano} de dano!")

personagem = Personagem("Herói")
inimigo = Inimigo("Vilão")

while personagem.vida > 0 and inimigo.vida > 0:
    personagem.atacar(inimigo)
    if inimigo.vida <= 0:
        print(f"{inimigo.nome} foi derrotado! {personagem.nome} vence!")
        break
    inimigo.atacar(personagem)
    if personagem.vida <= 0:
        print(f"{personagem.nome} foi derrotado! {inimigo.nome} vence!")
        break



#12 Sistema de Pontuação e Energia no Jogo
    def __init__(self, vida):
        self.vida = vida

class Jogador:
    def __init__(self):
        self.energia = 100
        self.pontos = 0

    def atacar(self, inimigo):
        if self.energia > 0:
            if inimigo.vida > 0:
                inimigo.vida -= 10
                self.energia -= 10
                if inimigo.vida <= 0:
                    self.pontos += 10
                    print("Inimigo derrotado! Pontos:", self.pontos)
            else:
                print("O inimigo já está derrotado.")
        else:
            print("Energia insuficiente. Descanse para continuar atacando.")

    def descansar(self):
        if self.energia < 100:
            self.energia += 20
            if self.energia > 100:
                self.energia = 100
            print("Energia recuperada! Energia:", self.energia)
        else:
            print("Energia já está cheia.")

jogador = Jogador()
inimigo1 = Inimigo(30)
inimigo2 = Inimigo(20)

jogador.atacar(inimigo1)
jogador.atacar(inimigo1)
jogador.atacar(inimigo1)

jogador.descansar()

jogador.atacar(inimigo2)


#13 Criando um Sistema de Menu Interativo
import random

class Menu:
    def exibir_menu(self):
        print("Menu Interativo")
        print("1. Iniciar Jogo")
        print("2. Mostrar Opções")
        print("3. Sair")
    
    def mostrar_opcoes(self):
        print("\nOpções:")
        print("- Batalhas são contra 1 a 3 inimigos aleatórios.")
        print("- Vença todos os inimigos para ganhar.")
        print("- Perder significa fim de jogo.\n")

def iniciar_jogo():
    inimigos_totais = random.randint(1, 3)
    print(f"\nVocê enfrentará {inimigos_totais} inimigo(s)! Prepare-se!\n")

    progresso = 0
    for i in range(1, inimigos_totais + 1):
        print(f"Batalha {i}: Enfrentando inimigo {i}...")
        resultado = random.choice(["Vitória", "Derrota"])
        
        if resultado == "Vitória":
            print("Você venceu!\n")
            progresso += 1
        else:
            print("Você perdeu! Fim de jogo.\n")
            return
    
    if progresso == inimigos_totais:
        print("Parabéns! Você venceu todos os inimigos!")
    else:
        print("Fim de jogo. Tente novamente!\n")

def executar_menu():
    menu = Menu()
    while True:
        menu.exibir_menu()
        escolha = input("\nEscolha uma opção (1-3): ")
        
        if escolha == "1":
            iniciar_jogo()
        elif escolha == "2":
            menu.mostrar_opcoes()
        elif escolha == "3":
            print("Saindo do jogo. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

executar_menu()