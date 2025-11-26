import datetime
import random



print("ola,seja bem vindo ao estacionamento\n" \
"tabela de preços:1 hora = R$10,00, menos de uma hora = R$00,00")

entrada:datetime.time
saida:datetime.time
tempo:datetime.time
tarifa = 10
pagamento = ["pix","debito","credito","dinheiro"]
carrinho = []
sair = False
encerrar = ""







month = random.randint(1,12)
entrada = datetime.datetime(2025, month,random.randint(1,31), random.randint(0,24),random.randint(0,59), 0)
saida = datetime.datetime(2025, month,random.randint(entrada.day,31), random.randint(entrada.hour,24),random.randint(0,59), 0)





print(f'\ndata de entrada e saida:{entrada} {saida}\n')

def calculateTime():
     return saida.hour - entrada.hour

valorTotal = calculateTime() * tarifa
print(f"valor total:{valorTotal}\n")


while sair == False:

    print (f"escolha uma forma de pagamento:\npix [0],debito [1],credito [2],dinheiro[3]\n{pagamento[0]}\n{pagamento[1]}\n{pagamento[2]}\n{pagamento[3]}")
    escolha = int(input())
    if  escolha == 0:
         print("voce escolheu",pagamento[0])
         carrinho.append(pagamento[0])
         
    elif escolha == 1:
         print("voce escolheu",pagamento[1])
         carrinho.append(pagamento[1])
    elif   escolha == 2:
         print("voce escolheu",pagamento[2])
         carrinho.append(pagamento[2])
    else :
         print("voce escolheu",pagamento[3])
         carrinho.append(pagamento[3])

    #encerrar = input()
    break



print("\n=============RECIBO=============")
print(f"tempo de permanencia:{calculateTime()} horas")
print(f"valor total:{valorTotal}")
print(f"forma de pagamento selecionada:{carrinho}")



