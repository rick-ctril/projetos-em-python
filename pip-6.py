#Esse programa ler um ÂNGULO qualquer e mostra na tela o valor de SENO, COSSENO E TANGENTE.
#Um jeito de fazer.
from math import radians, sin, cos, tan
an = float(input('Digite um angulo: '))
seno = sin(math.radians(an))
cosseno = cos(math.radians(an))
tangente = tan(math.radians(an))
print ('O ângulo de {} tem o seno de {:.2f} o cosseno de {:.2f} e a tangente de {:.2f}.' .format(an, seno, cosseno))


#Outro jeito de fazer e mais organizado.
import math
ângulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(ângulo))
print ('O ângulo de {} tem o seno {:.2f}' .format(ângulo, seno))
cosseno = math.cos(math.radians(ângulo))
print ('O ângulo de {} tme o cosseno {:.2f}' .format(ângulo, cosseno))
tangente = math.tan(math.radians(ângulo))
print ('O ângulo de {} tem a tangente {:.2f}' .format(ângulo, tangente))





#SIGA MEU INSTAGRAM @geecko___