def espaco_extremidade(texto):
    inicio = 0
    fim = len(texto) - 1

    while inicio <= fim and texto[inicio] == " ":
        inicio += 1

    while fim >= inicio and texto[fim] == " ":
        fim -= 1

    resultado = ""
    for i in range(inicio, fim + 1):
        resultado = resultado + texto[i]

    return resultado


def validacao_inteiro(texto):
    if len(texto) == 0:
        return False

    for i in range(len(texto)):
        c = texto[i]
        if c < "0" or c > "9":
            return False

    return True


def texto_para_inteiro(texto):
    valor = 0
    for i in range(len(texto)):
        digito = ord(texto[i]) - ord("0")
        valor = valor * 10 + digito
    return valor


def dividir_linha(linha):
    tokens = []
    token_atual = ""

    for c in linha:
        if c == " " or c == "\t":
            if len(token_atual) > 0:
                tokens.append(token_atual)
                token_atual = ""
        else:
            token_atual = token_atual + c

    if len(token_atual) > 0:
        tokens.append(token_atual)

    return tokens


def ordenar_crescente(arr):
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > chave:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave


def organizar_conteineres(container):
    n = len(container)

    soma_linha = []
    for i in range(n):
        total = 0
        for j in range(n):
            total = total + container[i][j]
        soma_linha.append(total)

    soma_coluna = []
    for j in range(n):
        total = 0
        for i in range(n):
            total = total + container[i][j]
        soma_coluna.append(total)

    ordenar_crescente(soma_linha)
    ordenar_crescente(soma_coluna)

    for k in range(n):
        if soma_linha[k] != soma_coluna[k]:
            return "Impossible"

    return "Possible"


def ler_inteiro_valido(mensagem, minimo, maximo):
    while True:
        entrada = espaco_extremidade(input(mensagem))

        if not validacao_inteiro(entrada):
            print("Entrada invalida. Digite um numero inteiro positivo.")
            continue

        valor = texto_para_inteiro(entrada)

        if valor < minimo or valor > maximo:
            print(f"Valor fora da restricao ({minimo} <= valor <= {maximo}).")
            continue

        return valor


def ler_linha_inteiros(mensagem, quantidade):
    while True:
        entrada = espaco_extremidade(input(mensagem))
        tokens = dividir_linha(entrada)

        if len(tokens) != quantidade:
            print(f"Esperado {quantidade} valores, recebido {len(tokens)}. Tente novamente.")
            continue

        valido = True
        valores = []

        for t in tokens:
            if not validacao_inteiro(t):
                print(f"Valor invalido: '{t}'. Use apenas inteiros >= 0.")
                valido = False
                break
            valores.append(texto_para_inteiro(t))

        if not valido:
            continue

        return valores


def consultas():
    return ler_inteiro_valido(
        "Digite o numero de consultas q (1 <= q <= 10): ", 1, 10
    )


def ler_matriz(consulta):
    print(f"\n--- Consulta {consulta} ---")

    n = ler_inteiro_valido(
        "Digite o numero de conteineres n (1 <= n <= 100): ", 1, 100
    )

    container = []
    for i in range(n):
        linha = ler_linha_inteiros(
            f"Linha {i} da matriz ({n} valores): ", n
        )
        container.append(linha)

    return container


def main():
    q = consultas()

    resultados = []
    for caso in range(1, q + 1):
        container = ler_matriz(caso)
        resultados.append(organizar_conteineres(container))

    print("\nSaida:")
    for resultado in resultados:
        print(resultado)


if __name__ == "__main__":
    main()