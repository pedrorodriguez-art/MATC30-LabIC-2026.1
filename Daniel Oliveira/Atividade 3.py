def proxima_palavra(w):
    letras = list(w)
    tamanho = len(letras)
    
    i = tamanho - 2
    while i >= 0 and letras[i] >= letras[i + 1]:
        i -= 1
        
    if i == -1:
        return "no answer"
        
    j = tamanho - 1
    while letras[j] <= letras[i]:
        j -= 1
        
    letras[i], letras[j] = letras[j], letras[i]
    
    esquerda = i + 1
    direita = tamanho - 1
    while esquerda < direita:
        letras[esquerda], letras[direita] = letras[direita], letras[esquerda]
        esquerda += 1
        direita -= 1
    
    return "".join(letras)

t = int(input())
res = []

for _ in range(t):
    w = input().strip()
    res.append(proxima_palavra(w))

for r in res:
    print(r)

