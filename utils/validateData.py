# utils/validateData.py
from typing import Dict, List

def validate_libro(book: dict) -> bool:
    required_fields = ["titulo", "autor", "genero", "valoracion"]

    for field in required_fields:
        if field not in book or not book[field]:
            print(f"Error: El campo '{field}' es obligatorio en libros.")
            return False

    if not isinstance(book["valoracion"], int) or not (1 <= book["valoracion"] <= 5):
        print("Error: La valoración debe ser un número entre 1 y 5.")
        return False
    
    return True


def validate_pelicula(movie: dict) -> bool:
    required_fields = ["titulo", "director", "genero", "anio"]

    for field in required_fields:
        if field not in movie or not movie[field]:
            print(f"Error: El campo '{field}' es obligatorio en películas.")
            return False

    if not isinstance(movie["anio"], int) or not (1900 <= movie["anio"] <= 2100):
        print("Error: El año de la película debe ser un número válido entre 1900 y 2100.")
        return False

    return True


def validate_musica(music: dict) -> bool:
    required_fields = ["titulo", "artista", "genero", "anio"]

    for field in required_fields:
        if field not in music or not music[field]:
            print(f"Error: El campo '{field}' es obligatorio en música.")
            return False

    if not isinstance(music["anio"], int) or not (1900 <= music["anio"] <= 2100):
        print("Error: El año de la música debe ser un número válido entre 1900 y 2100.")
        return False

    return True


def validate_data(category: str, element: dict) -> bool:
    if category == "libros":
        return validate_libro(element)
    elif category == "peliculas":
        return validate_pelicula(element)
    elif category == "musica":
        return validate_musica(element)
    else:
        print("Error: Categoría no válida.")
        return False
