class Pessoa:
    def __init__(self, nome="", idade=0):
        self.nome = nome
        self.idade = idade if idade >= 0 else 0

    def set_nome(self, nome):
        self.nome = nome

    def set_idade(self, idade):
        if idade >= 0:
            self.idade = idade
        else:
            print("Idade não pode ser um valor negativo.")

def main():
    nome = "Ítalo"
    idade = 19

    pessoa = Pessoa(nome, idade)
    
    print("Informações da Pessoa:")
    print(f"Nome: {pessoa.nome}Idade: {pessoa.idade}")

    pessoa.set_idade(-5)

if __name__ == "__main__":
    main()
