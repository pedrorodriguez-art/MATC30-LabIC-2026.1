
def proxima_palavra(palavra):
    letras=list(palavra)
    i=len(letras)-2
    while i>=0 and letras[i]>=letras[i+1]:
        i-=1
    if i==-1:
        return "no answer"
    j=len(letras)-1
    while letras[j]<=letras[i]:
        j-=1
    letras[i],letras[j]=letras[j],letras[i]
    letras[i+1:]=sorted(letras[i+1:])
    return "".join(letras)

t=int(input())
for _ in range(t):
    print(proxima_palavra(input().strip()))
