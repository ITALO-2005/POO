class Livro:
    def __init__(self, titulo, autor, isbn, copias_totais):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.copias_totais = copias_totais
        self.emprestimos = []  # Usando lista pública para simplificar

    def get_emprestimos(self):
        return self.emprestimos

    def emprestar(self):
        if self.get_disponibilidade() > 0:
            self.emprestimos.append("Livro emprestado")
            return "Empréstimo realizado com sucesso!"
        else:
            return "Não há livro disponível para empréstimo."

    def devolver(self, emprestimo):
        if emprestimo in self.emprestimos:
            self.emprestimos.remove(emprestimo)

    def get_disponibilidade(self):
        return self.copias_totais - len(self.emprestimos)

    def get_titulo(self):
        return self.titulo
