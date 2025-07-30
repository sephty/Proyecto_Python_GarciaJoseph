from utils.corefiles import read_json, write_json
from utils.validateData import validate_data
from utils.screenController import pausar_pantalla

def add_new_libro():
    print("\nAñadir nuevo Libro: ")

    new_libro = {
        "titulo": input("Título: "),
        "autor": input("Autor: "),
        "genero": input("Género: "),
        "valoracion": int(input("Valoración (1-5): "))
    }

    if validate_data("libros", new_libro):
        add_element_to_collection("libros", new_libro)
    else:
        print("Los datos del libro no son válidos.")
        pausar_pantalla()

def add_element_to_collection(category: str, element: dict):
    path = "data/coleccion.json"
    data = read_json(path)

    if category == "libros":
        data[0]["libros"].append(element)
    elif category == "peliculas":
        data[0]["peliculas"].append(element)
    elif category == "musica":
        data[0]["musica"].append(element)

    write_json(path, data)
    print(f"{category[:-1].capitalize()} añadido correctamente.")
    pausar_pantalla()


 # hope this wqorks