# Sistema de estacionamento com veiculos ilimitados
# Armazena varias placas enquanto o programa roda.

veiculos = []  # Lista para armazenar varios veiculos

# Adicionar veiculo
def adicionar(placa):
    placa = placa.upper().strip()

    if placa in veiculos:
        print("O veiculo", placa, "ja esta no patio.")
    else:
        veiculos.append(placa)
        print("Veiculo", placa, "foi adicionado ao patio.")

# Remover veiculo
def remover(placa):
    placa = placa.upper().strip()

    if placa not in veiculos:
        print("O veiculo", placa, "nao esta no patio.")
    else:
        veiculos.remove(placa)
        print("Veiculo", placa, "removido do patio.")

# Listar veiculos
def listar():
    if len(veiculos) == 0:
        print("O patio esta vazio.")
    else:
        print("Veiculos no patio:")
        for p in veiculos:
            print("-", p)

# Menu do usuario
def menu():
    while True:
        print("Sistema de Estacionamento")
        print("1 - Adicionar veiculo")
        print("2 - Remover veiculo")
        print("3 - Mostrar veiculos no patio")
        print("4 - Sair")

        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            placa = input("Digite a placa para adicionar: ")
            adicionar(placa)

        elif opcao == "2":
            placa = input("Digite a placa para remover: ")
            remover(placa)

        elif opcao == "3":
            listar()

        elif opcao == "4":
            print("Encerrando o sistema.")
            break

        else:
            print("Opcao invalida.")


menu()