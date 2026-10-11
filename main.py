import biblioteca

opcion = int
while opcion!= "5":
    print(""" 
    Biblioteca de peliculas:
    1. Agregar pelicula
    2. Ver lista de peliculas
    3. Marcar pelicula como vista
    4. Eliminar pelicula
    5. Salir
    """)
    opcion = input("Seleccione una opción: ")
    if opcion == 1:
        biblioteca.agregar_pelicula()
    elif opcion == 2:
        biblioteca.ver_peliculas()
    elif opcion == 3:
        biblioteca.marcar_como_vista()
    elif opcion == 4:
        biblioteca.eliminar_pelicula()
    elif opcion == 5:
        break
    else:
        print("Opcion invalida.")
print("¡Hasta luego!")