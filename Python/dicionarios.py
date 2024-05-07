def dicionarios1():
  listaContatos = [
    {
      'nome': 'Myrian',
      'telefone': "65 999323992"
    },
    {
      'nome': 'Claudia',
      'telefone': "65 84549168"
    },
    {
      'nome': 'Marcio',
      'telefone': "65 981698059"
    },
  ]
  status = True
  while status:
    print("======= Escolha uma das seguintes opções ======= ")
    print("Mostrar todos os contatos (1) ")
    print("Adicionar um novo Contato (2) ")
    print("Buscar número de telefone atráves do nome (3) ")
    print("Remover um contato (4) ")
    print("Sair (5) ")
    opcoes = int(input("Digite uma das opções: "))

    if opcoes == 1:
      print("Lista de Contatos:")
      for contato in listaContatos:
        print(f"Nome: {contato['nome']} - Telefone: {contato['telefone']}")
    elif opcoes == 2:
      print("Novo Contato")
      novoContato = {
        'nome': input('Digite o nome do contato: '),
        'telefone': input('Digite o telefone do contato: ')
      }
      listaContatos.append(novoContato)
    elif opcoes == 3:
      print("Buscar atráves do nome do contato")
      nomeContato = input("Digite o nome do contato: ")
      for contato in listaContatos:
        if nomeContato == contato['nome']:
          print("Resultado da busca: ", f"Nome Contato: {contato['nome']} - Telefone Contato: {contato['telefone']}")
    elif opcoes == 4:
      print("Remover o Contato") 
      for contato in listaContatos:
        print(f"Nome: {contato['nome']} - Telefone: {contato['telefone']}")
      removerContato = input("Digite o nome do Contato a ser excluido") 
      for contato in listaContatos:
        if removerContato == contato['nome']:
          listaContatos.remove(contato)
    elif opcoes == 5:
      print("Programa irar encerrar!")
      status = False

# dicionarios1()


def dicionarios2():
  biblioteca = {
    'livro1': {
      'autor': 'Jofrey',
      'titulo': 'A vingança de Baltazar',
      'ano_publicacao': '2010'
    },
    'livro2': {
      'autor': 'Jofrey',
      'titulo': 'O retorno de Baltazar',
      'ano_publicacao': '2011'
    },
    'livro3': {
      'autor': 'Jofrey',
      'titulo': 'O ínicio de Baltazar',
      'ano_publicacao': '2009'
    }
  }
  print("======== LIVROS DA BIBLIOTECA ========")
  for livros in biblioteca.values():
    print("Livro:", livros['titulo'])
  escolhaUsuario = input("Digite o livro que voce gostaria de ver os detalhes: ")
  for livros in biblioteca.values():
    if escolhaUsuario == livros['titulo']:
      print('\nDetalhes sobre o livro:', escolhaUsuario)
      print('Titulo:', livros['titulo'])
      print('Autor:', livros['autor'])
      print('Ano da Publicação:', livros['ano_publicacao'])
    

# dicionarios2()