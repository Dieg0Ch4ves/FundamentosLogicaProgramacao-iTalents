import random

def listas1():
  listaNumeros = []
  for i in range(10):
    numeroAleatorio = random.randrange(100)
    listaNumeros.append(numeroAleatorio)
  numeroPalpite = int(input("Digite um número: "))
  if numeroPalpite in listaNumeros:
    print("Você acertou!")
  else:
    print("Não foi desta vez!")
  for numero in listaNumeros:
    print("A lista possuia :", numero)
  print("O maior número da lista era :", max(listaNumeros))
  print("O menor número da lista era : ", min(listaNumeros))
  listaNumeroMedia = sum(listaNumeros) / len(listaNumeros)
  print("A média dos números da lista era :", listaNumeroMedia)

# listas1()

def listas2():
  status = True
  listaCompras = []
  while(status):
    opcoes = int(input("Escolha uma opção: 1 - Adicionar um novo item na lista de compras, 2 - Exibir a lista de compras e 3 - Para encerrar o programa: "))
    if opcoes == 1:
      novoItem = input("Escreva o novo item para adicionar na lista: ")
      listaCompras.append(novoItem)
    elif opcoes == 2:
      print("Sua lista possui os seguintes itens")
      for item in listaCompras:
        print("Item :", item)
      print("E possui um total de", len(listaCompras), "itens")
    elif opcoes == 3:
      print("O programa irar encerrar")
      status = False
    else:
      print("Escolha uma opção válida!")
    
# listas2()

def listas3():
  tuplaAluno = ("Gabriel", 9, 10, 4, 10, 4)
  nomeAluno, notaPort, notaMat, notaCie, notaArt, notaIng = tuplaAluno
  listaNota = list(tuplaAluno)
  listaNota.pop(0)
  listaNotaMedia = sum(listaNota) / len(listaNota)
  print(f"\n Nome aluno: {nomeAluno}")
  print(f"Nota de Português: {notaPort}")
  print(f"Nota de Matemática: {notaMat}")
  print(f"Nota de Ciências: {notaCie}")
  print(f"Nota de Artes: {notaArt}")
  print(f"Nota de Inglês: {notaIng}")
  if listaNotaMedia >= 6:
    print("Aluno foi Aprovado! Com a média: ", listaNotaMedia)
  else:
    print("Aluno foi Reprovado! Com a média: ", listaNotaMedia )

# listas3()