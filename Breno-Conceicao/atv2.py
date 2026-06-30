#ATIVIDADE 2 - BRENO

def somar_array(ar):
    total = 0
    for i in range(len(ar)):
        total = total + ar[i]
    return total


def validacao(texto):
    if len(texto) == 0:
        return False

    inicio = 0
    if texto[0] == "-":
        inicio = 1
        if len(texto) == 1:
            return False

    for i in range(inicio, len(texto)):
        caractere = texto[i]
        if caractere < "0" or caractere > "9":
            return False

    return True


def texto_para_inteiro(texto):
    negativo = texto[0] == "-"
    inicio = 1 if negativo else 0

    valor = 0
    for i in range(inicio, len(texto)):
        digito = ord(texto[i]) - ord("0")
        valor = valor * 10 + digito

    return -valor if negativo else valor


def espaco(texto):
    palavras = []
    palavra_atual = ""

    for i in range(len(texto)):
        caractere = texto[i]
        if caractere == " ":
            if len(palavra_atual) > 0:
                palavras.append(palavra_atual)
                palavra_atual = ""
        else:
            palavra_atual = palavra_atual + caractere

    if len(palavra_atual) > 0:
        palavras.append(palavra_atual)

    return palavras


def tamanho():
    while True:
        entrada = input("Digite o tamanho do array (n > 0): ")

        if not validacao(entrada):
            print("Entrada invalida. Digite um numero inteiro.")
            continue

        n = texto_para_inteiro(entrada)

        if n <= 0:
            print("Valor fora da restricao. n deve ser maior que 0.")
            continue

        return n


def array(n):
    while True:
        entrada = input(f"Digite os {n} elementos separados por espaço: ")
        valores_texto = espaco(entrada)

        if len(valores_texto) != n:
            print(f"Quantidade invalida. Digite exatamente {n} numeros.")
            continue

        ar = []
        entrada_valida = True

        for valor_texto in valores_texto:
            if not validacao(valor_texto):
                print(f"'{valor_texto}' nao e um numero inteiro valido.")
                entrada_valida = False
                break

            valor = texto_para_inteiro(valor_texto)

            if valor > 1000:
                print(f"Valor {valor} fora da restricao (ar[i] <= 1000).")
                entrada_valida = False
                break

            ar.append(valor)

        if entrada_valida:
            return ar


def main():
    n = tamanho()
    ar = array(n)

    print(f"Saída: {somar_array(ar)}")


if __name__ == "__main__":
    main()