from prettytable import PrettyTable

def lcg(x0, a, c, m):
    x = (x0*a + c) % m
    return x


x0 = int(input("Qual o primeiro número da sequencia?"))
a = int(input("Qual o multiplicador?"))
c = int(input("Qual o incremento?"))
m = int(input("Qual o módulo? "))
tabela = PrettyTable(["Iteração", "Número"])
lista_de_n = []
row = []
n = x0
i = 0

while True:
    i += 1
    row = []
    n = lcg(n,a,c,m)
    if n not in lista_de_n:
        lista_de_n.append(n)
        row.append(i)
        row.append(n)
        tabela.add_row(row)
    else:
        break

print(tabela)