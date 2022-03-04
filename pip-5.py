'''Programa que ler o comprimento do cateto oposto e do cateto adjacente de 
um triângulo e mostra o valor da hipotenusa.'''
#Metodo matematico sem importação de medir o valor da hipotenusa.
co = float(input('Complimento do cateto: '))
ca = float(input('Complimento do cateto adiacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print ('A hipotenusa vai medir {:.2f}' .format(hi))


#Metodo com importação 
import math
co = float(input('Complimento do cateto: '))
ca = float(input('Complimento do cateto adiacente: '))
hi = math.hypot(co, ca)
print ('A hipotenusa vai medir {:.2f}' .format(hi))




# SIGA MEU INSTAGRAM @geecko___