import json
import os
from typing import Dict, List, Union


def read_json(path: str) -> Union[Dict, List]:
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []  
    except json.JSONDecodeError:
        return []  
    except Exception as e:
        raise RuntimeError(f"Error al leer el archivo: {e}")


def write_json(path: str, data: Union[Dict, List]) -> None:
    try:
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        raise RuntimeError(f"Error al escribir en el archivo: {e}")


def initialize_json(path: str) -> None:
    if not os.path.exists(path):
        initial_structure = [
            {
                "coleccion_id": "media-001",
                "nombre": "Mi Colección",
                "libros": [],
                "peliculas": [],
                "musica": []
            }
        ]
        write_json(path, initial_structure)  


def clone_json(path: str) -> Union[Dict, List]:
    try:
        return read_json(path) 
    except Exception as e:
        raise RuntimeError(f"Error al clonar el archivo: {e}")
