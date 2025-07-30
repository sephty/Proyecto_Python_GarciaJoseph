from tabulate import tabulate
from app import menu
from utils.screenController import limpiar_pantalla, pausar_pantalla


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
            pass
        case 2:
            pass
        case 3:
            pass
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
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            return menu()
        case _:
            print("Opción no válida. Intenta de nuevo.")
            pausar_pantalla()
            return opcion_2()


def opcion_3():
    limpiar_pantalla()
    print("=" * 43)
    print("        Buscar un Elemento")
    print("=" * 43)

    opciones = [
        [1, "Buscar por Título"],
        [2, "Buscar por Autor/Director/Artista"],
        [3, "Buscar por Género"],
        [4, "Regresar al Menú Principal"]
    ]
    print(tabulate(opciones, tablefmt="plain"))
    print("=" * 43)

    try:
        opcion = int(input("Selecciona una opción (1-4): "))
    except ValueError:
        print("Por favor, ingresa un número válido.")
        pausar_pantalla()
        return opcion_3()

    match opcion:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            return menu()
        case _:
            print("Opción no válida. Intenta de nuevo.")
            pausar_pantalla()
            return opcion_3()


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
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
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
            pass
        case 2:
            pass
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
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            return menu()
        case _:
            print("Opción no válida. Intenta de nuevo.")
            pausar_pantalla()
            return opcion_6()


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
            pass
        case 2:
            pass
        case 3:
            return menu()
        case _:
            print("Opción no válida. Intenta de nuevo.")
            pausar_pantalla()
            return opcion_7()


