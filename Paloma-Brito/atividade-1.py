#Atividade 1 ->  Simples = 1 ponto
# Construa uma função para calcular a soma de dois números inteiros.

def calcular_soma(primeiro_valor, segundo_valor):
    resultado_soma = primeiro_valor + segundo_valor
    return resultado_soma


primeiro_valor = int(input("Digite o primeiro número inteiro:" ))
segundo_valor = int(input("Digite o segundo número inteiro: "))

resultado = calcular_soma(primeiro_valor, segundo_valor)

print("Resultado da soma:", resultado)
