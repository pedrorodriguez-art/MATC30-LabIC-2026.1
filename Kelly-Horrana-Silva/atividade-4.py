def organizar_conteineres(container: list[list[int]]) -> str:
    n = len(container)

    soma_linhas = []
    soma_colunas = [0] * n

    # soma de cada linha
    for i in range(n):
        soma_linhas.append(sum(container[i]))

    # soma de cada coluna
    for j in range(n):
        for i in range(n):
            soma_colunas[j] += container[i][j]

    # comparação final
    if sorted(soma_linhas) == sorted(soma_colunas):
        return "Possível"

    return "Impossível"


def main():
    q = int(input().strip())

    for _ in range(q):
        n = int(input().strip())
        container = []

        for _ in range(n):
            linha = list(map(int, input().split()))
            container.append(linha)

        print(organizar_conteineres(container))


if __name__ == "__main__":
    main()