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

  a = int(input("Digite o valor de a: "))
  while a > 1000 or a < 1:
    print("Valor inválido")
    a = int(input("Digite outro valor (1000 >= a >=1): "))
  Lista.append(a)
  b = int(input("Digite o valor de b: "))
  while b > 1000 or b < 1:
    print("Valor inválido")
    b = int(input("Digite outro valor (1000 >= b >=1): "))
  Lista.append(b)

  print(f"Soma dos valores: {Lista.soma()}")

if __name__=="__main__":
  main()
