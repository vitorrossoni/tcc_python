print("ola,seja bem vindo ao sistema de estacionamento do shopping\n" \
"tabela de preços:1 hora = R$5,00, menos de uma hora = R$00,00")

entrada = float(input("Digite o horário de entrada (ex: 8.5 para 8h30): "))
saida = float(input("Digite o horário de saída (ex: 10.0 para 10h00): "))
tempo = saida - entrada
tarifa = 10

if tempo <= 1:
    valor = tarifa
else:
    valor = tempo * tarifa

print("Tempo estacionado:", tempo, "hora(s)")
print("Valor a pagar: R$", round(valor, 2))

pagamento = (input("digite a forma de pagamento(ex:credidito, debito, pix): "))









print("==========recibo==========\n tempo de permanencia", tempo)
print(" valor total de:", valor)
print(" forma de pagamento", pagamento)