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

  def processar_lexicografia(self):
    if self.head == None:
      print("Lista Vazia")
      return
    Atual = self.head
    while Atual != None:
      w = Atual.valor
      caracteres = list(w) 
      n = len(caracteres)
      i = n - 2
      while i >= 0 and caracteres[i] >= caracteres[i + 1]:
        i -= 1
      if i == -1:
        print("no answer")
      else:
        j = n - 1
        while caracteres[j] <= caracteres[i]:
          j -= 1
        caracteres[i], caracteres[j] = caracteres[j], caracteres[i]
        caracteres[i + 1:] = reversed(caracteres[i + 1:])
        print("".join(caracteres))
      Atual = Atual.next

def main():
  Lista_Palavras = List()
  T = int(input("Digite a quantidade de casos de teste (T): "))
  while T < 1 or T > 100000:
    print("Valor inválido")
    T = int(input("Digite outro valor para T: "))
  for i in range(T):
    w = input(f"Digite a palavra {i+1}: ").strip()
    Lista_Palavras.append(w)
  Lista_Palavras.processar_lexicografia()

if __name__=="__main__":
  main()
