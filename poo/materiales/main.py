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

- clase: el gran grupo que engloba a esos objetos.

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

- Los objetos tienen estado, que está dado por el conjunto de esos atributos (volar, comer alpiste, etc). Todo eso conforma lo que se conoce como el estado de los opbjetos.
- El estado de los objetos puede cambiar o modificarse.
- Los objetos tienen cierto comportamiento que están dados por los mensajes que reciben de algún modo, y ese comportamiento de algun modo puede modificar su estado.
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
- Los objetos pueden tener distintos estados.
- Aun con distintos estados, los objetos pueden entender los mismos mensajes (los mensajes se llaman métodos).

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

- A cada individuo/objeto dentro de una clase: instancia

- Esos mensajes que entienden los objetos se conocen como interfaz (conjunto de mensajes que entienden).
"""

"""
- Los objetos que comparten su interfaz son polimórficos.
- En este caso vemos un polimorfismo parcial porque comparten parte de su interfaz y no toda.

- Los objetos en sí, no saben si son o no polimórficos.
- Para ver polimorfismo necesitamos un observador u otro actor (en este caso: nosotros).
"""

"""
class "Nombre de la clase" (siempre en mayúscula):

    def __init__(self, atributo1, atributo2, etc): 
        # las funciones son los diferentes metodos
        # self: "uno mismo" (siempre pasarlo)
        # el init (metodo interno) es el constructor del objeto que me permite darle vida.
        # en el constructor voy a poner todas aquellas característcias que sean necesatrias 

    # instanciación del objeto
    pepita = "Nombre de la clase"(100)
"""

"""
1) La diferencia entre un método y una funcion es que la funcion no esta dentro de una clase. 
 El metodo (es como una función), pero forma parte de la clase.
 Un método es, entonces, la descripción de qué hacer cuando se recibe un mensaje del mismo nombre. El conjunto de estos métodos provee de comportamiento a las instancias de una clase.

2) las funciones retornan un valor mientras que los procedimientos tienen un efecto, es decir, modifican algo.
"""

# Tarea
# Hacer que las golondrinas entiendan el mensaje esta_feliz(), y que devuelva si está feliz (que es cuando tienen de energía más de 50) y para los dragones, implementar ese método, pero están felices cuando tienen más de 500 de energía.

print("Arrancamos la tarea")
print("Parte 1:", pepita.esta_feliz())
print("Parte 2:", anastasia.esta_feliz())
print("Parte 3:", roberta.esta_feliz())

# Gracias a is pudimos vertificar que batman, bruno_diaz y bruce_wayne son idénticos, es decir, tienen la misma identidad. Lo mismo sucede con clark_kent y superman.

# De todas formas, en la mayoría de los casos para comparar dos objetos nos alcanza con el operador de equivalencia visto antes en este recorrido, el ya conocido ==

# Para conocer el estado de un objeto, podemos acceder a cada uno de sus atributos escribiendo objeto.atributo, habrás notado que, a diferencia de cuando envíamos un mensaje, al acceder a un atributo no vamos a usar paréntesis.

"""
1) __init__ viene de la palabra en inglés initialize que en castellano es inicializar. Es lo que se conoce como el constructor de una clase y nos permite darle valores iniciales a los atributos de sus instancias a la hora de crearlas. 

__init__ también es un método, pero recordá que solo sirve para darle un valor inicial a los atributos de las instancias cuando las creamos. 

2) Por su parte, self(que en castellano sería algo así como yo) es un primer parámetro obligatorio que nos permite acceder a los atributos del objeto que estamos instanciando. Si bien ese parámetro no debe llamarse selfobligatoriamente, es la convención que se utiliza para nombrarlo y la respetaremos a lo largo de todo el recorrido.

"""