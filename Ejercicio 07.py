'''
Ejercicio 7
Escribir una función reciba un diccionario con las asignaturas
y las notas de un alumno y devuelva otro diccionario con las asignaturas
 en mayúsculas y las calificaciones correspondientes a las notas.
'''
def calificaciones(notas):
    Calificaciones = {} # Genero un nuevo diccionario para las mayusculas
    calificacion = []
    for i in notas.values():
        if i < 5:
            calificacion.append("Desaprobado")
        elif i < 7:
            calificacion.append("Aprobado")
        elif i < 9:
            calificacion.append("Muy bien")
        else:
            calificacion.append("Excelente")
    j = 0
    for i in notas.keys(): # Recorro las claves del diccionario

        ''' Asigno esa clave en mayuscula al diccionario y 
        le doy el valor correspondiente'''

        Calificaciones[i.upper()] = calificacion[j]
        j += 1

    print(Calificaciones)
calificaciones({"matematicas":3, "lengua":8, "historia":6})