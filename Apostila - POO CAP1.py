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




        
        
        







