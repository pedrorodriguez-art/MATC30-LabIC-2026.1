def simpleArraySum(ar):
    soma = 0

    for numero in ar:
        soma += numero

    return soma



if __name__ == '__main__':
    
    print("     Soma dos Elementos de um Array")

    n = int(input("Qual o tamanho do array? "))

    numeros = list(map(int, input(
        f"Quais números nesse array? "
    ).split()))

    soma = simpleArraySum(numeros)

    print(f"Array informado : {numeros}")
    print(f"A soma desse array é: {soma}")
