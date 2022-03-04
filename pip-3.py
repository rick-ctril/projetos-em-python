#Programa para calcular quanto pagar por alugel de carros.
#Variavel para saber quantos dias passou com o carro.
dias = int(input('Quantos dias alugados: '))
#Variavel para saber quantos km o carro rodou.
km = float(input('Quantos KMs foram percoridos: '))
#Variavel pago vai atribuir o valor do calculo dias e kms.
pago = (dias * 60) + (km * 0.15)
#Escreve na tela quanto é o valor a ser pago.
print ('O total a pagar é de R${:.2f}' .format(pago))




#SIGA MEU INSTAGRAM @geecko___