from prettytable import PrettyTable

def MiddleSquare(x, digitos_de_saida):
    # Elevemos, então, este número ao quadrado 
    x_sqr = x**2
    print("O quadrado do número {} é {}".format(x, x_sqr))
    # O próximo passo, é extrair números ao meio deste número
    # Vamos separar o número ao meio
    # Para isso, precisamos saber a quantidade de dígitos para cortarmos com exatidão

    corte = x_sqr
    digitos = 0
    while corte > 0:
        corte = int(corte/10)
        digitos += 1
    metade = int(digitos/2)
    print("A quantidade de digitos é: ", digitos)
    print("A metade: ",metade)

    # Agora que temos a metade, precisamos decidir como será feito o corte e
    # Para que possamos imprimir os digitos de saida solicitados
    # Temos três casos:
    # Digitos > digitos_de_saida precisamos cortar as casas
    # Digitos = digitos_de_saida podemos imprimir tranquilamente
    # Digitos < digitos_de_saida precisamos adicionar zeros
    print("Comparando os dígitos do número com a saída desejada")
    if digitos > digitos_de_saida:
        # Vamos realizar cortes no número até ele chegar a digitos_de_saida
        # Aqui ele pode ser par ou impar, portanto:
        print("Maior que a saída desejada, realizando cortes")
        if digitos%2 ==0:
            print("Número de digitos: {} é par".format(digitos))
            # Par
            dif_digitos = int((digitos - digitos_de_saida)/2)
            # Este é um número par, portanto cortaremos uma parte de cada
            print("Número de digitos a cortar de cada lado: ", dif_digitos)
            x_sqr = x_sqr % pow(10, digitos - dif_digitos)
            x_sqr = x_sqr // pow(10, dif_digitos)
            return x_sqr
        elif digitos %2 != 0:
            # Cortamos o lado esquerdo, e o transformamos em um número par
            print("Número de digitos: {} impar, realizando corte no lado esquerdo".format(digitos))
            x_sqr = x_sqr % pow(10, digitos-1)
            digitos = digitos - 1
            print("Numero de digitos atualizado: {}, o novo número é: {}".format(digitos, x_sqr))
            # Par
            dif_digitos = int((digitos - digitos_de_saida)/2)
            # Este é um número par, portanto cortaremos uma parte de cada
            print("Número de digitos a cortar de cada lado: ", dif_digitos)
            x_sqr = x_sqr % pow(10, digitos - dif_digitos)
            x_sqr = x_sqr // pow(10, dif_digitos)
            print("Finalizado, saida: ", x_sqr)
            return x_sqr
    elif digitos == digitos_de_saida:
        print("Igual à saída desejada")
        return x_sqr
    elif digitos < digitos_de_saida:
        print("O número é menor, adicionar zeros AO PRINTAR")
        return x_sqr


# Começando, vamos pegar um número 
x = int(input("Qual a semente que você usará?"))
digitos_de_saida = int(input("Quantos dígitos de saída você deseja?"))
intervalos = int(input("Quantos números você deseja imprimir? "))
tabela = PrettyTable(['Iteração', 'Semente', 'Numero'])

for i in range(intervalos):
    row = []
    row.append(i)
    row.append(x)
    ms_x = MiddleSquare(x,digitos_de_saida)
    row.append(ms_x)
    x = ms_x
    tabela.add_row(row)
print(tabela)