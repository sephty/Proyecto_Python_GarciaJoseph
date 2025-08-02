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

def cargar_coleccion(coleccion_id=None):
    from utils.corefiles import read_json, write_json, cargar_ultima  # Avoid circular import
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

    from utils.temporal_data import elementos_temporales
    elementos_temporales["coleccion_id"] = coleccion_id

    for tipo in ["libros", "peliculas", "musica"]:  # 'musica' for music
        ids_elementos = coleccion_seleccionada.get(tipo, [])
        
        if tipo == "musica":  # Use 'musica.json' for music
            archivo_tipo = "data/musica.json"
        else:
            archivo_tipo = f"data/{tipo}.json"
        
        elementos = read_json(archivo_tipo)

        # Filter elements by IDs in the collection
        elementos_filtrados = [elem for elem in elementos if elem["id"] in ids_elementos]

        # Save filtered elements into temporal data
        elementos_temporales[tipo] = elementos_filtrados

    print(f"Colección con ID {coleccion_id} cargada exitosamente.")
    write_json("data/ultima_coleccion.json", coleccion_id)

def guardar_coleccion_actual():
    from utils.corefiles import read_json, write_json
    from utils.temporal_data import elementos_temporales
    from utils.id_gen import generar_id_media

    coleccion_id = elementos_temporales.get("coleccion_id")
    if not coleccion_id:
        print("No hay una colección activa cargada.")
        return

    colecciones = read_json("data/coleccion.json")
    libros_data = read_json("data/libros.json")
    peliculas_data = read_json("data/peliculas.json")
    musica_data = read_json("data/musica.json")  

    tipos_archivos = {
        "libros": ("data/libros.json", libros_data),
        "peliculas": ("data/peliculas.json", peliculas_data),
        "musica": ("data/musica.json", musica_data)  
    }

    for tipo, (archivo_path, archivo_data) in tipos_archivos.items():
        nuevos_elementos = elementos_temporales.get(tipo, [])

        for elem in nuevos_elementos:
            if "id" not in elem:
                elem["id"] = generar_id_media(tipo, archivo_path)

        archivo_data.extend(nuevos_elementos)
        write_json(archivo_path, archivo_data)

        for coleccion in colecciones:
            if coleccion["id"] == coleccion_id:
                if tipo not in coleccion:
                    coleccion[tipo] = []
                coleccion[tipo].extend([elem["id"] for elem in nuevos_elementos])
                break

        print(f"{len(nuevos_elementos)} {tipo} guardado(s) en {archivo_path}")

    write_json("data/coleccion.json", colecciones)
    print("Colección actual actualizada correctamente.")




def crear_nueva_coleccion():
    from utils.screenController import limpiar_pantalla
    from utils.id_gen import generar_id_coleccion
    from utils.corefiles import read_json, write_json
    from utils.temporal_data import elementos_temporales
    limpiar_pantalla()
    print("=" * 43)
    print("   Crear una Nueva Colección")
    print("=" * 43)

    nombre = input("Introduce el nombre de la nueva colección: ")
    if not nombre:
        print("Nombre no puede estar vacío.")
        return crear_nueva_coleccion()

    colecciones = read_json("data/coleccion.json")
    coleccion_id = generar_id_coleccion()
    colecciones.append({
        "id": coleccion_id,
        "nombre": nombre
    })
    write_json("data/coleccion.json", colecciones)
    elementos_temporales["coleccion_id"] = coleccion_id
    print(f"Colección {nombre} creada con éxito.")
