class Termostato:
    def __init__(self, temperatura_atual, temperatura_desejada, ligado):
        self.temperatura_atual = temperatura_atual
        self.temperatura_desejada = temperatura_desejada
        self.ligado = ligado
        
    def exibir_info(self):
        print(self.temperatura_atual)
        print(self.temperatura_desejada)
        print(self.ligado)

termostato = Termostato(30, 24, 10)
termostato.exibir_info()