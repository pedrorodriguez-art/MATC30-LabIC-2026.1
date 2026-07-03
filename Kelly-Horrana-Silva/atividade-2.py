#Atividade 2 -> Simples = 1 ponto
# Dado um array de inteiros, encontre a soma de seus elementos.

def soma_elementos(lista):
    return sum(lista)


def main():
    numeros = list(map(int, input("Digite os números separados por espaço: ").split()))

    resultado = soma_elementos(numeros)

    print("Soma dos elementos:", resultado)


if __name__ == "__main__":
    main()