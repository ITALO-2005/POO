class Livro:
    def __init__(self, titulo, autor, isbn, copias_totais):
        self.titulo = ""
        self.autor = " "
        self.isbn = ""
        self.copias_totais = 0
        self.copias_disponiveis = 0
        self.emprestimos = []
    
    def get_emprestimos(self):
        return self.__emprestimos
    def emprestar(self):
        if self.get_quantidade_disponivel () > 0:
            self.__emprestimos.append(emprestimo)
        else:
            print(f"Não há livro disponivel para emprestimo")

    def remover_emprestimo(self, emprestimo):
        self.__emprestimos.remove(emprestimo)
    def get_quantidade_disponivel(self):
        return self.copias_totais - len(self.__emprestimos)