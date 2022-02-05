'''Ejercicio 5
Escribir una función que reciba una frase y devuelva
un diccionario con las palabras que contiene y su longitud.
'''
def cantidadletras(frase):
    listadepalabras = frase.split() ## Guarda en la lista las palabras de la cadena
    letras = map(len,listadepalabras) ## map aplica la funcion len (en este caso) a cada valor de la lista
## devuelve un diccionario con la lista y la cantidad de letras
    return dict(zip(listadepalabras,letras))
print(cantidadletras("La casa esta en orden"))
