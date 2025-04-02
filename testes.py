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
