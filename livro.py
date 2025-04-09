class Livro:
    def __init__(self, titulo, autor, isbn, copias_totais):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.copias_totais = copias_totais
        self.copias_disponiveis = 0
        self.emprestimos = []
    
    def get_emprestimos(self):
        return self.__emprestimos
    
    def emprestar(self):
        if self.get_quantidade_disponivel () > 0:
            self.__emprestimos.append("Livro emprestado")
        else:
            print(f"Não há livro disponivel para emprestimo")

    def devolver(self, emprestimo):
        self.__emprestimos.remove(emprestimo)
    def get_disponibilidade(self):
        return self.copias_totais - len(self.__emprestimos)

    def get_titulo(self):
        return self.__titulo