def encontrar_proxima_permutacao(palavra):
    caracteres = list(palavra)
    tamanho = len(caracteres)
    indice_pivo = tamanho - 2

    while (
        indice_pivo >= 0
        and caracteres[indice_pivo] >= caracteres[indice_pivo + 1]
    ):
        indice_pivo -= 1

    if indice_pivo < 0:
        return "no answer"

    indice_sucessor = tamanho - 1

    while caracteres[indice_sucessor] <= caracteres[indice_pivo]:
        indice_sucessor -= 1

    caracteres[indice_pivo], caracteres[indice_sucessor] = (
        caracteres[indice_sucessor],
        caracteres[indice_pivo],
    )

    caracteres[indice_pivo + 1:] = reversed(caracteres[indice_pivo + 1:])

    return "".join(caracteres)


quantidade_casos = int(input())

for _ in range(quantidade_casos):
    palavra = input().strip()
    print(encontrar_proxima_permutacao(palavra))
    