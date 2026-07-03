def main():
    ''''
    # Atividade 1 — Soma de dois números inteiros
    ## Descrição
    - Função que recebe dois números inteiros e retorna a soma entre eles.

    ## Parâmetros
    | Parâmetro | Tipo | Descrição       |
    |-----------|------|-----------------|
    | `a`       | int  | O primeiro valor |
    | `b`       | int  | O segundo valor  |

    ## Retorno
    Do tipo `int` retorna a soma de a e b.

    ## Restrições
    - `1 ≤ a, b ≤ 1000`
    - Caso algum valor esteja fora do intervalo, retorna um erro.
    '''
    a = int(input("a = "))
    b = int(input("b = "))

    if not 1 <= a <= 1000:
        raise ValueError("Os valores devem estar entre 1 e 1000.")
    
    if not 1 <= b <= 1000:
        raise ValueError("Os valores devem estar entre 1 e 1000.")

    result = a + b
    print(result)

if __name__ == "__main__":
    main()