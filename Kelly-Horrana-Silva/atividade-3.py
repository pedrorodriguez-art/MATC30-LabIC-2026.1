# Atividade 3 → Intermediária = 1 ponto
# A ordem lexicográfica é conhecida como ordem alfabética para strings. Uma string é maior que
# outra se aparece depois em uma lista ordenada lexicograficamente.
# Dada uma palavra, crie uma nova palavra trocando alguns ou todos os seus caracteres. Essa nova
# palavra deve atender a dois critérios:
# • Deve ser maior que a palavra original.
# • Deve ser a menor palavra que atende à primeira condição.
# Se não for possível, retorne "no answer".

def proxima_palavra(palavra):
    letras = list(palavra)
    n = len(letras)

    i = n - 2
    while i >= 0 and letras[i] >= letras[i + 1]:
        i -= 1

    if i == -1:
        return "no answer"

    j = n - 1
    while letras[j] <= letras[i]:
        j -= 1

    letras[i], letras[j] = letras[j], letras[i]

    letras[i + 1:] = sorted(letras[i + 1:])

    return "".join(letras)


def main():
    palavra = input("Digite uma palavra: ")

    print(proxima_palavra(palavra))


if __name__ == "__main__":
    main()