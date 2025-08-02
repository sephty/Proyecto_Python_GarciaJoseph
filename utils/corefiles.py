import json
import os
from typing import Dict, List, Union

def read_json(path: str) -> Union[Dict, List]:
    try:
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []  
    except Exception as e:
        raise RuntimeError(f"Error al leer el archivo: {e}")

def write_json(path: str, data: Union[Dict, List]) -> None:
    try:
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    except Exception as e:
        raise RuntimeError(f"Error al escribir en el archivo: {e}")

def initialize_json(path: str) -> None:
    if not os.path.exists(path):
        initial_structure = []  
        write_json(path, initial_structure)  

def clone_json(path: str) -> Union[Dict, List]:
    try:
        return read_json(path) 
    except Exception as e:
        raise RuntimeError(f"Error al clonar el archivo: {e}")

def initialize_coleccion(path: str = 'data/coleccion.json') -> None:
    if not os.path.exists(path):
        from utils.id_gen import generar_id_coleccion
        coleccion = [{
            "id": generar_id_coleccion(path),
            "nombre": "Mi Colección"
        }]
        write_json(path, coleccion)

def cargar_ultima() -> str:
    try:
        ultima_coleccion_id = read_json("data/ultima_coleccion.json")
        if ultima_coleccion_id:
            return ultima_coleccion_id
        else:
            print("No hay ID de colección guardado previamente.")
            return None
    except Exception as e:
        print(f"Error al leer el archivo de la última colección: {e}")
        return None
