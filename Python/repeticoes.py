def repeticoes1():
  jogadores = []
  for i in range(6):
    jogador = {
      'nome': input("Digite o nome do Jogador: "),
      'idade': int(input("Digite o idade do Jogador: "))
    }
    jogadores.append(jogador)

  def idadeOrdenada(e):
    return e['idade']

  jogadores.sort(key=idadeOrdenada)
  for jogador in jogadores:
    print("Jogador com nome", jogador['nome'], "tem a idade de", jogador['idade'], "anos")


# repeticoes1()

def repeticoes2():
  alunos = []
  media_alunos = 0
  qtd_alunos = int(input("Quantos alunos tem na sala: "))
  for i in range(qtd_alunos):
    aluno = {
      "nome": input("Informe o nome do aluno "),
      "nota": float(input("Informe a nota do aluno "))
    }
    media_alunos = media_alunos + aluno['nota']
  media_alunos = media_alunos / qtd_alunos
  print("A média dos alunos foi de", media_alunos)

# repeticoes2()

def repeticoes3():
  numero_digitado = float(input("Digite um número: "))
  while numero_digitado >= 0:
    numero_digitado = float(input("Digite um número: "))

# repeticoes3()

def repeticoes4():
  resposta = 's'
  while resposta == 's':
    valor_compra = float(input("Digite o valor da sua compra: "))
    valor_passado = float(input("Digite o valor em dinheiro para passar: "))
    if valor_compra <= valor_passado:
      troco = valor_passado - valor_compra
      print("O seu troco será de", "R$", troco)
    else:
      print("Você não possui o dinheiro suficienta para a compra!")
      break
    resposta = input("Outra compra? Digite 's' para Sim e 'n' para Não")

# repeticoes4()