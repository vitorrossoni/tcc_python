import datetime
import random


veiculos = []



def adicionar(placa):
    placa = placa.upper().strip()
    if placa in veiculos:
        print("O veículo", placa, "já está no pátio.")
    else:
        veiculos.append(placa)
        print("Veículo", placa, "adicionado ao pátio.")


def remover(placa):
    placa = placa.upper().strip()
    if placa not in veiculos:
        print("O veículo", placa, "não está no pátio.")
    else:
        veiculos.remove(placa)
        print("Veículo", placa, "removido do pátio.")


def listar():
    if len(veiculos) == 0:
        print("O pátio está vazio.")
    else:
        print("Veículos no pátio:")
        for p in veiculos:
            print("-", p)



def gerar_tempos():
    month = random.randint(1, 12)
    entrada = datetime.datetime(2025, month, random.randint(1, 28),
                                random.randint(0, 23), random.randint(0, 59), 0)

    saida = datetime.datetime(2025, month, random.randint(entrada.day, 28),
                              random.randint(entrada.hour, 23), random.randint(0, 59), 0)

    return entrada, saida


def calcular_valor():
    tarifa = 10  # R$10 por hora

    entrada, saida = gerar_tempos()
    horas = saida.hour - entrada.hour
    valor_total = horas * tarifa

    return entrada, saida, horas, valor_total




def pagamento():
    metodos = ["pix", "debito", "credito", "dinheiro"]

    print("Escolha uma forma de pagamento:")
    for i, m in enumerate(metodos):
        print(f"{i} - {m}")

    escolha = int(input("Digite o número da forma de pagamento: "))

    if 0 <= escolha < len(metodos):
        return metodos[escolha]
    else:
        print("Opção inválida. Pagamento definido como dinheiro.")
        return "dinheiro"




def menu():
    while True:
        print("\n=== SISTEMA DE ESTACIONAMENTO ===")
        print("1 - Adicionar veículo")
        print("2 - Remover veículo")
        print("3 - Mostrar veículos no pátio")
        print("4 - Realizar pagamento de um veículo")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            placa = input("Digite a placa para adicionar: ")
            adicionar(placa)

        elif opcao == "2":
            placa = input("Digite a placa para remover: ")
            remover(placa)

        elif opcao == "3":
            listar()

        elif opcao == "4":
            if len(veiculos) == 0:
                print("Nenhum veículo no pátio.")
                continue

            listar()
            placa = input("Digite a placa que deseja pagar: ").upper()

            if placa not in veiculos:
                print("Essa placa não está no pátio.")
                continue

            entrada, saida, horas, total = calcular_valor()
            metodo = pagamento()

            print("\n=========== RECIBO ===========")
            print("Veículo:", placa)
            print("Entrada:", entrada)
            print("Saída:", saida)
            print("Tempo total:", horas, "horas")
            print("Valor total: R$", total)
            print("Forma de pagamento:", metodo)
            print("==============================")

            remover(placa)

        elif opcao == "5":
            print("Encerrando o sistema.")
            break

        else:
            print("Opção inválida.")


menu()
