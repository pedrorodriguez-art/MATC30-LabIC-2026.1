def somar(a, b):
    return a + b


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


def soma(mensagem, minimo, maximo):
    while True:
        entrada = input(mensagem)

        if not validacao(entrada):
            print("Entrada invalida. Digite um numero inteiro.")
            continue

        valor = texto_para_inteiro(entrada)

        if valor < minimo or valor > maximo:
            print(f"Valor fora da restricao ({minimo} <= valor <= {maximo}).")
            continue

        return valor


def main():
    a = soma("Digite o valor de a (1 <= a <= 1000): ", 1, 1000)
    b = soma("Digite o valor de b (1 <= b <= 1000): ", 1, 1000)

    print(f"Saída: {somar(a, b)}")


if __name__ == "__main__":
    main()