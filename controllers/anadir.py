from utils.corefiles import write_json, read_json
from utils.validateData import validate_data
from utils.screenController import pausar_pantalla
from utils.temporal_data import elementos_temporales
import controllers.menuCon as menu
import utils.id_gen as id_gen
 # add
def add_libro():
    print("=" * 43)
    print("      Añadir un Nuevo Libro")
    print("=" * 43)

    # Gather book details
    titulo = input("Título: ")
    autor = input("Autor: ")
    genero = input("Género: ")
    
    while True:
        try:
            valoracion = int(input("Valoración (1-5): "))
            if 1 <= valoracion <= 5:
                break
            else:
                print("La valoración debe estar entre 1 y 5.")
        except ValueError:
            print("Valor inválido. Por favor, ingresa un número entre 1 y 5.")

    libro = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "valoracion": valoracion
    }

    if validate_data("libros", libro):
        # Add to the temporary list
        if "libros" not in elementos_temporales:
            elementos_temporales["libros"] = []
        libro["id"] = id_gen.generar_id_media("libro", "data/libros.json")
        elementos_temporales["libros"].append(libro)

    pausar_pantalla()
    return menu.opcion_1()

def add_pelicula():
    print("=" * 43)
    print("      Añadir una Nueva Película")
    print("=" * 43)

    # Gather movie details
    titulo = input("Título: ")
    director = input("Director: ")
    genero = input("Género: ")
    
    while True:
        try:
            valoracion = int(input("Valoración (1-5): "))
            if 1 <= valoracion <= 5:
                break
            else:
                print("La valoración debe estar entre 1 y 5.")
        except ValueError:
            print("Valor inválido. Por favor, ingresa un número entre 1 y 5.")
    
    while True:
        try:
            anio = int(input("Año de la película: "))
            if 1900 <= anio <= 2100:
                break
            else:
                print("Año inválido. Debe ser entre 1900 y 2100.")
        except ValueError:
            print("Valor inválido. Por favor, ingresa un número válido para el año.")

    pelicula = {
        "titulo": titulo,
        "director": director,
        "genero": genero,
        "valoracion": valoracion,
        "anio": anio
    }

    if validate_data("peliculas", pelicula):
        # Add to the temporary list
        if "peliculas" not in elementos_temporales:
            elementos_temporales["peliculas"] = []
        pelicula["id"] = id_gen.generar_id_media("pelicula", "data/peliculas.json")
        elementos_temporales["peliculas"].append(pelicula)

    pausar_pantalla()
    return menu.opcion_1()


def add_musica():
    print("=" * 43)
    print("      Añadir una Nueva Música")
    print("=" * 43)

    # Gather music details
    titulo = input("Título: ")
    artista = input("Artista: ")
    genero = input("Género: ")
    
    while True:
        try:
            valoracion = int(input("Valoración (1-5): "))
            if 1 <= valoracion <= 5:
                break
            else:
                print("La valoración debe estar entre 1 y 5.")
        except ValueError:
            print("Valor inválido. Por favor, ingresa un número entre 1 y 5.")
    
    while True:
        try:
            anio = int(input("Año de la música: "))
            if 1900 <= anio <= 2100:
                break
            else:
                print("❌ Año inválido. Debe ser entre 1900 y 2100.")
        except ValueError:
            print("Valor inválido. Por favor, ingresa un número válido para el año.")

    musica = {
        "titulo": titulo,
        "artista": artista,
        "genero": genero,
        "valoracion": valoracion,
        "anio": anio
    }

    if validate_data("musica", musica):
        # Add to the temporary list
        if "musica" not in elementos_temporales:
            elementos_temporales["musica"] = []
        musica["id"] = id_gen.generar_id_media("musica", "data/musica.json")
        elementos_temporales["musica"].append(musica)

    pausar_pantalla()
    return menu.opcion_1()

