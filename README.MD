hecho por: Joseph Guilliani Garcia Jimenez
fecha: 30/07/2025
programa: Gestion de coleccion de media


# Administrador de Colección de Libros/Películas/Música

El Administrador de Colección de Libros/Películas/Música es una aplicación de consola que permite al usuario gestionar una colección personal de elementos culturales, como libros, películas o música. El objetivo principal es ofrecer una herramienta sencilla para organizar títulos, con detalles como el autor, género, y una valoración. Esto es útil para quienes desean mantener un registro estructurado de su colección, consultar rápidamente algún elemento o encontrar recomendaciones basadas en ciertos criterios.

---

## Problemática

Para muchas personas, organizar su colección de libros, películas o música puede ser un desafío, especialmente cuando el número de elementos crece y es difícil recordar detalles específicos. Sin un sistema, es complicado:

- Mantener un registro ordenado de cada elemento con sus características.
- Consultar detalles de cada título, como autor, género o valoraciones, sin revisar manualmente cada uno.
- Realizar búsquedas rápidas por título, género o autor.

Este administrador de colección ayuda a resolver estas problemáticas al ofrecer una interfaz de consola donde los datos quedan organizados y accesibles. Además, la aplicación permite guardar y cargar los datos en un archivo JSON, asegurando que el registro de la colección se mantenga entre sesiones.

---

## Tecnologías y Herramientas

**Front-end:**  
Aplicación de consola en Python

**Recursos:**  
- Diseño de los menús: [ProgrammersLand Menu Gist](https://gist.github.com/programmersland/0d76751149e083e073e7aac03e6fbae0)  
- Librería para mostrar la información en formato de tablas: [Tabulate en PyPI](https://pypi.org/project/tabulate/)  
- GitHub: Para la gestión de versiones del código en el desarrollo, usando _conventional commits_.

---

## Funciones Principales

### Añadir Elemento a la Colección

Permite al usuario registrar un nuevo elemento en la colección, especificando:

- Título  
- Autor/Director/Artista (según el tipo de colección)  
- Género  
- Valoración o puntuación (opcional)  

Los datos se guardan en un archivo JSON para su persistencia.

### Listar Elementos de la Colección

Muestra todos los elementos registrados en la colección.  
Puede incluir opciones de visualización adicionales, como listar por categoría (libros, películas o música) o por género.

### Buscar Elemento

Función para buscar un elemento en la colección filtrando por:

- Título  
- Autor o género  

Facilita el acceso rápido a detalles específicos sin necesidad de revisar toda la lista.

### Editar Elemento

Permite modificar la información de un elemento específico en la colección.  
Los usuarios pueden actualizar detalles como el título, el autor o la valoración del elemento, y los cambios se guardan automáticamente en el archivo JSON.

### Eliminar Elemento

Elimina un elemento de la colección según el título o un identificador específico.  
Asegura que la colección esté actualizada y sin elementos duplicados o innecesarios.

### Cargar y Guardar Colección en JSON

- Al iniciar el programa, la aplicación carga la colección desde un archivo JSON para continuar donde el usuario la dejó.  
- Al finalizar, guarda automáticamente cualquier cambio realizado en el archivo JSON, manteniendo la persistencia de los datos.
