from utils.temporal_data import elementos_temporales
from utils.corefiles import read_json, write_json
from utils.screenController import limpiar_pantalla, pausar_pantalla

def eliminar_por_titulo():
    limpiar_pantalla()
    print("=" * 43)
    print("        Eliminar Elemento por Título")
    print("=" * 43)

    tipo = input("Tipo de elemento (libros/peliculas/musica): ").lower()
    if tipo not in elementos_temporales:
        print("Tipo no válido.")
        pausar_pantalla()
        return

    titulo = input("Título del elemento a eliminar: ").strip().lower()
    lista = elementos_temporales.get(tipo, [])

    encontrado = None
    for item in lista:
        if item["titulo"].lower() == titulo:
            encontrado = item
            break

    if not encontrado:
        print("Elemento no encontrado.")
        pausar_pantalla()
        return

    confirm = input(f"¿Estás seguro de eliminar '{encontrado['titulo']}'? (s/n): ").lower()
    if confirm == "s":
        lista.remove(encontrado)

        data = read_json(f"data/{tipo}.json")
        data = [item for item in data if item["id"] != encontrado["id"]]
        write_json(f"data/{tipo}.json", data)

        print("Elemento eliminado correctamente.")
    else:
        print("Operación cancelada.")

    pausar_pantalla()


def eliminar_por_id():
    limpiar_pantalla()
    print("=" * 43)
    print("        Eliminar Elemento por ID")
    print("=" * 43)

    tipo = input("Tipo de elemento (libros/peliculas/musica): ").lower()
    if tipo not in elementos_temporales:
        print("Tipo no válido.")
        pausar_pantalla()
        return

    id_buscar = input("ID del elemento a eliminar: ").strip()
    lista = elementos_temporales.get(tipo, [])

    encontrado = None
    for item in lista:
        if item["id"] == id_buscar:
            encontrado = item
            break

    if not encontrado:
        print("Elemento no encontrado.")
        pausar_pantalla()
        return

    confirm = input(f"¿Estás seguro de eliminar '{encontrado['titulo']}' (ID: {id_buscar})? (s/n): ").lower()
    if confirm == "s":
        lista.remove(encontrado)

        data = read_json(f"data/{tipo}.json")
        data = [item for item in data if item["id"] != id_buscar]
        write_json(f"data/{tipo}.json", data)

        print("Elemento eliminado correctamente.")
    else:
        print("Operación cancelada.")

    pausar_pantalla()
