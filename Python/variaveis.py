def variaveis1():
  nomeUsuario = input("Digite seu nome: ")
  idadeUsuario = int(input("Digite sua Idade: "))
  print("Olá,", nomeUsuario, "seja bem vindo!", "Você possui", idadeUsuario, "Anos")


# variaveis1()

def variaveis2():
  pesoUsuario = float(input("Digite seu peso: "))
  aguaPorPeso = 35
  aguaUsuario = pesoUsuario * aguaPorPeso /1000
  print("Você deve beber", aguaUsuario, "L por dia")


# variaveis2()

def variaveis3():
  salario_bruto = float(input("Digite seu salario bruto: "))
  desconto_prev = salario_bruto * 0.12
  desconto_vt = salario_bruto * 0.06
  salario_liquido = salario_bruto - desconto_prev - desconto_vt
  print("Seu salário líquido é de R$ ",salario_liquido)

# variaveis3()