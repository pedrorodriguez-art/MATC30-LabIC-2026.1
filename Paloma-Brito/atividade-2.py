#Atividade 2 -> Simples = 1 ponto
# Dado um array de inteiros, encontre a soma de seus elementos.

def calcular_soma_elementos(lista_numeros):
    resultado_soma = 0

    for numero_atual in lista_numeros:
        resultado_soma = resultado_soma + numero_atual

    return resultado_soma


quantidade_elementos = int(input("Informe a quantidade de elementos da lista: "))

lista_numeros = []

print("Digite os números da lista:")

for quantidade_lida in range(quantidade_elementos):
    valor_informado = int(input())
    lista_numeros.append(valor_informado)

resultado = calcular_soma_elementos(lista_numeros)

print("Resultado da soma:", resultado)
