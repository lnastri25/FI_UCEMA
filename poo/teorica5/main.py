#!/bin/python3

from aves import pepita, anastasia, roberta # Importamos una librería (aves) y dentro de las aves, nos enfocamos en Pepita , Anastasia y Roberta
# Pepita sabe volar porque lo hace sin quejarse
#print(pepita.volar_en_circulos())
# Pepita no sabe hablar porque no es un atributo/característica de Pepita poder hablar.
# Además aprendimos que Pepita es una Golondrina.
#print(pepita.hablar())
# A Pepita le gusta comer alpiste. 
#print(pepita.comer_alpiste(200))

# Los atributos de cada objeto hacen a cada objeto lo que son.

"""
- Sabemos que Pepita es un objeto individual, en particular es un objeto de la clase Golondrinas (yo soy un humano dentro de la clase seres humanos por ejemplo),
Que entiende mensajes (lo que las golondrinas entienden) y que tiene las características de una Golondrina, es decir atributos.

- Si tuviese que agrupar los objetos, los agrupo en base a sus características particulares porque las comparten y ese grupo es lo que se conoce como clase. El conjunto abstracto de característcias que me definen a los objetos.

- Dentro de cada clase tengo individuos, que conforman ese conjunto. Eso es lo que se conoce como instancias de una clase.
"""
print("Llamemos a Pepita")
print(pepita)
print("Pepita al comienzo:", pepita.energia)
pepita.volar_en_circulos()
print("Pepita después de volar:", pepita.energia)
print(pepita.comer_alpiste(200))
print("Pepita después de comer:", pepita.energia)
print("Hasta acá Pepita...")

"""
- Pepita tiene una energía basal. Ahora sabemos que a Pepita cuando le damos órdenes, algo en su estado cambia (la energía).

- Entonces ahora sabemos que el estado de pepita está dado por su energía y que pepita tiene como atributos o características saber volar y comer alpiste.

- Los objetos tienen cierto comportamiento que están dados por los mensajes que reciben de algún modo, y ese comportamiento de algun modo puede modificar su estado.

- Un atributo puede tomar el valor que le damos por parámetro, o puede tomar algún valor inicial que le indiquemos.
- No siempre son la misma cantidad de parámetros que de atributos.
"""
print("Llamemos a Anastasia")
print(anastasia)
print("En el caso de Anastasia tiene de energía:", anastasia.energia) # Tiene más energía basal. Tienen diferente estado. 100 ≠ 200.
anastasia.volar_en_circulos()
print(anastasia.energia)
anastasia.comer_alpiste(200)
print(anastasia.energia)
print("Hasta acá Anastasia...")

"""
- Cada vez que ejecutamos el script, nosotros les damos vida a estos objetos y ellos conviven entre sí dentro de lo que es el ambiente (en este caso).
- Dentro del ambiente pueden tener un estado en particular.
- En un ambiente distinto, se puede tener un estado diferente y en cada ambiente, los objetos conviven todos entre si, cada uno con su estado pero a veces pueden compartir algunos de los mismos mensajes.
"""

print("Llamemos a Roberta")
print(roberta)
print("Roberta al comienzo tiene de energía:", roberta.energia)
roberta.volar_en_circulos()
print("Energía después de volvar:", roberta.energia) # No solo parte de un estado distinto, sino que ademas cuando le damos un mensaje lo entiende de forma distinta. No la afecta de la misma manera al estado. No implica la misma energía volar en círculos para roberta que para anastasia y pepita.
# roberta.comer_alpiste(200) --> Roberta es un dragón; no come alpiste
# print("Energía después de comer:", roberta.energia)
roberta.escupir_fuego()
print("Energía después de sacar fuego:", roberta.energia)
roberta.comer_peces(200)
print("Energía después de comer peces:", roberta.energia)
print("Hasta acá Roberta...")

"""
- Aprendimos que hay objetos que entienden los mismos mensajes aunque no sean de la misma clase.

Pepita y Anastasia --> Golondrinas
Roberta --> Dragones
"""

# Tarea
# Hacer que las golondrinas entiendan el mensaje esta_feliz(), y que devuelva si está feliz (que es cuando tienen de energía más de 50) y para los dragones, implementar ese método, pero están felices cuando tienen más de 500 de energía.

print("Arrancamos la tarea")
print("Parte 1:", pepita.esta_feliz())
print("Parte 2:", anastasia.esta_feliz())
print("Parte 3:", roberta.esta_feliz())

# Gracias a is pudimos vertificar que batman, bruno_diaz y bruce_wayne son idénticos, es decir, tienen la misma identidad. Lo mismo sucede con clark_kent y superman.

# De todas formas, en la mayoría de los casos para comparar dos objetos nos alcanza con el operador de equivalencia visto antes en este recorrido, el ya conocido ==

"""
¿Qué es la POO?
    - La programación POO nos permite modelizar cada uno de estos elementos en clases, definiendo sus atributos y métodos (abstracción). Al programar generamos instancias de cada uno de ellos y estableceremos cómo se comunican y relacionan.

    - POO: Forma de programar en la cual se trata de desarrollar el código de forma tal que tengamos pedacitos de código que sean interconectables entre sí, que puedan dialogar entre sí y que nos permitan de ese modo armar un sistema mucho mas complejo.

    - La POO se basa en pensar las herramientas como si estuviesen formadas por objetos. 
    
¿Qué es un objeto?
    - Es una entidad computacional que me permite interactuar dándole mensajes. Es aquel con lo que me puedo comunicar y, él mismo, entiende ciertos mensajes. Tiene referencias internas, lo que se conoce como sus estados o tienen ciertas características internas las cuales el objeto es consciente.


1) __init__:

    __init__ (método interno) viene de la palabra en inglés 'initialize' que en castellano es inicializar. Es lo que se conoce como el constructor de una clase y nos permite darle valores iniciales a los atributos de sus instancias a la hora de crearlas. No es una interfaz porque no le podemos mandar un mensaje.

    __init__ también es un método, pero recordá que solo sirve para darle un valor inicial a los atributos de las instancias cuando las creamos. 

2) Self:

    Por su parte, self (que en castellano sería algo así como yo) es un primer parámetro obligatorio que nos permite acceder a los atributos del objeto que estamos instanciando. Si bien ese parámetro no debe llamarse self obligatoriamente, es la convención que se utiliza para nombrarlo y la respetaremos a lo largo de todo el recorrido.

    - Un atributo siempre va a arrancar con self. 
    - Self también es un parametro, pero es un parametro especial. No se lo cuenta como parametro si me lo preguntan.

    def __init__(self, parametro1, parametro2, etc):
        # las funciones son los diferentes metodos       
        # self: "uno mismo" (siempre pasarlo)
        # self.atributo1 = atributo1
        # self.atributo2 = atributo2

3) Estado:

    - Los objetos tienen estado, que está dado por el conjunto de esos atributos (volar, comer alpiste, etc). Todo eso conforma lo que se conoce como el estado de los opbjetos.
    - El estado de los objetos puede cambiar o modificarse.
    - Estado --> Conjunto de atributos. (self.atributo1, self.atributo2)
    - Los objetos pueden tener distintos estados.
    - Aun con distintos estados, los objetos pueden entender los mismos mensajes (los mensajes se llaman métodos).
    - Para conocer el estado de un objeto, podemos acceder a cada uno de sus atributos escribiendo objeto.atributo, habrás notado que, a diferencia de cuando envíamos un mensaje, al acceder a un atributo no vamos a usar paréntesis.

4) Interfaz/Método/Mensaje:
    - Interfaz --> Conjunto de mensajes/métodos que puede entender una clase.
    - Esos mensajes que entienden los objetos se conocen como interfaz (conjunto de mensajes que entienden).
    - La diferencia entre un método y una funcion es que la funcion no esta dentro de una clase. 
    - El metodo (es como una función), pero forma parte de la clase.
    - Un método es, entonces, la descripción de qué hacer cuando se recibe un mensaje del mismo nombre. El conjunto de estos métodos provee de comportamiento a las instancias de una clase.

5) Polimorfismo:

    - Polimorfismo --> Cuando dos o más objetos entienden el mismo mensaje.
    - Los objetos que comparten su interfaz son polimórficos.
    - En este caso vemos un polimorfismo parcial porque comparten parte de su interfaz y no toda.

    - Los objetos en sí, no saben si son o no polimórficos.
    - Para ver polimorfismo necesitamos un observador u otro actor (en este caso: nosotros).

    - En polimorfismo hablamos de 3 participantes: 
        • La clase/objeto que envía el mensaje y al menos 2 que la reciban. 
        • No alcanza con que 2 clases compartan interfaz, sino que tiene que haber una tercer clase que las ponga en común a las dos.   

6) Raise:

    Cuando lanzamos una excepción provocamos un error explícito que interrumpe el flujo de nuestro programa.

    La excepción no solo aborta el método en el cual se produce sino también la ejecución de todos los métodos de la cadena de envío de mensajes y los posteriores, pero cuidado, porque no se descartan los cambios realizados anteriormente en caso de que los hubiera.

    ej: raise Exception("string) --> suele venir después de un else.

    Con el raise indicamos qué tipo de excepción queremos buscar; esto hace que terminemos la ejecución del programa.

7) Instancia:

    - A cada individuo/objeto dentro de una clase se lo conoce como instancia.

    class "Nombre de la clase" (siempre en mayúscula la primer letra):

    # instanciación del objeto
    pepita = "Nombre de la clase"(100)

8) Clase:

    - Es el gran grupo que engloba a estos objetos.
    - Descripción de objeto. Consta de una serie de métodos y datos que resumen las características de este objeto. Definir clases permite trabajar con código reutilizable. Puesto que desde una clase se puede crear una instancia y así reutilizar el código escrito para esta si tener que volver a escribir el código para la instancia. La instancia toma el patrón de la clase padre. Sin embargo, las variables son idependientes.

    2 tipos de clases:

    A) Clase abstracta:

        - Una clase abstracta es aquella de la que no se pueden declarar instancias, dicho de otra manera no se pueden declarar objetos de una clase abstracta.
        - La finalidad de una clase abstracta es servir como clase base para otras clases a las que generalmente se conoce como clases "concretas".
        - Ejemplo: Dispositivo
        - Las clases abstractas proveen comportamiento a sus subclases.

    B) Clase concreta:

        - Una clase concreta es aquella de la que se pueden declarar instancias, dicho de otra manera se pueden declarar objetos de una clase concreta. 
        - Ejemplo: Notebook y Tablet
        - Las clases concretas se utilizan para crear instancias.

9) Atributos:

    - Características que aplican al objeto solo en el caso en que el sea visible en pantalla por el usuario; entonces sus atributos son el aspecto que refleja, tanto en color, tamaño, posición, si está o no habilitado.

10) Herencia:

    - Mecanismo para compartir automáticamente métodos y datos entre classes, subclases y objetos.
    - Permite crear nuevas clases introduciendo las variaciones con respecto a su clase padre.

    2 tipos de herencia:

    A) Herencia simple: una subclase puede herecar datos y métodos de una clase simple así como añadir o sustraer ciertos comportamientos.

    B) Herencia múltiple: posibilidad de adquirir métodos y datos de varias clases simultáneamente.

    - Para recapitular, cuando dos o más objetos repiten lógica, creamos una clase con el comportamiento en común. 
    - Análogamente, en el caso que dos o más clases repitan lógica, debemos crear una nueva clase a la que llamaremos superclase. 
    - Esta llevará los métodos repetidos de las clases originales (subclases) y haremos que estas últimas hereden de ella. 
    - De esta forma, las subclases que heredan de la superclase sólo tendrán definido su comportamiento particular. 

x) Agregados:

    a) La diferencia entre un método y una funcion es que la funcion no esta dentro de una clase. 
    El metodo (es como una función), pero forma parte de la clase.
    Un método es, entonces, la descripción de qué hacer cuando se recibe un mensaje del mismo nombre. El conjunto de estos métodos provee de comportamiento a las instancias de una clase.

    b) Las funciones retornan un valor mientras que los procedimientos tienen un efecto, es decir, modifican algo.

    c)  = --> asignas parametro
        == --> comparas o igualas parametro
"""