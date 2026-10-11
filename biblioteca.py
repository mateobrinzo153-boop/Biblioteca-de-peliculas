import json

peliculas = []


def agregar_pelicula():
    nombre = input("Inserte el nombre de la pelicula: ").strip().lower()
    categoria = input("Inserte la categoria: ").strip().lower()
    vista = False

    
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
    if not nombre.strip() or not categoria.strip() or not director.strip():
        print("Campo obligatorio.")
        return
    pelicula = {
        "nombre": nombre,
        "categoria": categoria,
        "vista": vista,
        "puntuación": puntuacion,
        "año": año,
        "director": director
        
    }

    peliculas.append(pelicula)
    guardar_peliculas()

def ver_peliculas():
    for pelicula in peliculas:
        vista_var = "vista" if pelicula["vista"] else "no vista"
        print(f"{pelicula["nombre"]} - {pelicula["categoria"]} - {vista_var} - {pelicula["puntuación"]} - {pelicula["año"]} - {pelicula["director"]}")
    if not peliculas:
        print("No se registraron peliculas.")

def marcar_como_vista():
    encontrada = False
    nombre = input("Inserte nombre de la pelicula: ")
    for pelicula in peliculas:
        if pelicula["nombre"].strip().lower() == nombre.strip().lower():
            encontrada = True
            pelicula["vista"] = True
            guardar_peliculas()
            print("Pelicula marcada como vista.")
    if not encontrada:
        print(f"La pelicula '{nombre}' no se encuentra en la biblioteca")
        return

def eliminar_pelicula():
    nombre = input("Inserte nombre de la pelicula: ")
    encontrada = False
    for pelicula in peliculas:
        if pelicula["nombre"].strip().lower() == nombre.strip().lower():
            respuesta = input(f"Esta seguro de que quiere eliminar {nombre} de la biblioteca?(s/n)")
            while respuesta not in ["s", "n"]:
                print("Respuesta no valida. Ingrese 's' para sí o 'n' para no.")
                respuesta = input().strip().lower()
            if respuesta == "s":
                peliculas.remove(pelicula)
                guardar_peliculas()
                print("Pelicula eliminado")
            elif respuesta == "n":
                print("Eliminacion cancelada.")
                return
            encontrada = True
            break

    if not encontrada:
        print(f"La pelicula '{nombre}' no se encuentra en la biblioteca")
        return

def guardar_peliculas():
    with open('biblioteca.json', 'w') as archivo:
        json.dump(peliculas, archivo, indent=4)

try:
    with open("biblioteca.json", "r", encoding="utf-8") as archivo:
        peliculas = json.load(archivo)

    for pelicula in peliculas:
        if not all(dato in pelicula for dato in [
            "nombre", "categoria", "vista",
            "puntuación", "año", "director"
        ]):
            raise ValueError

except FileNotFoundError:
    peliculas = []

except (json.JSONDecodeError, ValueError):
    print("Error: faltan datos o el archivo JSON es inválido.")
    peliculas = []