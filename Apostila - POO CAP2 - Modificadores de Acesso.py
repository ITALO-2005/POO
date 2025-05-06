#2.1 Encapsulamento (public, private)
#14 Ajuste na classe Personagem:
class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.__vida = vida

    def mostrar_vida(self):
        return self.__vida 

#15 Ajuste na classe Pontuacao:
class Pontuacao:
    def __init__(self):
        self.__pontos = 0

    def adicionar_pontos(self, valor):
        if valor > 0:
            self.__pontos += valor

#16 Ajuste na classe Inimigo:
class Inimigo:
    def __init__(self, nome, vida, forca):
        self.nome = nome
        self.__vida = vida
        self.__forca = forca

    def atacar(self):
        print(f"O inimigo ataca com força {self.__forca}")
        
#17 Ajuste na classe Jogador:
class Jogador:
    def __init__(self, nome, energia):
        self.nome = nome
        self.__energia = energia

    def usar_energia(self, valor):
        if 0 <= self.__energia - valor <= 100:
            self.__energia -= valor

    def recuperar_energia(self, valor):
        if 0 <= self.__energia + valor <= 100:
            self.__energia += valor

#2.2 Getters e Setters
#18 Ajuste na classe Personagem
class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.__vida = vida

    @property
    def vida(self):
        return self.__vida

#19 Ajuste na classe Pontuaçãoclass Pontuacao:
    def __init__(self):
        self.__pontos = 0

    @property
    def pontos(self):
        return self.__pontos

    @pontos.setter
    def pontos(self, valor):
        if valor >= 0:
            self.__pontos = valor

#20 Ajuste na classe Jogo
class Jogo:
    def __init__(self):
        self.__dificuldade = 1

    @property
    def dificuldade(self):
        return self.__dificuldade

    @dificuldade.setter
    def dificuldade(self, valor):
        if 1 <= valor <= 3:
            self.__dificuldade = valor

#21 Ajuste na classe Personagem (atributo defesa)
class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.__vida = vida
        self.__defesa = 0

    @property
    def defesa(self):
        return self.__defesa

    @defesa.setter
    def defesa(self, valor):
        if 0 <= valor <= 100:
            self.__defesa = valor
            
#2.3 Construtores
#22 Ajuste na classe Personagem
class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.__vida = vida

#23 Ajuste na classe Inimigo
class Inimigo:
    def __init__(self, nome, vida, forca):
        self.nome = nome
        self.__vida = vida
        self.__forca = forca

#24 Ajuste na classe Jogador
class Jogador:
    def __init__(self, nome, energia, pontos):
        self.nome = nome
        self.__energia = energia
        self.pontos = pontos

#25 Ajuste na classe Menu
class Menu:
    def __init__(self, titulo):
        self.titulo = titulo

    def iniciar(self):
        print(f"Iniciando o menu: {self.titulo}")
