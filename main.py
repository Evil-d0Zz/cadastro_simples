from time import sleep

alunos = [['admin', 44, 'masculino', '99999999999']] #lista vazia

def listar():
  print("Lista de usuarios:")
  x = 0
  for user in alunos:
    print(f'{x}: Nome: {user[0]}, Idade: {user[1]}, Sexo: {user[2]}, CPF: {user[3]}')
    x += 1


while True:


  print("""
    
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
▓▓░░░░░░[01]░-░Adicionar usuarios░░░░░░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
▓▓░░░░░░[02]░-░Listar usuarios░░░░░░░░░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
▓▓░░░░░░[03]░-░Deletar usuario░░░░░░░░░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
▓▓░░░░░░[04]░-░Alterar usuario░░░░░░░░░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
▓▓░░░░░░[99]░-░Sair░░░░░░░░░░░░░░░░░░░░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
_______▒__________▒▒▒▒▒▒▒▒▒▒▒▒▒▒
______▒_______________▒▒▒▒▒▒▒▒        By: N3w.elf
_____▒________________▒▒▒▒▒▒▒▒
____▒___________▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
___▒
__▒______▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
_▒______▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓
▒▒▒▒___▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓
▒▒▒▒__▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓▒▓
▒▒▒__▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▒▒

  """)

  try:
    cmd = int(input("[!] Escolha uma opçao: "))
  except:

    print("Apenas Numeros!")

  if cmd == 1:
    nome  = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo: ")
    cpf = str(input("CPF: "))

    alunos.append(f'[{nome}, {idade}, {sexo}, {cpf}]')
    print(f"\nUsuario {nome} criado com sucesso!")

  elif cmd  == 2:
    listar()

  elif cmd == 3:
    listar()
    id = int(input("Defina o id do usuario: "))
    alunos.remove(alunos[id])

  elif cmd == 4:
    
    listar()
    id = int(input("Defina o id do usuario: "))
    alunos.remove(alunos[id])
    nome  = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo: ")
    cpf = str(input("CPF: "))

    alunos.append(f'[{nome}, {idade}, {sexo}, {cpf}]')
    print(f"\nUsuario {nome} alterado com sucesso!")
  
  elif cmd == 99:
    print("Saindo...")
    sleep(2)
    exit()
  else:
    print("Erro")
    break


