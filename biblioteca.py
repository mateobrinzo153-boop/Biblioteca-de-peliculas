import json

peliculas = []

def agregar_pelicula():
    nombre = input("Inserte el nombre de la pelicula: ").strip().lower()
    categoria = input("Inserte la categoria: ").strip().lower()
    

    if not (nombre.strip() or categoria.strip() or director.strip()):
        print("Campo obligatorio.")
        return
    while True:
        try:
            puntuacion = int(input("Inserte la puntuacion(1-10): "))
            año = int(input("Inserte el año de estreno(hasta 2026): "))
            if 1 <= puntuacion <= 10 and año <= 2026:
                break
            else:
                print("Inserte un numero valido.")
                return
            
        except ValueError:
            print("Inserte un numero valido.")
            return
    
    director = input("Inserte el nombre del director: ").strip().lower().capitalize()

    pelicula = {
        "nombre": nombre,
        "categoria": categoria,
        "puntuación": puntuacion,
        "año": año,
        "director": director
    }

    peliculas.append(pelicula)

def ver_peliculas():
    for pelicula in peliculas:
        print(f"{pelicula["nombre"]} - {pelicula["categoria"]} - {pelicula["puntuación"]} - {pelicula["año"]} - {pelicula["director"]}")
    if not peliculas:
        print("No se registraron peliculas.")

def eliminar_pelicula():
    nombre = input("Inserte nombre de la pelicula a eliminar: ")
    encontrado = False
    for pelicula in peliculas:
        if pelicula["nombre"].strip().lower() == nombre.strip().lower():
            respuesta = input(f"Esta seguro de que quiere eliminar {nombre} de la biblioteca?(s/n)")
            while respuesta not in ["s", "n"]:
                print("Respuesta no valida. Ingrese 's' para sí o 'n' para no.")
                respuesta = input().strip().lower()
            if respuesta == "s":
                peliculas.remove(pelicula)
                print("Producto eliminado")
            elif respuesta == "n":
                print("Eliminacion cancelada.")
                return
            encontrado = True
            break

    if not encontrado:
        print("Producto no encontrado")
            