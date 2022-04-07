import Tlexer
print("Analisador Léxico - MINIJAVA\n")
nometxt = input("Digite o nome do Arquivo para analisar: ")
data = open(nometxt, "r").read()
Tlexer.vailexer(data)

