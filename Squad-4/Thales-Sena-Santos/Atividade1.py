def soma(a, b):
    a, b = int(a), int(b)
    if a  >= 1 and b <= 1000:
        resultado = a + b
    return resultado


if __name__ == '__main__':

    a = input ("Digite um número: ")
    b = input ("Digite outro número: ")

    print(soma(a, b))