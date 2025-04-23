#2.1 Encapsulamento (public, private)
#14 Ajuste na classe Personagem:
class Personagem:
    def __init__(self, vida):
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

    def mostrar_pontos(self):
        return self.__pontos

#16 Ajuste na classe Inimigo:
class Inimigo:
    def __init__(self, forca):
        self.__forca = forca 

    def atacar(self):
        print(f"O inimigo ataca com força {self.__forca}") 
