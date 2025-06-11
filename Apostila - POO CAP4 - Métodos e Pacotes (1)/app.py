# Altere esta linha para escolher entre SQL ou NoSQL
from banco_dados_sql import Conexao
# from banco_dados_nosql import Conexao

def main():
    conexao = Conexao()
    print(conexao.conectar())

if __name__ == "__main__":
    main()
