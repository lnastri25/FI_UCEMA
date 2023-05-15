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
        • El cliente se encarga de presentar (renderizar) la respuesta al usuario final

        b) Servidor (Back-End):
        • El servidor procesa el pedido y responde a esa demanda del cliente. Siempre aporta algo (contenido, datos, etc.)

            - Para que se cumpla esta relación tiene que, sí o sí, haber una comunicación entre Cliente y Servidor. Esta comunicación se hace a través de un protocolo.

    - Esta comunicación ocurre a través de redes Intranets o la misma Internet, empleando un protocolo llamado HTTP, sobre el cuál hablaremos en el punto siguiente.

    - Entonces en la arquitectura web cliente-servidor, los servidores son quienes almacenan y proveen la información o recursos dados, y los clientes son responsables de presentar la información al usuario, empleando tecnologías específicas de la Web.

5) Protocolos de comunicación (HTTP):

    - ¿Alguna vez te preguntaste cómo es que logramos comunicarnos los seres humanos? ¿Cómo es que las palabras pueden estructurarse en conversaciones ordenadas? Bueno, los seres humanos somos capaces de estructurar las palabras, y estas en oraciones que devienen en conversaciones. En este proceso se pone en juego no solo cuestiones ficiológicas, sino también cuestiones culturales y personales, como: la lengua, las normas sociales, los valores culturales, los intereses y propósitos individuales. Por tanto, lo que pensamos como un simple intercambio de palabras, se convierte en una actividad compleja, matizada con el ritmo de todo esta información extra...o meta.

    - Los protocolos, como verás, forman parte de nuestras vidas más de lo que pensábamos. Y estos pueden variar según el entorno en el que nos movemos. Cada ámbito posee sus propias reglas para la comunicación. No nos expresamos de igual modo cuando estamos en un recital, que cuando estamos en la facultad ¿No?

        a) Protocolo:  
        - Este conjunto de reglas de comunicación, implícitas o explícitas, se denomina protocolo y en Internet hay uno específico para establecer la comunicación entre servidores y clientes. 
        - Este protocolo fue creado para la transferencia de archivos hipertextuales y se llama justamente HTTP, por las siglas en inglés de protocolo de transferencia de hipertexto (HyperText Transfer Protocol).

        - Este protocolo de comunicación empleado en la Web tiene ciertas características que debemos tener en cuenta:

            • Pedido-Respuesta: se abre una conexión por cada pedido, que surge del cliente, y el servidor la cierra cuando ha enviado la respuesta

            • Stateless: el protocolo per-sé no maneja ninguna noción de memoria de pedidos anteriores

            • Textual: se intercambian mensajes de sólo texto



"""