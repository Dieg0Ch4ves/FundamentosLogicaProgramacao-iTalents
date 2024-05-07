import string

def funcoes1():
  
  def soma (a, b):
    return a + b

  def subtracao(a, b):
    return a - b

  def multiplicacao(a, b):
    return a * b

  def divisao (a, b):
    return a / b

  def calculadora(a, b, tipo):
    if tipo == 1:
      return soma(a, b)
    
    if tipo == 2:
      return subtracao(a, b)
    
    if tipo == 3:
      return multiplicacao(a, b)
    
    if tipo == 4:
      return divisao(a, b)
    
    if tipo < 1 or tipo > 4:
      return "Tipo de operação inválida"

  valorA = float(input("Informe o valor 1 a calcular: "))
  valorB = float(input("Informe o valor 2 a calcular: "))
  tipoOperacao = int(input("Informe o tipo de operação, Obs > 1 = soma, 2 = subtração, 3 = multiplicação e 4 = divisão: "))
  print(f"O resultado da operação é ", calculadora(valorA, valorB, tipoOperacao))

# funcoes1()

def funcoes2():
  sequencia = input("Digite a frase palíndromo: ")
  sequenciaFinal = sequencia.lower()
  sequenciaFinal = sequencia.replace(" ", "")
  pontuacoes = string.punctuation
  tabela_de_traducao = str.maketrans('', '', pontuacoes)
  sequenciaFinal = sequenciaFinal.translate(tabela_de_traducao)
  
  sequenciaInvertida = sequenciaFinal[::-1]
  if sequenciaFinal == sequenciaInvertida:
    print(f"Sua frase é um palídromo!\n frase normal: {sequenciaFinal} \n frase invertida: {sequenciaInvertida} ")
  else: 
    print(f"Sua frase NÃO é um palídromo!\n frase normal: {sequenciaFinal} \n frase invertida: {sequenciaInvertida} ")

# funcoes2()