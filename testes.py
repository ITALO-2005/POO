import random

class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100

    def atacar(self, alvo):
        dano = random.randint(5, 20)
        alvo.vida -= dano
        print(f"{self.nome} ataca {alvo.nome} causando {dano} de dano!")

class Inimigo:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100

    def atacar(self, alvo):
        dano = random.randint(5, 20)
        alvo.vida -= dano
        print(f"{self.nome} ataca {alvo.nome} causando {dano} de dano!")

personagem = Personagem("Herói")
inimigo = Inimigo("Vilão")

while personagem.vida > 0 and inimigo.vida > 0:
    personagem.atacar(inimigo)
    if inimigo.vida <= 0:
        print(f"{inimigo.nome} foi derrotado! {personagem.nome} vence!")
        break
    inimigo.atacar(personagem)
    if personagem.vida <= 0:
        print(f"{personagem.nome} foi derrotado! {inimigo.nome} vence!")
        break




class Funcionario:
    def __init__(self, nome, id_funcionario, salario_base):
        self.nome = nome
        self.id_funcionario = id_funcionario
        self.salario_base = salario_base
        self.bonus = 0
        self.faltas = 0

    def registrar_falta(self):
        self.faltas += 1

    def adicionar_bonus(self, valor):
        self.bonus += valor

    def recalcular_bonus(self):
        # Subtraindo uma penalidade com base no número de faltas
        penalidade = self.faltas * 50  # Exemplo: penalidade de 50 por falta
        self.bonus = max(0, self.bonus - penalidade)  # Evita bônus negativo

    def get_id(self):
        return self.id_funcionario

    def calcular_salario(self):
        return self.salario_base + self.bonus - (self.faltas * 100)  # Penalidade de 100 por falta

    def resumo(self):
        return (f"Nome: {self.nome}\n"
                f"ID: {self.id_funcionario}\n"
                f"Salário Base: R$ {self.salario_base:.2f}\n"
                f"Bônus: R$ {self.bonus:.2f}\n"
                f"Faltas: {self.faltas}\n"
                f"Salário Final: R$ {self.calcular_salario():.2f}")

# Exemplo de uso
func = Funcionario("João Silva", 123, 2000)
func.registrar_falta()
func.adicionar_bonus(500)
func.recalcular_bonus()
print(func.resumo())
