"""
1) OS & SYS:

    - Como mencionamos anteriormente, los scripts suelen interactuar con el sistema de archivos (file system o FS) y el sistema operativo en general (Operative System u OS). Justamente por ello es que el módulo os de Python nos será de particular ayuda cuando escribamos nuestros scripts. Allí encontraremos operaciones como las siguientes:

    os.stat: nos permite obtener estadísticas de un archivo (como por ejemplo su tamaño)

    os.rename: nos permite renombrar archivos

    os.rmdir: nos permite eliminar directorios

    De igual forma, el submódulo os.path nos dará más funcionalidades para interactuar con archivos y sus rutas:

    os.path.dirname: nos permite obtener el directorio donde un archivo está contenido

    os.getcwd: nos permite conocer el directorio donde estamos

    os.path.exists: nos permite saber si un archivo existe

    os.path.join: nos permite concatenar rutas (por ejemplo, combinar /una y ruta para obtener /una/ruta)

    os.listdir: nos permite listar los archivos que tengo dentro de un directorio

    os.chdir: nos permite cambiar a otro directorio


- La biblioteca os tiene muchos métodos útiles para todo lo que se refiere a rutas, creación y eliminación de carpetas, modificación de archivos, etc. Dos métodos muy importantes son:

    os.mkdir(ruta), el cual sirve para crear una carpeta en la ruta indicada (si queremos crearla en la carpeta donde estamos parados solo tenemos que poner el nombre de la carpeta). Nos permite crear una carpeta en cualquier lugar de la computadora; si queremos movernos a la carpeta esa que creamos, hacemos “chdir”,

    os.chdir(ruta), el cual nos permite movernos de carpeta hasta la ruta indicada.

Ejemplos de estos pueden ser:
#Crear la carpeta Prácticas en el directorio actual:
os.mkdir(“Prácticas”)
#Crear la carpeta Teorías en el directorio superior:
os.mkdir(“../Teorías”)
#Movernos a la carpeta Prácticas:
os.chdir(“Prácticas”)
#Movernos desde Prácticas a Teorías:
os.chdir(“../../Teorías”)

2) Por último, el módulo sys nos dará acceso a sys.argv: una lista que contiene el nombre del script y los argumentos con los que se ejecutó un programa.

SYS: nos sirve para tomar parámetros desde la terminal.

2 tipos de archivos:

El que puede leer/escribir.
El que puede ejecutar (ejecutable).

A) Apertura de archivos:
open(path_al_archivo, modo)

- "path_al_archivo" es un objeto de tipo str que indica la ruta en la que se encuentra el archivo. Me dice la ubicacion de mi archivo en la computadora

- "modo" es un objeto de tipo str que indica la forma en la que Python accederá al archivo en cuestión. (forma de manipulación del archivo. Que quiero hacer con el archivo? Lo tengo que saber de antemano)

r: read --> abre un archivo solo para lectura.
r+: read & write --> abre un archivo para escritura y lectura.
a: append --> abre un archivo para agregar información. Si el archivo no existe, crea un nuevo archivo para escritura.
w: write --> abre un archivo solo para escritura. Sobreescribre el archivo si este ya existe. Si el archivo no existe, crea un nuevo archivo para escritura.
w+: --> sirve para escribir y leer en un archivo, y borrar lo que había antes.

B) Cierre de archivos:
archivo = open(path_al_archivo, modo)
archivo.close()

    De no cerrar los archivos, se puede ralentizar la máquina. Con demasiadas cosas abiertas, se utiliza más RAM, lo que afectará el rendimiento de la máquina y del programa que estemos creando.

3) Sin embargo, existe otra forma de apertura de archivos que nos ahorra este paso y siempre nos asegura el cierre de adecuado:

with open(path_al_archivo, modo) as miarch:
#Aquí van las líneas de procesamiento del archivo 

    .read() Lee del archivo según el número de bytes de tamaño. Si no se pasa ningún, entonces lee todo el archivo.
    .readline() Lee como máximo el número de caracteres de tamaño de la línea. Esto continúa hasta el final de la línea y luego regresa.
    .readlines() Esto lee las líneas restantes del objeto de archivo y las devuelve como una lista. Cada elemento de la lista, es una línea del archivo.
    .write(): escribe una cadena en un archivo.
    .writelines(): escribe una lista de cadenas en un archivo.

4) Para Python la escritura y la lectura son dos pasos por separado.
    ~: /Home/User

    ~/Doc/hola.txt → ruta relativa
    ./Doc/hola.txt → ruta relativa
    Home/User/Doc/hola.txt → ruta absoluta (yo estoy asumiendo un usuario entonces si le paso el codigo a otra compu, probablemente el código se rompa porque no voy a tener el mismo usuario)


5) GLOB:

The glob module, which is short for global, is a function that's used to search for files that match a specific file pattern or name. It can be used to search CSV files and for text in files.
"""