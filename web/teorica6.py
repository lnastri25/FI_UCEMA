"""

1) Internet:

    - Internet por más de que parezca mentira, es algo fisico. Es una conexion fisica ('cableada') entre todas las computadoras del mundo. Quizás una está en Movistar Argentina, pero la otra puede estar en T-Mobile USA. Cada vez, necesitamos que esa conexión sea mejor.

    - Internet se podría definir como la red de redes de computadoras, conectadas por medio de un cableado físico que permite intercambiar información entre todos sus usuarios.

    - Para acceder al servicio que ofrece la información, debemos tener dos programas que se ejecutan en dos computadoras diferentes y que nos permiten compartir recursos.

    - A la computadora que ejecuta el programa que proporciona el recurso o información se la denomina servidor y a la computadora que consume un recurso o información se la denomina cliente. En la computadora del cliente se ejecutará entonces el programa que le permite utilizar el recurso o leer la información.

    - Pero ¿Qué tipo de recursos pueden brindarse o consimirse a través de internet? Por medio de Internet podemos enviar mensajes, programas ejecutables, archivos de texto, consultar bases de datos, etc.

2) WEB:

    - La Web en particular, diminutivo de World Wide Web, es un conjunto de páginas interconectadas por las cuales podemos navegar, las cuales están disponibles gracias a la existencia de la internet.

    - Estas páginas web están pensadas para consumir contenido hipertextual, es decir contenido que contiene vínculos o enlaces a otros contenidos.

3) Introducción al concepto de Cloud Computing:

    - La computación en la nube o Cloud Computing es el consumo o prestación bajo demanda de recursos tecnologicos a través de Internet.

    - En lugar de comprar y mantener servidores y centros de datos físicos(es decir una super duper máquina en tu casa), podés consumir los servicios tecnológicos, como potencia informática, almacenamiento y bases de datos, según te sea necesario, en el momento que te sea necesario, de un proveedor.

    - A traves de la conexion web, no solamente vamos a poder compartir archivos, sino que vamos a poder compartir Hardware.

4) Arquitectura Web (Cliente .VS. Servidor):

    - Los sistemas Web hoy en día presentan en genarl una arquitectura distribuida, es decir que sus componentes están distribuidos en dos tipos de nodos: clientes (muchos) y servidores (uno). En esta arquitectura, llamada cliente-servidor, los clientes se comunican con el servidor siguiendo un protocolo de pedido-respuesta en el que:

        a) Cliente (Front-End):
        • Un cliente hace un pedido. El cliente siempre es el que consume y está demandando constantemente (contenido, datos, etc.)
        • El cliente se encarga de presentar (renderizar/visualizar) la respuesta al usuario final.
            --> Lenguajes utilizados: CSS y HTML.

        b) Servidor (Back-End):
        • El servidor procesa el pedido y responde a esa demanda del cliente. Siempre aporta algo (contenido, datos, etc.)
            --> Lenguajes utilizados: Python.

            - Para que se cumpla esta relación tiene que, sí o sí, haber una comunicación entre Cliente y Servidor. Para que la comunicación sea efectiva se necesita de un protocolo.

    - Esta comunicación ocurre a través de redes Intranets o la misma Internet, empleando un protocolo llamado HTTP, sobre el cuál hablaremos en el punto siguiente.

    - Entonces en la arquitectura web cliente-servidor, los servidores son quienes almacenan y proveen la información o recursos dados, y los clientes son responsables de presentar la información al usuario, empleando tecnologías específicas de la Web.

5) Protocolos de comunicación (HTTP):

    - ¿Alguna vez te preguntaste cómo es que logramos comunicarnos los seres humanos? ¿Cómo es que las palabras pueden estructurarse en conversaciones ordenadas? Bueno, los seres humanos somos capaces de estructurar las palabras, y estas en oraciones que devienen en conversaciones. En este proceso se pone en juego no solo cuestiones ficiológicas, sino también cuestiones culturales y personales, como: la lengua, las normas sociales, los valores culturales, los intereses y propósitos individuales. Por tanto, lo que pensamos como un simple intercambio de palabras, se convierte en una actividad compleja, matizada con el ritmo de todo esta información extra...o meta.

    - Los protocolos, como verás, forman parte de nuestras vidas más de lo que pensábamos. Y estos pueden variar según el entorno en el que nos movemos. Cada ámbito posee sus propias reglas para la comunicación. No nos expresamos de igual modo cuando estamos en un recital, que cuando estamos en la facultad ¿No?

        a) Protocolo:  
        - Este conjunto de reglas de comunicación, implícitas o explícitas, se denomina protocolo y en Internet hay uno específico para establecer la comunicación efectiva entre servidores y clientes. 
        - Este protocolo fue creado para la transferencia de archivos hipertextuales y se llama justamente HTTP, por las siglas en inglés de protocolo de transferencia de hipertexto (HyperText Transfer Protocol).

        - Este protocolo de comunicación empleado en la Web tiene ciertas características que debemos tener en cuenta:

            • Pedido-Respuesta: se abre una conexión por cada pedido, que surge del cliente, y el servidor la cierra cuando ha enviado la respuesta. (El servidor jamás le hace un pedido al cliente)

            • Stateless: el protocolo per-sé no maneja ninguna noción de memoria de pedidos anteriores. 
                - Esto quiere decir una vez que hay un pedido desde el cleinte, el servidor va a responder pero no hay memoria, es decir, que cierra la conexion después de cada pedido. Por lo tanto, NO puedo volver 3hs después y pedirle datos sobre el pedido que le había hecho anteriormente.

            • Textual: se intercambian mensajes de sólo texto.

            • Basado en códigos de respuesta: incluso para los flujos de error; no hay memoria compartida, continuaciones, excepciones ni eventos.

6) Presentación:

    - De lo que dijimos anteriormente se desprende que la presentación o representación de los datos por el servidor corren por parte del cliente. Según lo vivenciado navegando en internet sabemos que las presentaciones son mucho más ricas e interactivas que simple texto. ¡Con el texto enviado por el servidor plano no nos alcanza!

    - Lo que el servidor responde normalmente es el código fuente de una página escrita usando una combinación de lenguajes, que es interpretado por un programa del cliente, el mismo programa que también es responsable de crear las conexiones HTTP.

    - ¿Saben cómo se llama esta aplicación? Adivinaron, ¡es el navegador (browser)!

    - Los navegadores modernos son capaces de entender algunos lenguajes sin necesidad de ningún complemento (plugin), que son los que constituyen como el estándar la Web:

        • HTML: lenguajes basado en etiquetas, emparentado con XML, diseñado para estructurar información.

        • CSS: lenguaje para formatear información (estructurada en HTML).

        • JavaScript: lenguaje de propósito general, que en los navegadores es utilizado para desarrollar cualquier lógica de aplicación. Este último nos permite entre otras cosas:

            □ Mutar, acceder a, y observar eventos del DOM (la representación del contenido HTML).
            □ Implementar efectos visuales complejos; Realizar pedidos al servidor en segundo plano.
            □ Implementar navegabilidad del lado del cliente.


    • El cliente va a renderizar la data que manda el servidor utilizando ciertas tecnologías (HTML, CSS, JavaScript).

7) Página Web:

    - Un archivo HTML expuesto en la nube.
    - Es algo más estático. 
    - NO almacena (memoriza, guarda) información.

8) Sitio Web:

    - Conjunto de páginas web.
    - Diferencia entre sitio y página: Son muchos archivos HTML interconectados.

9) Aplicación Web:

    - Tiene una base datos asociada y la lógica (el código) para procesar y manejar la información y almacenar datos.
    - Persisto (almaceno) información en una base de datos.
    - Ejemplo: Mercado Libre

    a) Aplicacion Rest:
        - Para que una aplicación sea rest, tiene que tener una url asociada a un recurso.
        - Los verbos HTTP disparan acciones particulares --> siempre hablando de apliaciones Rest.

        ¿Cómo me doy que una aplicación es Rest?
        
        - Para que sea Rest una aplicación cada url distinta tiene que hacer referencia a un recurso en particular, recurso: un tipo de ítem de la base de datos. 
            --> Ejemplos: Mercado Libre

            - Cuando yo busco libros en el buscador, va a buscar todos los resultados en la base de datos de libros. https://listado.mercadolibre.com.ar/libros#D[A:libros]
            - Cuando yo busco aros de plata en el buscador, va a buscar todos los resultados en la base de datos de aros de plata. 
            https://listado.mercadolibre.com.ar/aros-de-plata#D[A:aros%20de%20plata]
            
            https://www.mercadolibre.com.ar/

            “Http es el protocolo con el que yo me estoy comunicando al servidor de Mercado Libre”
s
10) URL:

    - Me dice el protocolo que voy a estar usando (HTTPS, 'S de secure') y el recurso que voy a estar usando.

11) Tipos de verbos:

    - Tiene al menos 4 verbos HTTP importantes --> disparan acciones particulares --> SIEMPRE HABLANDO de aplicaciones REST.

    a) Get:

        - Es el verbo HTTP asociado a las consultas.
        - El 'get' siempre lo hace el cliente; La magia de buscar la hace el servidor.

    b) Post:

        - Es el verbvo HTTP que está asociado a escribir o persistir datos (de cero).

    c) Delete:

        - Es el verbo HTTP asociado a borrar datos.

    d) Patch:

        - Es el verbo HTTP asociado a modificar/reescribir datos.

x) Adicionales:

    • Request --> pedido. La biblioteca 'requests' me permite hacer pedidos en Python.
    • JSON --> es como una estructura de diccionarios, que tiene sus 'keys' y sus 'values'.

"""