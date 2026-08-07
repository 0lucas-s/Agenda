contatos = []
contatos_favoritos = []

def adicionar_contato():
  nome = input("Digite o nome: ")
  numero = input("Digite o número: ")
  email = input("Digite o email: ")
  contato = {"Nome":nome, "Número":numero, "Email":email} # Criando um dicionario
  contatos.append(contato) # append para adicionar "contato" na lista "contatos"
  return

def favoritar_contato():
  while True:
    ver_contatos()
    favoritar = input('\nDigite o número de quem quer favoritar: ')
    indice_contato = int(favoritar) - 1 # Ajusta o número digitado para a posição correta na lista ex(escolhe: posição 2(3 no indice python), -1 volta para o python entender 2)
    if indice_contato >= 0 and indice_contato < len(contatos):
      contatos_favoritos.append(contatos[indice_contato]) # Pega o indice(indice_contato) digitado pelo usuario e adiciona na lista (contatos_favoritos)
      print(f"\nContato {favoritar} foi adicionado aos favoritos!") # aqui {favoritar} ja vai estar com um valor guardado, por isso não imprime o input denovo
      break
    else:
      print("\nEsse contato não existe!")

def ver_contatos():
  if not contatos: # Se não tiver contatos, então rodar o print abaixo
    print("\nNão tem contatos para ser adicionado!")
  else:
    print("\nContatos:")
    for indice, contato in enumerate(contatos, start=1): # Numéra automaticamente a lista 'contatos'
      print(f"\n{indice}. Nome: {contato['Nome']} | Número: {contato['Número']} | Email: {contato['Email']}")
  return

def ver_favoritos():
  if not contatos_favoritos:
    print('\nNão tem contatos favoritados!')
  else:
    print("\nContatos favoritos:")
    for indice, contato in enumerate(contatos_favoritos, start=1):
      print(f"\n{indice}. Nome: {contato['Nome']} | Número: {contato['Número']} | Email: {contato['Email']}")
  return


while True: # Faz rodar infinitamente até ser fechado
  print("\nAgenda de Contatos")
  print("\n1. Adicionar contato")
  print("2. Adicionar aos favoritos")
  print("3. Ver contatos")
  print("4. Ver favoritos")
  print("5. Editar contatos")
  print("6. Sair\n")

  escolha = input("Digite sua escolha de 1 a 6: ")

  if escolha == "1":
    adicionar_contato()
  elif escolha == "2":
    favoritar_contato()
  elif escolha == "3":
    ver_contatos()
  elif escolha == "4":
    ver_favoritos()
  elif escolha == "6":
    break # Pra fechar o programa no terminal