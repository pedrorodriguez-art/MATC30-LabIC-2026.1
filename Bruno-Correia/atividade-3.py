def main():
    """
    # Atividade 3 - Próxima ordem lexicográfica
    ## Descrição
    Essa função irá percorrer uma lista encadeada de palavras e retornar, para 
    cada uma delas, a menor string lexicograficamente maior possível. Caso não 
    seja possível formar uma palavra maior, ela retornará que não há resposta.

    ## Parâmetros
    | Parâmetro | Tipo | Descrição       |
    |-----------|------|-----------------|
    | `T`       | int  | Número de casos de teste (Tamanho da lista) |
    | `w`       | string | Palavras que serão adicionadas à Lista |

    ## Retorno
    Imprime no console a nova palavra reorganizada ou 
    "no answer" caso a palavra já esteja na sua maior combinação possível.
    """
    length = int(input())
    
    words = []
    for _ in range(length):
        word = input().strip()
        words.append(word)

    results = []
    for word in words:
        chars = list(word)
        n = len(chars)
        
        i = n - 2
        while i >= 0 and chars[i] >= chars[i + 1]:
            i -= 1
        
        if i == -1:
            results.append("no answer")
            continue
        
        j = n - 1
        while chars[j] <= chars[i]:
            j -= 1
        
        chars[i], chars[j] = chars[j], chars[i]
        chars[i + 1:] = chars[i + 1:][::-1]
        results.append("".join(chars))
    
    for res in results:
        print(res)

if __name__ == "__main__":
    main()