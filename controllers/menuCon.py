from tabulate import tabulate
from utils.screenController import limpiar_pantalla, pausar_pantalla 
from app import menu, arrancar_programa
import controllers.coleccionMan as colMan
import controllers.editar as edit
import controllers.anadir as add
import controllers.listar as search
import controllers.eliminar as delete
from utils.temporal_data import elementos_temporales


def opcion_1():
    limpiar_pantalla()
    print("=" * 43)
    print("        Añadir un Nuevo Elemento")
    print("=" * 43)

    opciones = [
        [1, "Libro"],
        [2, "Película"],
        [3, "Música"],
        [4, "Regresar al Menú Principal"]
    ]
    print(tabulate(opciones, tablefmt="plain"))
    print("=" * 43)

    try:
        opcion = int(input("Selecciona una opción (1-4): "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        pausar_pantalla()
        return opcion_1()

    match opcion:
        case 1:
            add.add_libro()
        case 2:
            add.add_pelicula()
        case 3:
            add.add_musica()
        case 4:
            return menu()
        case _:
            print("Opción no válida. Intenta de nuevo.")
            pausar_pantalla()
            return opcion_1()


def opcion_2():
    limpiar_pantalla()
    print("=" * 43)
    print("        Ver Todos los Elementos")
    print("=" * 43)

    opciones = [
        [1, "Ver Todos los Libros"],
        [2, "Ver Todas las Películas"],
        [3, "Ver Toda la Música"],
        [4, "Regresar al Menú Principal"]
    ]
    print(tabulate(opciones, tablefmt="plain"))
    print("=" * 43)

    try:
        opcion = int(input("Selecciona una opción (1-4): "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        pausar_pantalla()
        return opcion_2()

    match opcion:
        case 1:
            if "libros" in elementos_temporales and elementos_temporales["libros"]:
                headers = ["Título", "Autor", "Género", "Valoración"]
                books = [[libro['titulo'], libro['autor'], libro['genero'], libro['valoracion']] for libro in elementos_temporales["libros"]]
                print(tabulate(books, headers=headers, tablefmt="pretty"))
            else:
                print("No hay libros para mostrar.")
            pausar_pantalla()
            return opcion_2()
        case 2:
            if "peliculas" in elementos_temporales and elementos_temporales["peliculas"]:
                headers = ["Título", "Director", "Género", "Año", "Valoración"]
                peliculas = [[pelicula['titulo'], pelicula['director'], pelicula['genero'], pelicula['anio'], pelicula['valoracion']] for pelicula in elementos_temporales["peliculas"]]
                print(tabulate(peliculas, headers=headers, tablefmt="pretty"))
            else:
                print("No hay películas para mostrar.")
            pausar_pantalla()
            return opcion_2()
        case 3:
            if "musica" in elementos_temporales and elementos_temporales["musica"]:
                headers = ["Título", "Artista", "Género", "Año", "Valoración"]
                musica = [[musica['titulo'], musica['artista'], musica['genero'], musica['anio'], musica['valoracion']] for musica in elementos_temporales["musica"]]
                print(tabulate(musica, headers=headers, tablefmt="pretty"))
            else:
                print("No hay música para mostrar.")
            pausar_pantalla()
            return opcion_2()
        case 4:
            return menu()
        case _:
            print("Opción no válida")
            pausar_pantalla()
            return opcion_2()

def opcion_4():
    limpiar_pantalla()
    print("=" * 43)
    print("        Editar un Elemento")
    print("=" * 43)

    opciones = [
        [1, "Editar Título"],
        [2, "Editar Autor/Director/Artista"],
        [3, "Editar Género"],
        [4, "Editar Valoración"],
        [5, "Regresar al Menú Principal"]
    ]
    print(tabulate(opciones, tablefmt="plain"))
    print("=" * 43)

    try:
        opcion = int(input("Selecciona una opción (1-5): "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        pausar_pantalla()
        return opcion_4()

    match opcion:
        case 1:
            tipo = input("¿Qué tipo de elemento deseas editar? (libros/peliculas/musica): ")
            if tipo in ["libros", "peliculas", "musica"]:
                edit.editar_elemento(tipo, "titulo")
            else:
                print("Categoría no válida.")
                pausar_pantalla()
                return opcion_4()
        case 2:
            tipo = input("¿Qué tipo de elemento deseas editar? (libros/peliculas/musica): ")
            if tipo in ["libros", "peliculas", "musica"]:
                edit.editar_elemento(tipo, "autor" if tipo == "libros" else "director" if tipo == "peliculas" else "artista")
            else:
                print("Categoría no válida.")
                pausar_pantalla()
                return opcion_4()
        case 3:
            tipo = input("¿Qué tipo de elemento deseas editar? (libros/peliculas/musica): ")
            if tipo in ["libros", "peliculas", "musica"]:
                edit.editar_elemento(tipo, "genero")
            else:
                print("Categoría no válida.")
                pausar_pantalla()
                return opcion_4()
        case 4:
            tipo = input("¿Qué tipo de elemento deseas editar? (libros/peliculas/musica): ")
            if tipo in ["libros", "peliculas", "musica"]:
                edit.editar_elemento(tipo, "valoracion")
            else:
                print("Categoría no válida.")
                pausar_pantalla()
                return opcion_4()
        case 5:
            return menu()
        case _:
            print("Opción no válida")
            pausar_pantalla()
            return opcion_4()


def opcion_5():
    limpiar_pantalla()
    print("=" * 43)
    print("        Eliminar un Elemento")
    print("=" * 43)

    opciones = [
        [1, "Eliminar por Título"],
        [2, "Eliminar por Identificador Único"],
        [3, "Regresar al Menú Principal"]
    ]
    print(tabulate(opciones, tablefmt="plain"))
    print("=" * 43)

    try:
        opcion = int(input("Selecciona una opción (1-3): "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        pausar_pantalla()
        return opcion_5()

    match opcion:
        case 1:
            delete.eliminar_por_titulo()
            return opcion_5()
        case 2:
            delete.eliminar_por_id()
            return opcion_5()
        case 3:
            return menu()
        case _:
            print("Opción no válida. Intenta de nuevo.")
            pausar_pantalla()
            return opcion_5()


def opcion_6():
    limpiar_pantalla()
    print("=" * 43)
    print("        Ver Elementos por Categoría")
    print("=" * 43)

    opciones = [
        [1, "Ver Libros"],
        [2, "Ver Películas"],
        [3, "Ver Música"],
        [4, "Regresar al Menú Principal"]
    ]
    print(tabulate(opciones, tablefmt="plain"))
    print("=" * 43)
    try:
        opcion = int(input("Selecciona una opción (1-4): "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        pausar_pantalla()
        return opcion_6()
    match opcion:
        case 1:
            if "libros" in elementos_temporales and elementos_temporales["libros"]:
                headers = ["Título", "Autor", "Género", "Valoración"]
                books = [[libro['titulo'], libro['autor'], libro['genero'], libro['valoracion']] for libro in elementos_temporales["libros"]]
                print(tabulate(books, headers=headers, tablefmt="pretty"))
            else:
                print("No hay libros para mostrar.")
            pausar_pantalla()
            return opcion_6()
        case 2:
            if "peliculas" in elementos_temporales and elementos_temporales["peliculas"]:
                headers = ["Título", "Director", "Género", "Año", "Valoración"]
                peliculas = [[pelicula['titulo'], pelicula['director'], pelicula['genero'], pelicula['anio'], pelicula['valoracion']] for pelicula in elementos_temporales["peliculas"]]
                print(tabulate(peliculas, headers=headers, tablefmt="pretty"))
            else:
                print("No hay películas para mostrar.")
            pausar_pantalla()
            return opcion_6()
        case 3:

            if "musica" in elementos_temporales and elementos_temporales["musica"]:
                headers = ["Título", "Artista", "Género", "Año", "Valoración"]
                musica = [[musica['titulo'], musica['artista'], musica['genero'], musica['anio'], musica['valoracion']] for musica in elementos_temporales["musica"]]
                print(tabulate(musica, headers=headers, tablefmt="pretty"))
            else:
                print("No hay música para mostrar.")
            pausar_pantalla()
            return opcion_6()
        case 4:
            return menu()


def opcion_7():
    limpiar_pantalla()
    print("=" * 43)
    print("        Guardar y Cargar Colección")
    print("=" * 43)

    opciones = [
        [1, "Guardar la Colección Actual"],
        [2, "Cargar una Colección Guardada"],
        [3, "Regresar al Menú Principal"]
    ]
    print(tabulate(opciones, tablefmt="plain"))
    print("=" * 43)

    try:
        opcion = int(input("Selecciona una opción (1-3): "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        pausar_pantalla()
        return opcion_7()

    match opcion:
        case 1:
            colMan.guardar_coleccion_actual()
            pausar_pantalla()
        case 2:
            colMan.cargar_coleccion_por_id()
        case 3:
            return menu()
        case _:
            print("Opción no válida. Intenta de nuevo.")
            pausar_pantalla()
            return opcion_7()


