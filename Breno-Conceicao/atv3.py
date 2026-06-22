def ordenar_crescente(letras, inicio):
    for i in range(inicio + 1, len(letras)):
        atual = letras[i]
        j = i - 1
        while j >= inicio and letras[j] > atual:
            letras[j + 1] = letras[j]
            j -= 1
        letras[j + 1] = atual
    return letras


def proxima(w):
    letras = list(w)
    tamanho = len(letras)

    i = tamanho - 2
    while i >= 0 and letras[i] >= letras[i + 1]:
        i -= 1

    if i < 0:
        return "no answer"

    menor_maior_indice = i + 1
    for j in range(i + 1, tamanho):
        if letras[j] > letras[i] and letras[j] < letras[menor_maior_indice]:
            menor_maior_indice = j

    letras[i], letras[menor_maior_indice] = letras[menor_maior_indice], letras[i]
    letras = ordenar_crescente(letras, i + 1)

    resultado = ""
    for k in range(len(letras)):
        resultado = resultado + letras[k]

    return resultado


def minuscula(caractere):
    codigo = ord(caractere)
    return ord('a') <= codigo <= ord('z')


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


def validacao(texto):
    if len(texto) == 0:
        return False

    for i in range(len(texto)):
        caractere = texto[i]
        if caractere < "0" or caractere > "9":
            return False

    return True


def texto_para_inteiro(texto):
    valor = 0
    for i in range(len(texto)):
        digito = ord(texto[i]) - ord("0")
        valor = valor * 10 + digito
    return valor


def validacao_palavra(w):
    tamanho = len(w)

    if tamanho < 1 or tamanho > 100:
        return False, f"tamanho invalido ({tamanho}). Deve ser 1 <= tamanho <= 100."

    for caractere in w:
        if not minuscula(caractere):
            return False, f"caractere invalido '{caractere}'. Use apenas [a-z]."

    return True, ""


def casos():
    while True:
        entrada = input("Digite o numero de casos de teste T (1 <= T <= 100000): ")

        if not validacao(entrada):
            print("Entrada invalida. Digite um numero inteiro positivo.")
            continue

        t = texto_para_inteiro(entrada)

        if t < 1 or t > 100000:
            print("Valor fora da restricao (1 <= T <= 100000).")
            continue

        return t


def ler_palavra_valida(numero_caso):
    while True:
        entrada = input(f"Digite a palavra do caso de teste {numero_caso}: ")
        w = espaco_extremidade(entrada)

        valida, motivo = validacao_palavra(w)
        if not valida:
            print(f"Entrada invalida: {motivo}")
            continue

        return w


def main():
    t = casos()

    resultados = []
    for caso in range(1, t + 1):
        w = ler_palavra_valida(caso)
        resultados.append(proxima(w))

    print("Saida:")
    for resultado in resultados:
        print(resultado)


if __name__ == "__main__":
    main()