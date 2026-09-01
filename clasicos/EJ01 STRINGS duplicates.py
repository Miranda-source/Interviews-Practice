""" Remove Duplicates

Input:  [1, 2, 4, 5, 6]
Output: 3

"""

oracion = "Python dice hola mundo"

separar = oracion.split()
solopalabras = []

for letra in separar:
    if letra not in solopalabras:
        solopalabras.append(letra)

resultado = " ".join(solopalabras)

print(resultado)

