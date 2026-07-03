#Atividade 1 ->  Simples = 1 ponto
# Construa uma função para calcular a soma de dois números inteiros.


def soma(a, b):
    return a + b


def main():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    resultado = soma(num1, num2)

    print("Soma:", resultado)


if __name__ == "__main__":
    main()