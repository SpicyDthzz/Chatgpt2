import os
os.system ("cls")

estudiantes = []
while True:
    print("Bienvenido al sistema de registro de la universidad")
    nombre = input("Ingrese el nombre del estudiante: ")
    try:
        rut = int(input("Ingrese el RUT del estudiante (sin puntos ni guion): "))
    except ValueError:
        print("El RUT debe ser un número entero.")
        continue
    direccion = input("Ingrese la dirección donde vive el estudiante: ")
    try:
        fecha_nacimiento = input("Ingrese la fecha de nacimiento (dd-mm-aaaa): ")
        dia, mes, año = fecha_nacimiento.split('-')
        dia = int(dia)
        mes = int(mes)
        año = int(año)
    except ValueError:
        print("La fecha de nacimiento debe estar en formato dd-mm-aaaa.")
        continue
    estudiante = [nombre, rut, direccion, fecha_nacimiento]
    estudiantes.append(estudiante)
    print("Estudiante registrado con éxito!")
    
    continuar = input("¿Desea registrar otro estudiante? (si/no): ")
    if continuar.lower() == 'no':
        break

print("Lista de estudiantes registrados:")
for e in estudiantes:
    print("Nombre:", e[0], "- RUT:", e[1], "- Dirección:", e[2], "- Fecha de Nacimiento:", e[3])
