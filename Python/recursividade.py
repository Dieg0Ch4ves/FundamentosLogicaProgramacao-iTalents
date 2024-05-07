def recursividade1():
  numeroUsuario = float(input("Informe um número"))
  def fatoracao(numero):
    if numero < 10:
      print("Numéro não pode ser fatorado", 'Número: ', numero)
    else:
      print(f"Fatorando: {numero}")
      numeroFatorado = numero / 10
      fatoracao(numeroFatorado)
  fatoracao(numeroUsuario)

# recursividade1()

def recursividade2():
  def fibonacci(n):
    if n <= 2:
      return n - 1
    else:
      return fibonacci(n - 1) + fibonacci(n - 2)
  
  termoUsuario = int(input("Digite um número da sequência de Fibonacci: "))
  resultado = fibonacci(termoUsuario)
  print(f"O termo {termoUsuario} da sequência de Fibonacci é {resultado}")
    
recursividade2()