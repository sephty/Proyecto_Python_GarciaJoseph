import utils.screenController as screenC
import controllers.estadistica as mainCon
from tabulate import tabulate


def menu():
    while True:
        menu = [
            [1, "Añadir un Nuevo Elemento"],
            [2, "Ver Todos los Elementos"],
            [3, "Buscar un Elemento"],
            [4, "Editar un Elemento"],
            [5, "Eliminar un Elemento"],
            [6, "Ver Elementos por Categoría"],
            [7, "Guardar y Cargar Colección de media"],
            [8, "Salir"]
        ]

        print("\n" + "="*43)
        print("   Administrador de Colección de media")
        print("="*43)
        print(tabulate(menu, tablefmt="plain"))
        print("="*43)

        try:
            opcion = int(input("Selecciona una opción (1-8): "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue

        match opcion:
            case 1:

                pass 
            case 2:
                pass 
            case 3:
                pass  
            case 4:
                pass 
            case 5:
                pass 
            case 6:
                pass  
            case 7:
                pass  
            case 8:
                print("Saliendo del programa...")
                screenC.limpiar_pantalla()
                break
            case _:
                print("Opción no válida. Intenta de nuevo.")
                screenC.pausar_pantalla()  

if __name__ == "__main__":
    menu()