from utils.temporal_data import elementos_temporales


def buscar_por_titulo(tipo: str):
    search_term = "some_default_term" 
    return [elem for elem in elementos_temporales[tipo] if search_term in elem["titulo"].lower()]


def buscar_por_autor_director_artista(tipo: str):
    search_term = "some_default_term"  
    return [elem for elem in elementos_temporales[tipo] if 
            ("autor" in elem and search_term in elem["autor"].lower()) or
            ("director" in elem and search_term in elem["director"].lower()) or
            ("artista" in elem and search_term in elem["artista"].lower())]


def buscar_por_genero(tipo: str):
    search_term = "some_default_term"  
    return [elem for elem in elementos_temporales[tipo] if search_term in elem["genero"].lower()]


def buscar_elemento(tipo: str, campo: str, valor: str):
    # Ensure that 'valor' is lower case to make the search case-insensitive
    valor = valor.lower()
    resultados = []
    
    # Search in libros (books)
    if tipo == "libros":
        for libro in elementos_temporales.get("libros", []):
            if campo == "titulo" and valor in libro["titulo"].lower():
                resultados.append(libro)
            elif campo == "autor" and valor in libro["autor"].lower():
                resultados.append(libro)
            elif campo == "genero" and valor in libro["genero"].lower():
                resultados.append(libro)

    # Search in peliculas (movies)
    elif tipo == "peliculas":
        for pelicula in elementos_temporales.get("peliculas", []):
            if campo == "titulo" and valor in pelicula["titulo"].lower():
                resultados.append(pelicula)
            elif campo == "director" and valor in pelicula["director"].lower():
                resultados.append(pelicula)
            elif campo == "genero" and valor in pelicula["genero"].lower():
                resultados.append(pelicula)

    # Search in musica (music)
    elif tipo == "musica":
        for musica in elementos_temporales.get("musica", []):
            if campo == "titulo" and valor in musica["titulo"].lower():
                resultados.append(musica)
            elif campo == "artista" and valor in musica["artista"].lower():
                resultados.append(musica)
            elif campo == "genero" and valor in musica["genero"].lower():
                resultados.append(musica)

    return resultados
