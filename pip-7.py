#Programa de seleção sortido usando lista
from random import choice
aluno1 = str(input('Primeiro aluno: '))
aluno2 = str(input('Segundo aluno: '))
aluno3 = str(input('Terceiro aluno: '))
aluno4 = str(input('Quarto aluno: '))
aluno5 = str(input('Quinto aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4, aluno5]
escolhido = choice(lista)
print ('O aluno escolhido {}!' .format(escolhido))
