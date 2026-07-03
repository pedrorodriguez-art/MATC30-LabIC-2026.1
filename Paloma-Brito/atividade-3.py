# Atividade 3 → Intermediária = 1 ponto
# A ordem lexicográfica é conhecida como ordem alfabética para strings. Uma string é maior que
# outra se aparece depois em uma lista ordenada lexicograficamente.
# Dada uma palavra, crie uma nova palavra trocando alguns ou todos os seus caracteres. Essa nova
# palavra deve atender a dois critérios:
# • Deve ser maior que a palavra original.
# • Deve ser a menor palavra que atende à primeira condição.
# Se não for possível, retorne "no answer".

def encontrar_proxima_palavra(palavra_original):
    lista_caracteres = list(palavra_original)

    posicao_troca = -1

    for indice_atual in range(len(lista_caracteres) - 2, -1, -1):

        if lista_caracteres[indice_atual] < lista_caracteres[indice_atual + 1]:
            posicao_troca = indice_atual
            break

    if posicao_troca == -1:
        return "no answer"

    posicao_substituta = posicao_troca + 1

    for indice_atual in range(posicao_troca + 1, len(lista_caracteres)):

        if (
            lista_caracteres[indice_atual] > lista_caracteres[posicao_troca]
            and lista_caracteres[indice_atual]
            <= lista_caracteres[posicao_substituta]
        ):
            posicao_substituta = indice_atual

    caractere_auxiliar = lista_caracteres[posicao_troca]
    lista_caracteres[posicao_troca] = lista_caracteres[posicao_substituta]
    lista_caracteres[posicao_substituta] = caractere_auxiliar

    inicio = posicao_troca + 1
    fim = len(lista_caracteres) - 1

    while inicio < fim:

        caractere_auxiliar = lista_caracteres[inicio]
        lista_caracteres[inicio] = lista_caracteres[fim]
        lista_caracteres[fim] = caractere_auxiliar

        inicio += 1
        fim -= 1

    return "".join(lista_caracteres)


quantidade_casos_teste = int(input())

for quantidade_processada in range(quantidade_casos_teste):

    palavra_informada = input()
