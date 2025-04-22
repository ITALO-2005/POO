# Classe Personagem
class Personagem:
    def __init__(self, vida):
        self.__vida = vida 

    def mostrar_vida(self):
        return self.__vida 


# Classe Pontuacao
class Pontuacao:
    def __init__(self):
        self.__pontos = 0 

    def adicionar_pontos(self, valor):
        if valor > 0:  
            self.__pontos += valor

    def mostrar_pontos(self):
        return self.__pontos 


personagem = Personagem(100)
print("Vida do personagem:", personagem.mostrar_vida())

pontuacao = Pontuacao()
pontuacao.adicionar_pontos(10)
print("Pontuação atual:", pontuacao.mostrar_pontos())


