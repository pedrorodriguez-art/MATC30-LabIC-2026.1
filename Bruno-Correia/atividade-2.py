def main():
    ''''
    # Atividade 2 - Soma de todos os elementos de um array
    ## Descrição
    Essa função irá percorrer um array e retornar a soma de todos os itens dele.

    ## Parâmetros
    | Parâmetro | Tipo | Descrição       |
    |-----------|------|-----------------|
    | `length`       | int  | Tamanho do Array |
    | `numbers`       | int  | Valores que serão adicionados ao Array  |

    ## Retorno

    O retorno será um `int` retornando a soma de todos os itens do array.
    '''
    length = int(input())
    numbers_arr = list(map(int, input().split()))

    if length != len(numbers_arr):
        raise ValueError("wrong array length")

    total_sum = 0
    for number in numbers_arr:
        total_sum += number

    print(total_sum)

if __name__ == "__main__":
    main()