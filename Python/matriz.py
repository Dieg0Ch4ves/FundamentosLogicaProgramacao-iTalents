import random

def matriz1():
  notasAlunos = []
  for indexAluno in range(3):
    alunoLinha = [] 
    notasAlunos.append(alunoLinha)
    for i in range(5):
      notaAluno = float(input(f"Digite a nota do aluno {indexAluno + 1}: "))
      alunoLinha.append(notaAluno)
  for notas in notasAlunos:
    mediaAluno = sum(notas) / len(notas)
    print("Média do Aluno: ", mediaAluno)

# matriz1()

def matriz2():
  ordem = int(input("Informe a ordem da matriz: "))
  matriz = [[random.randint(1, 10) for j in range(ordem)] for i in range(ordem)]
  diagPrimaria = sum(matriz[i][i] for i in range(ordem))
  diagSecundaria = sum(matriz[i][ordem - i - 1] for i in range(ordem))
  diferencaDiag = diagPrimaria - diagSecundaria

  print("Matriz completa: ")
  for linha in matriz:
    print(linha)
  print(f"A diferença das diagonais é de ", diferencaDiag)

matriz2()