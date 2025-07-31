def cargar_coleccion(coleccion_id=None):
    from utils.corefiles import read_json, write_json,cargar_ultima  # Move import to local scope to avoid circular import
    colecciones = read_json("data/coleccion.json")
    coleccion_seleccionada = None

    if coleccion_id is None:
        coleccion_id = cargar_ultima()  

    for coleccion in colecciones:
        if coleccion["id"] == coleccion_id:
            coleccion_seleccionada = coleccion
            break

    if coleccion_seleccionada is None:
        print(f"No se encontró la colección con ID {coleccion_id}.")
        return

    from utils.temporal_data import elementos_temporales  # Moved here to avoid global import
    elementos_temporales["coleccion_id"] = coleccion_id

    for tipo in ["libros", "peliculas", "musica"]:
        ids_elementos = coleccion_seleccionada.get(tipo, [])
        archivo_tipo = f"data/{tipo}.json"
        elementos = read_json(archivo_tipo)
        
        elementos_filtrados = [elem for elem in elementos if elem["id"] in ids_elementos]
        
        elementos_temporales[tipo] = elementos_filtrados

    print(f"Colección con ID {coleccion_id} cargada exitosamente.")

    write_json("data/ultima_coleccion.json", coleccion_id)


def cargar_coleccion_por_id():
    from utils.screenController import limpiar_pantalla  # Delayed import
    limpiar_pantalla()
    coleccion_id = input("Introduce el ID de la colección que deseas cargar: ")
    cargar_coleccion(coleccion_id)

def crear_nueva_coleccion():
    from utils.id_gen import generar_id_coleccion  # Delayed import
    from utils.corefiles import read_json, write_json
    nombre_coleccion = input("Introduce el nombre de la nueva colección: ")

    nueva_coleccion_id = generar_id_coleccion()

    nueva_coleccion = {
        "id": nueva_coleccion_id,
        "nombre": nombre_coleccion,
        "libros": [],
        "peliculas": [],
        "musica": []
    }

    colecciones = read_json("data/coleccion.json")
    colecciones.append(nueva_coleccion)
    write_json("data/coleccion.json", colecciones)

    write_json("data/ultima_coleccion.json", nueva_coleccion_id)

    print(f"¡Colección '{nombre_coleccion}' creada exitosamente.")