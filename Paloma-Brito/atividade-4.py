# Atividade 4 → Avançada = 7 pontos
# David possui vários contêineres, cada um com uma quantidade de bolas. Ele possui contêineres
# suficientes para ordenar cada tipo de bola em seu próprio contêiner.
# David deseja realizar operações de troca de forma que:
# • Cada contêiner contenha apenas bolas do mesmo tipo.
# • Nenhuma bola do mesmo tipo esteja em contêineres diferentes.
# Em uma única operação, David pode trocar duas bolas localizadas em contêineres diferentes.

def remover_espacos_extremidades(texto):
    inicio_texto = 0
    fim_texto = len(texto) - 1

    while inicio_texto <= fim_texto and texto[inicio_texto] == " ":
        inicio_texto += 1

    while fim_texto >= inicio_texto and texto[fim_texto] == " ":
        fim_texto -= 1

    texto_sem_espacos = ""

    while inicio_texto <= fim_texto:
        texto_sem_espacos += texto[inicio_texto]
        inicio_texto += 1

    return texto_sem_espacos


def texto_eh_numero(texto):
    if len(texto) == 0:
        return False

    for caractere_atual in texto:
        if caractere_atual < "0" or caractere_atual > "9":
            return False

    return True


def converter_texto_para_inteiro(texto):
    numero_convertido = 0

    for caractere_atual in texto:
        valor_digito = ord(caractere_atual) - ord("0")
        numero_convertido = numero_convertido * 10 + valor_digito

    return numero_convertido


def separar_valores(texto):
    lista_valores = []
    valor_atual = ""

    for caractere_atual in texto:

        if caractere_atual == " " or caractere_atual == "\t":

            if len(valor_atual) > 0:
                lista_valores.append(valor_atual)
                valor_atual = ""

        else:
            valor_atual += caractere_atual

    if len(valor_atual) > 0:
        lista_valores.append(valor_atual)

    return lista_valores


def ordenar_valores(lista_numeros):

    quantidade_valores = len(lista_numeros)

    for posicao_inicial in range(quantidade_valores - 1):

        menor_posicao = posicao_inicial

        for proxima_posicao in range(posicao_inicial + 1, quantidade_valores):

            if lista_numeros[proxima_posicao] < lista_numeros[menor_posicao]:
                menor_posicao = proxima_posicao

        valor_temporario = lista_numeros[posicao_inicial]
        lista_numeros[posicao_inicial] = lista_numeros[menor_posicao]
        lista_numeros[menor_posicao] = valor_temporario


def ler_numero(mensagem, minimo, maximo):

    while True:

        texto_digitado = remover_espacos_extremidades(input(mensagem))

        if not texto_eh_numero(texto_digitado):
            print("Digite apenas números inteiros.")
            continue

        numero_lido = converter_texto_para_inteiro(texto_digitado)

        if numero_lido < minimo or numero_lido > maximo:
            print("Valor fora da restrição.")
            continue

        return numero_lido


def ler_linha_matriz(quantidade_colunas):

    while True:

        linha_digitada = remover_espacos_extremidades(input())

        lista_textos = separar_valores(linha_digitada)

        if len(lista_textos) != quantidade_colunas:
            print("Quantidade de valores incorreta.")
            continue

        linha_convertida = []
        entrada_valida = True

        for texto_numero in lista_textos:

            if not texto_eh_numero(texto_numero):
                entrada_valida = False
                break

            linha_convertida.append(converter_texto_para_inteiro(texto_numero))

        if entrada_valida:
            return linha_convertida

        print("Linha inválida.")


def organizar_containers(matriz_containers):

    quantidade_containers = len(matriz_containers)

    totais_containers = []

    for indice_container in range(quantidade_containers):

        total_container = 0

        for indice_tipo_bola in range(quantidade_containers):
            total_container += matriz_containers[indice_container][indice_tipo_bola]

        totais_containers.append(total_container)

    totais_tipos = []

    for indice_tipo_bola in range(quantidade_containers):

        total_tipo = 0

        for indice_container in range(quantidade_containers):
            total_tipo += matriz_containers[indice_container][indice_tipo_bola]

        totais_tipos.append(total_tipo)

    ordenar_valores(totais_containers)
    ordenar_valores(totais_tipos)

    for indice_comparacao in range(quantidade_containers):

        if totais_containers[indice_comparacao] != totais_tipos[indice_comparacao]:
            return "Impossible"

    return "Possible"


def programa_principal():

    quantidade_consultas = ler_numero(
        "Informe a quantidade de consultas: ",
        1,
        10
    )

    for consulta_atual in range(1, quantidade_consultas + 1):

        print("\nConsulta", consulta_atual)

        quantidade_containers = ler_numero(
            "Informe a quantidade de containers: ",
            1,
            100
        )

        matriz_containers = []

        print("Digite a matriz:")

        for linha_atual in range(quantidade_containers):

            linha = ler_linha_matriz(quantidade_containers)

            matriz_containers.append(linha)

        resultado = organizar_containers(matriz_containers)

        print("Resultado:", resultado)


programa_principal()
