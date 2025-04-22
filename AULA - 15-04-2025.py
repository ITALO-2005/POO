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
    
    
#13 Sistema de Pontuação e Energia no Jogo
class Inimigo:
    def __init__(self, vida):
        self.vida = vida

class Jogador:
    def __init__(self):
        self.energia = 100
        self.pontos = 0

    def atacar(self, inimigo):
        if self.energia > 0:
            if inimigo.vida > 0:
                inimigo.vida -= 10
                self.energia -= 10
                if inimigo.vida <= 0:
                    self.pontos += 10
                    print("Inimigo derrotado! Pontos:", self.pontos)
            else:
                print("O inimigo já está derrotado.")
        else:
            print("Energia insuficiente. Descanse para continuar atacando.")

    def descansar(self):
        if self.energia < 100:
            self.energia += 20
            if self.energia > 100:
                self.energia = 100
            print("Energia recuperada! Energia:", self.energia)
        else:
            print("Energia já está cheia.")

jogador = Jogador()
inimigo1 = Inimigo(30)
inimigo2 = Inimigo(20)

jogador.atacar(inimigo1)
jogador.atacar(inimigo1)
jogador.atacar(inimigo1)

jogador.descansar()

jogador.atacar(inimigo2)


#14 Criando um Sistema de Menu Interativo
import random

class Menu:
    def exibir_menu(self):
        print("Menu Interativo")
        print("1. Iniciar Jogo")
        print("2. Mostrar Opções")
        print("3. Sair")
    
    def mostrar_opcoes(self):
        print("\nOpções:")
        print("- Batalhas são contra 1 a 3 inimigos aleatórios.")
        print("- Vença todos os inimigos para ganhar.")
        print("- Perder significa fim de jogo.\n")

def iniciar_jogo():
    inimigos_totais = random.randint(1, 3)
    print(f"\nVocê enfrentará {inimigos_totais} inimigo(s)! Prepare-se!\n")

    progresso = 0
    for i in range(1, inimigos_totais + 1):
        print(f"Batalha {i}: Enfrentando inimigo {i}...")
        resultado = random.choice(["Vitória", "Derrota"])
        
        if resultado == "Vitória":
            print("Você venceu!\n")
            progresso += 1
        else:
            print("Você perdeu! Fim de jogo.\n")
            return
    
    if progresso == inimigos_totais:
        print("Parabéns! Você venceu todos os inimigos!")
    else:
        print("Fim de jogo. Tente novamente!\n")

def executar_menu():
    menu = Menu()
    while True:
        menu.exibir_menu()
        escolha = input("\nEscolha uma opção (1-3): ")
        
        if escolha == "1":
            iniciar_jogo()
        elif escolha == "2":
            menu.mostrar_opcoes()
        elif escolha == "3":
            print("Saindo do jogo. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

executar_menu()





