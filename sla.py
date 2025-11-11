print ("ola,seja bem vindo ao circo!\n" \
"lista de preços:entrada inteira R$30, meia entrada R$15")

produto = ["meia", "inteira"]
carrinho = []
sair = False
encerrar = ""




while sair == False:
    print (f"oque voce gostaria de comprar?\n\meia entrada [0],entrada inteira [1]\n{produto[0]}\n{produto[1]}")
    escolha = int(input())
    if  escolha == 0:
         print("voce escolheu",produto[0])
         carrinho.append(produto[0])
    if  escolha == 1:
         print("voce escolheu",produto[1])
         carrinho.append(produto[1])
         encerrar = input()
    print("voce deseja sair? S/N")
    encerrar = input()
    if encerrar == "S":
           sair = True 
    else:
               continue
print(carrinho)