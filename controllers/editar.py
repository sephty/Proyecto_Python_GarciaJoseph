from utils.screenController import limpiar_pantalla, pausar_pantalla
from utils.temporal_data import elementos_temporales
from utils.corefiles import write_json, read_json

def seleccionar_elemento(tipo: str):
    items = elementos_temporales.get(tipo, [])
    if not items:
        print(f"No hay {tipo} cargados en la colección actual.")
        pausar_pantalla()
        return None

    print(f"\nLista de {tipo}:")
    for idx, item in enumerate(items, 1):
        print(f"{idx}. {item['titulo']} (ID: {item['id']})")

    seleccion = input("Introduce el ID del elemento que deseas editar: ")
    for item in items:
        if item["id"] == seleccion:
            return item

    print(" Elemento no encontrado.")
    pausar_pantalla()
    return None

def editar_campo(item: dict, campo: str):
    valor_actual = item.get(campo, "")
    nuevo_valor = input(f"{campo.capitalize()} actual: '{valor_actual}' → Nuevo valor (deja vacío para no cambiar): ")
    if nuevo_valor.strip():
        if campo == "valoracion":
            try:
                nuevo_valor = int(nuevo_valor)
                if not (1 <= nuevo_valor <= 5):
                    print(" La valoración debe estar entre 1 y 5.")
                    return
            except ValueError:
                print(" Valor inválido. Se mantiene el anterior.")
                return
        elif campo == "anio":
            try:
                nuevo_valor = int(nuevo_valor)
                if not (1900 <= nuevo_valor <= 2100):
                    print(" El año debe ser entre 1900 y 2100.")
                    return
            except ValueError:
                print(" Año inválido. Se mantiene el anterior.")
                return

        item[campo] = nuevo_valor

def editar_elemento(tipo: str, campo: str):
    limpiar_pantalla()
    print("=" * 43)
    print(f"       Editar {campo.capitalize()} de un {tipo.capitalize()}")
    print("=" * 43)

    item = seleccionar_elemento(tipo)
    if not item:
        return

    editar_campo(item, campo)

    print("Elemento editado correctamente.")
    pausar_pantalla()


    if tipo == "libros":
        libros_data = read_json("data/libros.json")
        for i, existing_item in enumerate(libros_data):
            if existing_item["id"] == item["id"]:
                libros_data[i] = item  
                break
        write_json("data/libros.json", libros_data)
    elif tipo == "peliculas":
        peliculas_data = read_json("data/peliculas.json")
        for i, existing_item in enumerate(peliculas_data):
            if existing_item["id"] == item["id"]:
                peliculas_data[i] = item  
                break
        write_json("data/peliculas.json", peliculas_data)
    elif tipo == "musica":
        musica_data = read_json("data/musica.json")
        for i, existing_item in enumerate(musica_data):
            if existing_item["id"] == item["id"]:
                musica_data[i] = item  
                break
        write_json("data/musica.json", musica_data)


