import random

class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100

    def atacar(self, alvo):
        dano = random.randint(5, 20)
        alvo.vida -= dano
        print(f"{self.nome} ataca {alvo.nome} causando {dano} de dano!")
