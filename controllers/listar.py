from utils.temporal_data import elementos_temporales
from tabulate import tabulate

def buscar_por_titulo():
    # Pedimos el término de búsqueda al usuario
    search_term = input("Introduce el término de búsqueda para el título: ").lower()
    
    resultados = []
    for tipo, items in elementos_temporales.items():  # Recorre todos los tipos: libros, peliculas, musica
        for elem in items:
            if "titulo" in elem and search_term in elem["titulo"].lower():
                # Añadimos el tipo para identificar de qué tipo es el resultado
                resultados.append({"Tipo": tipo.capitalize(), "Título": elem["titulo"]})
    
    # Si no hay resultados
    if not resultados:
        print("No se encontraron resultados.")
    else:
        # Mostrar los resultados usando tabulate
        print(tabulate(resultados, headers="keys", tablefmt="pretty"))
    

def buscar_por_autor_director_artista():
    # Pedimos el término de búsqueda al usuario
    search_term = input("Introduce el término de búsqueda para autor/director/artista: ").lower()
    
    resultados = []
    for tipo, items in elementos_temporales.items():  # Recorre todos los tipos: libros, peliculas, musica
        for elem in items:
            if ("autor" in elem and search_term in elem["autor"].lower()) or \
               ("director" in elem and search_term in elem["director"].lower()) or \
               ("artista" in elem and search_term in elem["artista"].lower()):
                # Añadimos el tipo para identificar de qué tipo es el resultado
                resultados.append({"Tipo": tipo.capitalize(), "Autor/Director/Artista": elem.get("autor") or elem.get("director") or elem.get("artista")})
    
    # Si no hay resultados
    if not resultados:
        print("No se encontraron resultados.")
    else:
        # Mostrar los resultados usando tabulate
        print(tabulate(resultados, headers="keys", tablefmt="pretty"))
    

def buscar_por_genero():
    # Pedimos el término de búsqueda al usuario
    search_term = input("Introduce el término de búsqueda para el género: ").lower()
    
    resultados = []
    for tipo, items in elementos_temporales.items():  # Recorre todos los tipos: libros, peliculas, musica
        for elem in items:
            if "genero" in elem and search_term in elem["genero"].lower():
                # Añadimos el tipo para identificar de qué tipo es el resultado
                resultados.append({"Tipo": tipo.capitalize(), "Género": elem["genero"]})
    
    # Si no hay resultados
    if not resultados:
        print("No se encontraron resultados.")
    else:
        # Mostrar los resultados usando tabulate
        print(tabulate(resultados, headers="keys", tablefmt="pretty"))
    

def buscar_elemento():
    # Pedimos el campo y valor para la búsqueda
    campo = input("Introduce el campo para buscar (titulo, autor, director, artista, genero): ").lower()
    valor = input(f"Introduce el valor para buscar en el campo '{campo}': ").lower()
    
    resultados = []
    for tipo, items in elementos_temporales.items():  # Recorre todos los tipos: libros, peliculas, musica
        for elem in items:
            if campo == "titulo" and "titulo" in elem and valor in elem["titulo"].lower():
                resultados.append({"Tipo": tipo.capitalize(), "Título": elem["titulo"]})
            elif campo == "autor" and "autor" in elem and valor in elem["autor"].lower():
                resultados.append({"Tipo": tipo.capitalize(), "Autor": elem["autor"]})
            elif campo == "director" and "director" in elem and valor in elem["director"].lower():
                resultados.append({"Tipo": tipo.capitalize(), "Director": elem["director"]})
            elif campo == "artista" and "artista" in elem and valor in elem["artista"].lower():
                resultados.append({"Tipo": tipo.capitalize(), "Artista": elem["artista"]})
            elif campo == "genero" and "genero" in elem and valor in elem["genero"].lower():
                resultados.append({"Tipo": tipo.capitalize(), "Género": elem["genero"]})
    
    # Si no hay resultados
    if not resultados:
        print("No se encontraron resultados.")
    else:
        # Mostrar los resultados usando tabulate
        print(tabulate(resultados, headers="keys", tablefmt="pretty"))


