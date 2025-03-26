class Livro:
    def __init__(self, titulo, autor, ano_publicacao, genero):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.genero = genero

    def exibir_info(self):
        print(self.titulo)
        print(self.autor)
        print(self.ano_publicacao)
        print(self.genero)

livro = Livro("Ítalo e seu Sax", "Ítalo", 2025, "Romance")
livro.exibir_info()

class Tarefa:
    def __init__(self, descricao, prazo, status):
        self.descricao = descricao
        self.prazo = prazo
        self.status = status 

class ContaBancaria:
    def __init__(self, titular, numero_conta, saldo):
        self.titular = titular
        self.numero_conta = numero_conta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

