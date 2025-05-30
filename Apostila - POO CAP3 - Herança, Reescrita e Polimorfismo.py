#2.4 Herança
# Classe base
class Personagem:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print(f"{self.nome} diz: Olá!")

    def atacar(self):
        print(f"{self.nome} ataca!")

class Inimigo(Personagem):
    def __init__(self, nome, vida, forca):
        super().__init__(nome)
        self.vida = vida
        self.forca = forca

class Jogador(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self.pontuacao = 0

    def adicionar_pontos(self, pontos):
        self.pontuacao += pontos

class Jogo:
    def iniciar(self):
        print("Iniciando jogo...")

class Menu:
    def exibir(self):
        print("Exibindo menu...")

# 26
class NPC(Personagem):
    def atacar(self):
        print(f"{self.nome} não pode atacar.")

# 27
class Chefe(Inimigo):
    def __init__(self, nome, vida, forca):
        super().__init__(nome, vida * 2, forca * 2)

# 28
class JogadorPremium(Jogador):
    def adicionar_pontos(self, pontos):
        super().adicionar_pontos(pontos * 2)

# 29
class JogoMultiplayer(Jogo):
    def __init__(self):
        self.jogadores = []

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)

# 30
class MenuAvancado(Menu):
    def salvar_configuracoes(self, configuracoes):
        self.configuracoes = configuracoes
        print("Configurações salvas:", configuracoes)

# 31
class Arma:
    def atacar(self):
        pass

class Espada(Arma):
    def atacar(self):
        return "Corte com espada!"

class Arco(Arma):
    def atacar(self):
        return "Flecha disparada!"

# 32
class Missao:
    def recompensa(self):
        pass

class MissaoPrincipal(Missao):
    def recompensa(self):
        return "Recompensa épica!"

class MissaoSecundaria(Missao):
    def recompensa(self):
        return "Recompensa simples."

# 33
class Item:
    def efeito(self):
        pass

class Pocao(Item):
    def efeito(self):
        return "Recupera vida."

class Equipamento(Item):
    def efeito(self):
        return "Aumenta defesa."

# 34
class Fase:
    def __init__(self, nome):
        self.nome = nome

    def caracteristicas(self):
        pass

class FaseFloresta(Fase):
    def caracteristicas(self):
        return "Verde, cheia de árvores."

class FaseDeserto(Fase):
    def caracteristicas(self):
        return "Quente, cheia de areia."

# 35
class Aliado(Personagem):
    def habilidade(self):
        pass

class Mago(Aliado):
    def habilidade(self):
        return "Lança bola de fogo."

class Guerreiro(Aliado):
    def habilidade(self):
        return "Golpe devastador."

#Reescrita e Polimorfismo
# 36
class NPC(Personagem):
    def falar(self):
        print(f"{self.nome} murmura algo enigmático...")

    def atacar(self):
        print(f"{self.nome} não pode atacar.")

# 37
class Chefe(Inimigo):
    def atacar(self):
        print(f"{self.nome} realiza um golpe especial com dano extra!")

# 38
class JogadorPremium(Jogador):
    def adicionar_pontos(self, pontos):
        self.pontuacao += pontos * 3

# 39
class JogoMultiplayer(Jogo):
    def iniciar(self):
        print("Jogo multiplayer iniciado. Conectando jogadores...")

# 40
class MenuAvancado(Menu):
    def exibir(self):
        print("Exibindo menu com opções avançadas.")

# 41
class FaseDeserto(Fase):
    def gerar_inimigos(self):
        return ["Escorpião Gigante", "Múmia", "Golem de Areia"]

#2.6 Herança Múltipla
# 42
class Voador:
    def voar(self):
        return "Voando pelos céus..."

class Dragao(Inimigo, Voador):
    pass

# 43
class Curador:
    def curar(self):
        return "Cura mágica realizada."

class Paladino(Guerreiro, Curador):
    pass

# 44
class MagiaElemental:
    def lançar_magia(self, elemento):
        return f"Lançando magia de {elemento}!"

class MagoElemental(Mago, MagiaElemental):
    pass

# 45
class AnimalMontaria:
    def montar(self):
        return "Montado e pronto para a batalha."

class Cavaleiro(Guerreiro, AnimalMontaria):
    pass

#2.7 Associação, Composição e Agregação
# 46 - Associação
class JogadorArma:
    def __init__(self, nome):
        self.nome = nome
        self.arma = None

    def equipar_arma(self, arma):
        self.arma = arma

# 47 - Associação
class PersonagemMissao:
    def __init__(self, nome):
        self.nome = nome
        self.missoes = []

    def aceitar_missao(self, missao):
        self.missoes.append(missao)

# 48 - Composição
class JogoComMenu:
    def __init__(self):
        self.menu = Menu()

# 49 - Composição
class FaseComInimigos:
    def __init__(self):
        self.inimigos = [Inimigo("Inimigo", 100, 10) for _ in range(3)]

# 50 - Composição
class Inventario:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)

# 51 - Agregação
class Guilda:
    def __init__(self):
        self.jogadores = []

    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)

# 52 - Agregação
class Mapa:
    def __init__(self):
        self.fases = []

    def adicionar_fase(self, fase):
        self.fases.append(fase)

# 53 - Agregação
class Loja:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)

# 54 - Associação
class AliadoJogador:
    def __init__(self, nome):
        self.nome = nome
        self.jogador_acompanhado = None

    def acompanhar(self, jogador):
        self.jogador_acompanhado = jogador

# 55 - Composição
class SistemaCombate:
    def __init__(self, personagem, inimigo):
        self.personagem = personagem
        self.inimigo = inimigo

    def encerrar(self):
        print("Combate encerrado!")
        del self.personagem
        del self.inimigo

