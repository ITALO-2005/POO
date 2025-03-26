class Livro:
    def __init__(self, titulo, autor, ano_publicacao, genero):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.genero = genero

class Tarefa:
    def __init__(self, descricao, prazo, status):
        self.descricao = descricao
        self.prazo = prazo
        self.status = status 

class Conta_Bancaria:
    def __init__(self, nome, cpf, n_agencia, n_conta, senha_transacao):
        self.nome = nome
        self.cpf = cpf
        self.n_agencia = n_agencia
        self.n_conta = n_conta
        self.senha_transacao =  senha_transacao