""" Remove Duplicates

Instructions: Given a sentence, write a program that removes repeated words while keeping the original order of the words.
The program should return a new sentence containing only the first occurrence of each word.

Example:

Input:
"python is easy and python is powerful"

Output:
"python is easy and powerful


"""

oracion = "Python dice hola mundo"

separar = oracion.split()
solopalabras = []

for letra in separar:
    if letra not in solopalabras:
        solopalabras.append(letra)

resultado = " ".join(solopalabras)

print(resultado)

