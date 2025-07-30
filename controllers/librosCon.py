import json
import os
import random


def generate_random_id(prefix: str = "") -> str:
    return f"{prefix}-{random.randint(1000, 9999)}"


def check_unique_id(path: str, category: str, new_id: str) -> bool:
    collection = read_json(path)
    if collection:   
        for element in collection[0][category]:
            if element["id"] == new_id:
                return False  
    return True


def read_json(path: str):
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: El archivo '{path}' no se encuentra.")
    except json.JSONDecodeError:
        print(f"Error: El archivo '{path}' no tiene un formato válido.")
    except Exception as e:
        print(f"Error inesperado al leer el archivo '{path}': {e}")
    return [] 


def write_json(path: str, data):
    try:
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error al guardar los datos en el archivo '{path}': {e}")


def initialize_json(path: str) -> None:
    if not os.path.exists(path):  
        initial_structure = [
            {
                "coleccion_id": generate_random_id("media"),  
                "libros": [],
                "peliculas": [],
                "musica": []
            }
        ]
        write_json(path, initial_structure)  
        print(f"Archivo creado: {path}")
    else:
        print("El archivo ya existe, no se modificó.")

def clone_json(path):
    try:
        return read_json(path)  
    except Exception as e:
        print(f"Error al clonar el archivo: {e}")
        return [] 


def add_element(path, category: str, element):
    collection = read_json(path) 
    if collection:
        if category in collection[0]:  
            element_id = generate_random_id(category[:4])  
            
            while not check_unique_id(path, category, element_id):
                element_id = generate_random_id(category[:4]) 

            element["id"] = element_id  
            collection[0][category].append(element)  
            write_json(path, collection) 
            print(f"Elemento añadido correctamente a {category}.")
        else:
            print(f"Categoría '{category}' no encontrada en la colección.")
    else:
        print("La colección está vacía o no existe.")


def delete_element(path, category: str, element_id: str):
    collection = read_json(path) 
    if collection:
        if category in collection[0]:
            elements = collection[0][category]
            updated_elements = [element for element in elements if element["id"] != element_id]
            
            if len(updated_elements) != len(elements): 
                collection[0][category] = updated_elements
                write_json(path, collection) 
                print(f"Elemento con ID '{element_id}' eliminado de {category}.")
            else:
                print(f"Elemento con ID '{element_id}' no encontrado en {category}.")
        else:
            print(f"Categoría '{category}' no encontrada en la colección.")
    else:
        print("La colección está vacía o no existe.")


def search_element(path, category: str, title: str):
    collection = read_json(path)  
    if collection:
        if category in collection[0]:
            elements = collection[0][category]
            found_elements = [element for element in elements if title.lower() in element["titulo"].lower()]
            return found_elements
        else:
            print(f"Categoría '{category}' no encontrada en la colección.")
            return []
    else:
        print("La colección está vacía o no existe.")
        return []


def view_all_elements(path, category: str):
    collection = read_json(path)  
    if collection:
        if category in collection[0]:
            elements = collection[0][category]
            if elements:
                print(f"Elementos en la categoría {category}:")
                for i, element in enumerate(elements, start=1):
                    print(f"{i}. Título: {element.get('titulo')}, Autor/Director: {element.get('autor')}, Género: {element.get('genero')}")
            else:
                print(f"No hay elementos en la categoría {category}.")
        else:
            print(f"Categoría '{category}' no encontrada en la colección.")
    else:
        print("La colección está vacía o no existe.")
