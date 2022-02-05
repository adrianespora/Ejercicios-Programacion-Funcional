'''Ejercicio 8
Escribir una función reciba un diccionario con las asignaturas y
las notas de un alumno y devuelva otro diccionario con las asignaturas
en mayúsculas y las calificaciones correspondientes a las notas aprobadas.'''

def calificaciones(notas):
    Calificaciones = {} # Genero un nuevo diccionario para las mayusculas
    calificacion = []
    calificacion_aprobados = []
    for i in notas.values():
        if i >= 5 and i < 7:
            calificacion_aprobados.append("Aprobado")
        elif i < 9:
            calificacion_aprobados.append("Muy bien")
        elif i == 10:
            calificacion_aprobados.append("Excelente")
    j = 0
    for i in notas.keys(): # Recorro las claves del diccionario

        ''' Asigno esa clave en mayuscula al diccionario y 
        le doy el valor correspondiente'''
        if notas[i] >= 5:
            Calificaciones[i.upper()] = calificacion_aprobados[j]
            j +=1

    print(Calificaciones)
calificaciones({"matematicas":5, "lengua":8, "historia":6, "tecnologia":10})