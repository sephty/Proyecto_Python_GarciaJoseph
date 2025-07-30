import utils.screenController as screenC
import controllers.menuCon as mainCon
from tabulate import tabulate
import utils.corefiles as corefiles


def menu():
    while True:
        screenC.limpiar_pantalla()
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
            screenC.pausar_pantalla()
            continue

        match opcion:
            case 1:
                mainCon.opcion_1()
            case 2:
                mainCon.opcion_2()
            case 3:
                mainCon.opcion_3()
            case 4:
                mainCon.opcion_4() 
            case 5:
                mainCon.opcion_5() 
            case 6:
                mainCon.opcion_6()  
            case 7:
                mainCon.opcion_7()  
            case 8:
                print("Saliendo del programa...")
                screenC.limpiar_pantalla()
                break
            case _:
                print("Opción no válida. Intenta de nuevo.")
                screenC.pausar_pantalla() 
                return menu()

if __name__ == "__main__":
    menu()