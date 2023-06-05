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

9) API (Aplicación Web):

    - Tiene una base datos asociada y la lógica (el código) para procesar y manejar la información y almacenar datos.
    - Persisto (almaceno) información en una base de datos.
    - Ejemplo: Mercado Libre

    a) API REST (Aplicación Resst):
        - Para que una aplicación sea rest, tiene que tener una url asociada a un recurso.
        - Los verbos HTTP disparan acciones particulares --> siempre hablando de apliaciones Rest.
        - Mapeo directo entre la URL y los recursos.
        - Se espera que cuando uno le pega a una ruta en particular, con un verbo http en particular, desencadene una situacion en particular. Hay verbos asociadas a distintas URL's
        - Para cada URL de una API rest, voy a tener ciertos verbos asociados. Depende de la url a la que yo le este pegando, voy a tener distintos verbos para usar.
        - Soportan distintos verbos HTTP.

        ¿Cómo me doy que una aplicación es Rest?
        
        - Para que sea Rest una aplicación cada url distinta tiene que hacer referencia a un recurso en particular, recurso: un tipo de ítem de la base de datos. 
            --> Ejemplos: Mercado Libre

            - Cuando yo busco libros en el buscador, va a buscar todos los resultados en la base de datos de libros. https://listado.mercadolibre.com.ar/libros#D[A:libros]
            - Cuando yo busco aros de plata en el buscador, va a buscar todos los resultados en la base de datos de aros de plata. 
            https://listado.mercadolibre.com.ar/aros-de-plata#D[A:aros%20de%20plata]
            
            https://www.mercadolibre.com.ar/

            “Http es el protocolo con el que yo me estoy comunicando al servidor de Mercado Libre”

10) URL:

    - Me dice el protocolo que voy a estar usando (HTTPS, 'S de secure') y el recurso que voy a estar usando.

    10.1) Partes de una URL:

        a) Protocolo: 
            - Sirve para conectarnos de una computadora a la otra. Para cada tipo de conexión que hagamos va a existir un protocolo en particular.

        b) Dominio:
            - Es como una especie de 'Nickname'. Es el nombre con el cual voy a mapear una IP en particular. Por detrás es una IP (código con el que puedo trackear una computadora en particular). Enmascara a la IP.

        c) Recurso: 
            - Es lo que se almacena en la base de datos. Si quiero buscar aros de plata, pongo /aros.de.plata y eso se va a ir a buscar a la base de datos de la URL.

            - Me traigo todos los ítems asociados a ese recurso.

            - Para crear un ítem nuevo, le tengo que pegar a /recurso y sobre ese voy a hacer el 'post'.

            - Un recurso es un objeto con datos asociados, relaciones con otros recursos y un conjunto de métodos que operan sobre él.

        d) Parámetros:
            - Son los filtros que le voy a estar pasando a la base de datos. Si quiero buscar aros de plata, pongo /aros.de.plata y eso se va a ir a buscar a la base de datos de la URL. Si quiero buscar aros de plata de 1000 pesos, pongo /aros.de.plata?precio=1000&color=plata y eso se va a ir a buscar a la base de datos de la URL.

            - Al /recurso, con un get, accedo a todos los items del recurso.

            - Puedo acceder de todas maneras haciendo /recurso/id --> me traigo la fila('row') del item en donde está en la base de datos. Lo que hago con esto es acceder a un item en particular de este recurso.

            - Me traigo un solo ítem particular asociado a ese recurso en particular.

        e) Query Params:
            - Filtro mediante la URL a que cosa voy a acceder a la base de datos de una API --> ?key=value (query params). Todo las claves que yo le paso a la api a través de la URL para filtrar la búsuqueda de la base de datos. 
            
            - El signo de pregunta ('?') me indica que a partir de ahí empiezan los parámetros. 
            - Para concatenar los parámetros se uso el signo de ampersand ('&').

        - Ejemplo: 'https://macowins-server.herokuapp.com/prendas?talle=40&tipo=pantalon'

            • url --> 'https://macowins-server.herokuapp.com/prendas?talle=40&tipo=pantalon'
            • https// --> protocolo
            • macowins-server.herokuapp.com --> dominio
            • prendas--> recurso
            • ?talle=40&tipo=pantalon' --> parámetro (trame la prenda que tenga el talle igual a 40 y el tipo igual a pantalón)

        • La diferencia entre PATH y URL es que la url funciona buscando un recurso en una página a la cual accedo a traves de internet. Podríamos decir que son una especia de path via internet. En cambio, cuando hablamos de path, estoy accediendo de forma local y es la dirección exacta hacia un recurso o archivo en una computadora local.

11) Tipos de verbos:

    - Tiene al menos 4 verbos HTTP importantes --> disparan acciones particulares --> SIEMPRE HABLANDO de aplicaciones REST.

    a) Get:
        - Es el verbo HTTP asociado a las consultas.
        - El 'get' siempre lo hace el cliente; La magia de buscar la hace el servidor.

    b) Post:
        - Es el verbvo HTTP que está asociado a escribir o persistir datos (de cero).
        - Cuando le pego a la URL, le tengo que pasar los datos. 
        - Cada pedido HTTP, tiene asociado una metadata --> 'headers=headers'

    c) Delete:
        - Es el verbo HTTP asociado a borrar datos.

    d) Patch:
        - Es el verbo HTTP asociado a modificar/reescribir 'una parte' de los datos.

    e) Put:
        - Es el verbo HTTP a modificar 'todo'.

12) Rest y sus URL's:

    • Formalización de REST: REST es un tipo de arquitectura de desarrollo web que se basa en el uso correcto de URLs y HTPP. Organizaremos nuestras rutas, tanto de una API como de un sitio común y corriente, en forma de recursos y colecciones.

        • GET /ventas/: consultar todos (listar)
        • DELETE /ventas/: borrar todos
        • POST /ventas/: crear uno
        • POST /ventas/1 crear uno con ID (QMP no lo soporta)
        • GET /ventas/1: consultar uno
        • PUT /ventas/1: modificar uno
        • DELETE /ventas/1: eliminar uno

        a) Reglas básicas para escribir las rutas REST:

            1) Debe evitarse usar verbos
            2) No debemos tener más de una URI para identificar un mismo recurso
            3) Deben ser independiente de formato
            4) Deben mantener una jerarquía lógica
            5) Los filtrados de información de un recurso no se hacen en la URI

13) Flask:

    - Flask es un micro framework web, que nos permite la construcción de APIs y aplicaciones REST. Está diseñado para que empezar sea rápido y fácil, con la capacidad de escalar a aplicaciones complejas. Flask ofrece sugerencias, pero no impone dependencias ni diseño de proyecto.

14) API:

    - Es un software que suele estar del lado del servidor.
    - Lo que hace la API es administrar los recursos de mi aplicación.
    - Expone los recursos en los distintos endpoints (rutas).
    - Tienen rutas ('endpoints') --> URL en las cuales se accede a los recursos.
    - Se programan todas aquellas acciones que se desencadenan cuando un usuario accede a esos 'endpoints'.

    a) Rutas:
        - Nuestra aplicación Flask se compondrá de una o más rutas que expondrán los distintos recursos de nuestro sistema. Cada ruta nos dice, como mínimo dos cosas:
        1) Bajo qué URL se expondrá el recurso
        2) Qué se responderá cuando se lo acceda

    b) Decordador:
        - Ejemplo: @app.get("/")
        - Le estoy diciendo a mi servidor que cuando alguien entre a la ruta '/' (la ruta principal), ejecute la función que viene a continuación.
        - Determina la ruta y el método.
        - Arrancan con '@' siempre.

15) Estructura del Proyecto Flask:

    - La estructura de un proyecto Flask es muy simple. Flask no impone una estructura de proyecto, pero sí sugiere una. La estructura sugerida es la siguiente:

    Flask (carpeta):
    
        • assets (carpeta): Acá irían todos los recursos extra (logo, styles, icon, img, data, etc).

        • app.py (archivo): es el archivo principal de la aplicación. En él se crea la aplicación Flask y se definen las rutas. Acá tenemos los endpoints (rutas) de mi API.   

        • templates (carpeta): es el directorio donde vamos a tener todas las plantillas HTML de mi aplicación. No están estáticas esas pantallas, sino que son dinámicas.

        • static (carpeta): es el directorio donde vamos a tener los estilos de esas pantallas. Dentro de static voy a tener otra carpeta que se llame css y ahí voy a tener todo.

            • css (carpeta)

16) Tres tecnologías básicas de una API:

    a) HTML:

        - Para presentar los datos provenientes del servidor del lado del cliente, se utiliza HTML, que no es un lenguaje de programación, sino más bien un sitema de eqtiqueas que está pensado para mostrar contenido.
        - HTML es un acrónimo de Hyper Text Markup Language, o lo que es lo mismo, Lenguaje de Marcado de Hyper Texto. El Hyper Texto tampoco es sólo texto… Entre los elementos del hiper texto podemos encontrar videos, imágenes, sonidos, etc.
        - Es un "texto con hormonas".
        - Nos va a permitir mandar información a partir del protocolo HTTP.
        - Lenguaje basado en etiquetas.
        - Me da la estructura básica sobre la que voy a renderizar la interfaz gráfica.

            Un documento HTML está formado por partes o etiquetas de distintos tipos:

                • Una línea que contiene información sobre la versión de HTML (no siempre),

                • Una cabecera (delimitada por el elemento HEAD). <head></head> --> Todo lo que no se ve, pero me ayuda a renderizar la página. Está toda la metadata de la página.

                • Un cuerpo, con el contenido del documento (delimitado por el elemento BODY). <body></body> --> Todo lo que se ve. Va a ir todo lo que quiero mostrar.

            Y todo el documento tiene que ir entre las etiquetas <html></html> e inicia con la etiqueta <!DOCTYPE html>

            
        Listado de etiquetas:

        <p> "texto" </p> --> párrafo
        <h1> "texto" </h1> --> título
        <a href="https://www.google.com.ar/"> "texto" </a> --> etiqueta para agregar enlaces
        <img src="https://www.google.com.ar/"> --> etiqueta para agregar imágenes
        <br> --> salto de línea
        <div> "texto" </div> --> div
        <ul> "texto" </ul> --> lista desordenada
        <ol> "texto" </ol> --> lista ordenada
        <li> "texto" </li> --> elemento de lista
        <table> "texto" </table> --> tabla
        <tr> "texto" </tr> --> fila
        <td> "texto" </td> --> columna
        <span> </span> == <div> </div>
        <iframe> </iframe> --> Sirve para embeber posts o videos --> Son difíciles de pisar (el estilo).
        <i> </i> --> Sirve para embeber íconos (favicons) --> formato .svg
        <style> </style> --> me permite agregar código CSS adentro de HTML


        • Etiquetas semánticas --> permite tener un código más mantenible.

    b) CSS:

        - CSS es un lenguaje de diseño gráfico para definir y crear la presentación de un documento estructurado escrito en un lenguaje de marcado. Es muy usado para establecer el diseño visual de los documentos web, e interfaces de usuario escritas en HTML o XHTML.
        - Decora y/o maquilla la base que puso HTML.
        - Todo lo que sea con estilos, se hace con CSS.
        - NO se prorgama código CSS adentro de HTML.
        - No opera contra el sistema operativo.
        - Etiqueta → <link rel="stylesheet" href="style.css"> --> nos permite linkear el HTML con los archivos CSS(estilos), por lo tanto irá en el head porque es algo que no se debe ver.
        - El codigo CSS se escribe entre {} y hace referencia a varios elementos del HTML.
        - Sintáxis: elemento { color : blue}
        - Al elemento lo voy a referenciar con el 'elemento' o con el 'class name'

    c) JavaScript:

        - Es un lenguaje de programación que me permite hacer lógica de programación.
        - Es lo dinámico sobre las estructuras maquilladas y/o decoradas. ('No puedo decirle a Alexa, abrime la puerta si no tengo puerta')

x) Adicionales:

    • Request --> pedido. La biblioteca 'requests' me permite hacer pedidos en Python.
    • JSON --> es como una estructura de diccionarios, que tiene sus 'keys' y sus 'values'.
    • Puerto -->  * Running on http://127.0.0.1:5000 --> En este caso estamos escuchando a la aplicación mediante el puerto '5000'.
    • Status code --> El status_code de esta operación fue '403' --> me dice como funcionó esa conexión. https://http.cat/
    • Las páginas web se renderizan en el navegador.
    • Hacer "HOVER" --> pasar por arriba del elemento
"""