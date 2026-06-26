"""
Atividade 2 - Soma dos Elementos de um Array
"""

def soma_array(ar):
    soma = 0
    for i in range(len(ar)):
        soma = soma + ar[i]
    return soma

def main():
    n = int(input().strip())
    ar = list(map(int, input().split()))
    if len(ar) != n:
        print("Erro: quantidade de elementos diferente do informado.")
        return
    print(soma_array(ar))

if __name__ == "__main__":
    main()
