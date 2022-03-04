#Programa para sortiar de forma rondomica a ordem de nomes da lista.
#Biblioteca usada.
from random import shuffle
#Digite cinco nomes para a lista.
n1 = str(input('Digite um nome: ')) 
n2 = str(input('Digite um nome: '))
n3 = str(input('Digite um nome: '))
n4 = str(input('Digite um nome: '))
n5 = str(input('Digite um nome: '))
#Lista com cinco nomes que foram digitados.
lista = [n1, n2, n3, n4, n5]
#Função que enbarralha os nomes de forma rondomica.
shuffle(lista)
#Escreve na tela os nomes em uma sequencia rondomica.
print ('A ordem da apresentção é {}.' .format(lista))
