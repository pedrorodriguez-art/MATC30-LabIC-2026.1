class No:
    def __init__(self, valor):
        self.valor = valor
        self.next = None 

    def imprimir(self): 
        return(f"Valor: {self.valor}")

class List:
    def __init__(self): 
        self.head = None 
        self.tail = None 

    def impressao(self): 
        if self.head == None:
            print ("Lista Vazia")
        else:
            print ("Imprimindo...")
            Atual = self.head
            while Atual != None:
                print (Atual.imprimir())
                Atual = Atual.next

    def append(self, valor):
        Nó = No(valor)
        if self.head == None:
            self.head = Nó
        else:
            Atual = self.head
            while Atual.next != None:
                Atual = Atual.next
            Atual.next = Nó

    def size(self):
        if self.head == None:
            return 0
        else:
            i=0
            Atual = self.head
            while Atual != None:
                Atual = Atual.next
                i+=1
            return i

    def soma(self):
        if self.head == None:
            return 0
        else:
            i=0
            Atual = self.head
            while Atual != None:
                i+=Atual.valor
                Atual = Atual.next
            return i
    
    def extrair_lista_ordenada(self):
        elementos = []
        Atual = self.head
        while Atual != None:
            elementos.append(Atual.valor)
            Atual = Atual.next
        elementos.sort()
        return elementos

    def comparar_com(self, outra_lista):
        return self.extrair_lista_ordenada() == outra_lista.extrair_lista_ordenada()


def organizingContainers(container):
    n = len(container)
    capacidades = List()
    totais_tipo = List()
    
    for i in range(n):
        soma_linha = sum(container[i])
        capacidades.append(soma_linha)
        
        soma_coluna = sum(container[j][i] for j in range(n))
        totais_tipo.append(soma_coluna)

    if capacidades.comparar_com(totais_tipo):
        return "Possible"
    else:
        return "Impossible"


def main():
    q = int(input().strip())
    while q <= 1 or q >= 10:
      q = int(input("Coloque um valor válido para q (1 <= q <= 10)").strip())
    for _ in range(q):
        n = int(input().strip())
        while n <=1 or n >= 100:
          n = int(input("Coloque um valor válido para n (1 <= n <= 100)").strip())
        container = []
        for _ in range(n):
            linha = list(map(int, input().rstrip().split()))
            container.append(linha)

        resultado = organizingContainers(container)
        print(resultado)

if __name__=="__main__":
    main()
