from tabulate import tabulate
from utils.screenController import limpiar_pantalla, pausar_pantalla

def musica_main():
        menu = [
            [1, "Añadir un Nuevo Elemento"],
            [2, "Ver Todos los Elementos"],
            [3, "Buscar un Elemento"],
            [4, "Editar un Elemento"],
            [5, "Eliminar un Elemento"],
            [6, "Ver Elementos por Categoría"],
            [7, "Guardar y Cargar Colección"],
            [8, "Salir"]
        ]