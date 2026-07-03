class No:
  def __init__(self, valor): # Criador dos nós
    self.valor = valor # Atribuição do valor ao nó
    self.next = None # Próximo nó

  def imprimir(self): # Função de imprimir os valores dos nós
    return(f"Valor: {self.valor}")

class List:
  def __init__(self): # Criador da lista
    self.head = None # Inicio da lista (Até agora vazia)
    self.tail = None # Final da Lista

  def impressao(self): # Imprime todos os elementos da lista
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

  def size(self): # Diz a quantidade de termos na lista
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

def main():
  Lista = List()
  tamanho = int(input("Digite o tamanho da lista: "))
  while tamanho < 0:
    print("Tamanho inválido, necessita ser no mínimo 0.")
    tamanho = int(input("Digite o tamanho da lista: "))

  for k in range(tamanho):
    valor = int(input("Digite o valor: "))
    while valor < 1000:
      print("Valor inválido")
      valor = int(input("Digite o valor: "))
    Lista.append(valor)

  print(f"Soma dos valores: {Lista.soma()}")

if __name__=="__main__":
  main()
