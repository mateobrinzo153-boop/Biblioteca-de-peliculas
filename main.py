import biblioteca

opcion = ""
while opcion!= "4":
    print(""" 
    Biblioteca de peliculas:
    1. Agregar pelicula
    2. Ver lista de peliculas
    3. Eliminar gasto
    4. Salir
    """)
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        biblioteca.agregar_pelicula()
    elif opcion == 2:
        biblioteca.ver_peliculas()
    elif opcion == 3:
        biblioteca.eliminar_pelicula()
    elif opcion == 4:
        pass
    else:
        print("Opcion invalida.")
print("¡Hasta luego!")