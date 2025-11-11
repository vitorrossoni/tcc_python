import datetime
import random



print("ola,seja bem vindo ao sistema de estacionamento do shopping\n" \
"tabela de preços:1 hora = R$10,00, menos de uma hora = R$00,00")

entrada:datetime
saida:datetime
tempo = saida - entrada
tarifa = 10
pagamento = ["pix","debito","credito","dinheiro"]
carrinho = []
sair = False
encerrar = ""





if tempo <= 1:
    valor = tarifa
else:
    valor = tempo * tarifa


my_datetime = datetime(2025, random.randint(1,12),random.randint(1,28), random.randint(0,24),random.randint(0,59), 0)
print("Tempo estacionado:", tempo, "hora(s)")
print("Valor a pagar: R$", round(valor, 2))








while sair == False:
    print(pagamento)
    print (f"escolha uma forma de pgaento:\n\pix [0],debito [1],credito [2],dinheiro[3]\n{pagamento[0]}\n{pagamento[1]}\n{pagamento[2]}\n{pagamento[3]}")
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

    encerrar = input()



print("\n\n\n\n\n\n\n==========recibo==========\n tempo de permanencia", tempo)
print(" valor total de:", valor)
print(" forma de pagamento",carrinho )
