from util_arquivos.escrita import escrever_arquivo
from util_arquivos.leitura import ler_arquivo

escrever_arquivo("mensagem.txt", "Olá, mundo!")
conteudo = ler_arquivo("mensagem.txt")
print(conteudo)