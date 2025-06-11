from banco_dados_sql import Conexao

def main():
    conexao = Conexao()
    print(conexao.conectar())

if __name__ == "__main__":
    main()
