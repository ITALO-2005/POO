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

class DNA:
    def __init__(self, Genes, Cromossomos, Genoma):
        self.Genes = Genes
        self.Cromossomos = Cromossomos
        self.Genoma = Genoma
    
    def exibir_info(self):
        print(self.Genes)
        print(self.Cromossomos)
        print(self.Genoma)
    
dna = DNA("RNA", "autossomicos", "codificada_DNA")
dna.exibir_info()
        
class Pixel:
    def __init__(self, posicao_x, posicao_y, cor):
        self.posicao_x = posicao_x  
        self.posicao_y = posicao_y 
        self.cor = cor 
    
    def exbir_info(self):
        print(self.posicao_x)
        print(self.posicao_y)
        print(self.cor)

pixel = Pixel(60, 50, "Black")
pixel.exbir_info()