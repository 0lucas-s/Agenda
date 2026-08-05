contatos = []

def adicionar_contato():
  nome = input("Digite o nome: ")
  numero = input("Digite o número: ")
  email = input("Digite o email: ")
  contato = {"Nome":nome, "Número":numero, "Email":email}
  contatos.append(contato) # append para adicionar "contato" na lista "contatos"
  
def ver_contatos():
  if not contatos:
    print("\nNão tem contatos!\n")
  else:
    for contato in contatos:  
      print()
      print("Nome:", contato["Nome"], "| Número:", contato["Número"], "| Email:", contato["Email"])
    



while True: # Faz rodar infinitamente até ser fechado
  print("\nAgenda de Contatos")
  print("\n1. Adicionar contato")
  print("2. Adicionar aos favoritos")
  print("3. Ver contatos")
  print("4. Editar contatos")
  print("5. Sair\n")

  escolha = input("Digite sua escolha de 1 a 5: ")

  if escolha == "1":
    adicionar_contato()
  elif escolha == "3":
    ver_contatos()
  elif escolha == "5":
    break # Pra fechar o programa no terminal