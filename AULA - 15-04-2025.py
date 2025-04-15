class Temperatura:
    def __init__(self, celsius):
        self.__celsius = celsius

    @property
    def celsius(self):
        return self.__celsius

    @property
    def fahrenheit(self):
        return (self.__celsius * 9/5) + 32

    @celsius.setter
    def celsius(self, valor):
        if valor < -273.15:
            print("Temperatura inexistente.")
            self.__celsius = 0
        else:
            self.__celsius = valor
            
            
temp = Temperatura(25)
print(f"Temperatura em °C: {temp.celsius}°C")
print(f"Temperatura em °F: {temp.fahrenheit}°F")

temp.celsius = 100
print(f"Temperatura em °C: {temp.celsius}")
print(f"Temperatura em °F: {temp.fahrenheit}")

try:
    temp.celsius = -300
except ValueError as e:
    print(e)
    
    
    
#EXERCICIO 1
class Pessoa:
    def __init__(self):
        self.__nome = ""
        self.__idade = 0

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_idade(self):
        return self.__idade

    def set_idade(self, idade):
        if idade >= 0:
            self.__idade = idade
        else:
            print("Idade não pode ser um valor Negativo")
            
def main():
    pessoa = Pessoa()
    
    pessoa.set_nome()
    pessoa.set_idade()
    
    print(pessoa.get_nome())
    print(pessoa.get_idade())
    pessoa.set_idade(-5)
    
if __name__ == "__main__":
    main()

