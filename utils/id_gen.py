import random

def generar_id_coleccion(path='data/coleccion.json') -> str:
    from utils.corefiles import read_json  # Importación local para evitar ciclo

    datos = read_json(path)
    ids_existentes = {str(item.get("id")) for item in datos if "id" in item}

    for _ in range(1000):
        nuevo_id = str(random.randint(1000, 9999))
        if nuevo_id not in ids_existentes:
            return nuevo_id

    raise RuntimeError("No se pudo generar un ID único para colección.")


def generar_id_media(media_type: str, path: str) -> str:
    from utils.corefiles import read_json  # Importación local para evitar ciclo
    
    datos = read_json(path)
    
    ids = [
        int(item["id"].split("-")[1])
        for item in datos
        if isinstance(item.get("id"), str) and item["id"].startswith(f"{media_type}-")
    ]

    siguiente_num = max(ids, default=0) + 1
    return f"{media_type}-{str(siguiente_num).zfill(3)}"

