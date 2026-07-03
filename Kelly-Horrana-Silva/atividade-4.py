def organizar_conteineres(matriz):
    quantidade = len(matriz)

    capacidade_conteiner = []
    quantidade_tipo_bola = [0] * quantidade

    # Soma das bolas em cada contêiner
    for linha in matriz:
        capacidade_conteiner.append(sum(linha))

    # Soma das bolas de cada tipo
    for i in range(quantidade):
        for j in range(quantidade):
            quantidade_tipo_bola[j] += matriz[i][j]

    if sorted(capacidade_conteiner) == sorted(quantidade_tipo_bola):
        return "Possible"

    return "Impossible"


def main():
    n = int(input("Quantidade de contêineres: "))

    matriz = []

    print("Digite a matriz:")

    for _ in range(n):
        linha = list(map(int, input().split()))
        matriz.append(linha)

    resultado = organizar_conteineres(matriz)
    print(resultado)


if __name__ == "__main__":
    main()