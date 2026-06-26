def ordenar(valores):
    total_elementos = len(valores)

    for posicao_atual in range(total_elementos - 1):
        menor_posicao = posicao_atual

        for posicao_comparacao in range(posicao_atual + 1, total_elementos):
            if valores[posicao_comparacao] < valores[menor_posicao]:
                menor_posicao = posicao_comparacao

        if menor_posicao != posicao_atual:
            troca = valores[posicao_atual]
            valores[posicao_atual] = valores[menor_posicao]
            valores[menor_posicao] = troca


def organizingContainers(matriz):

    dimensao = len(matriz)

    total_por_container = [0] * dimensao
    total_por_tipo = [0] * dimensao

    for indice_linha in range(dimensao):
        soma_linha = 0
        for indice_coluna in range(dimensao):
            soma_linha += matriz[indice_linha][indice_coluna]
        total_por_container[indice_linha] = soma_linha

    for indice_coluna in range(dimensao):
        soma_coluna = 0
        for indice_linha in range(dimensao):
            soma_coluna += matriz[indice_linha][indice_coluna]
        total_por_tipo[indice_coluna] = soma_coluna

    ordenar(total_por_container)
    ordenar(total_por_tipo)

    for posicao in range(dimensao):
        if total_por_container[posicao] != total_por_tipo[posicao]:
            return "Impossible"

    return "Possible"


def ler_matriz(tamanho_matriz):
    dados = []
    for _ in range(tamanho_matriz):
        entrada = input().split()
        linha_atual = []
        for item in entrada:
            linha_atual.append(int(item))
        dados.append(linha_atual)
    return dados


def main():
    quantidade_testes = int(input())
    for _ in range(quantidade_testes):
        tamanho_matriz = int(input())
        dados = ler_matriz(tamanho_matriz)
        print(organizingContainers(dados))


if __name__ == "__main__":
    main()
