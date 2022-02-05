'''Ejercicio 6
Escribir una función reciba una lista de notas y devuelva la lista de
calificaciones correspondientes a esas notas.

'''

def calificaciones(notas):
    calificaciones = []
    for i in notas:
        if i < 5:
            calificaciones.append("Desaprobado")
        elif i < 7:
            calificaciones.append("Aprobado")
        elif i < 9:
            calificaciones.append("Muy bien")
        else:
            calificaciones.append("Excelente")
    print(calificaciones)

calificaciones([7,4,5,2,10,8,3])