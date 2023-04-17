#!/bin/python3

"https://mumuki.io/fundamentos-informatica-ucema/chapters/682-programacion-con-objetos" # --> Mumuki

"https://github.com/AJVelezRueda/Fundamentos_de_informatica/blob/master/POO/Practica/Pr%C3%A1ctica_POO.md" # --> GitHub

## GUÍA 5: PRACTICA POO PARTE 1 ##

# Ejercicio 1 #
# Dada la siguiente clase, identificá la interfaz y el estado de la misma:

class Perro:
    def __init__(self):
        self._alimento = 0
        self._caricias = 0

    def energia(self):
        return self._alimento + (self._caricias * 10)

    def comer(self, gramos):
        self._alimento += gramos

    def acariciar(self):
        self._caricias += 1

    def estaDebil(self):
        return self._caricias < 2
    
    # La interfaz son los metodos que entiende la clase (energia, comer, acariciar, estaDebil) y el estado son los atributos (alimento y caricias)
    
# Ejercicio 2 #
# Modificá el método volar de la clase Golondrina visto en la clase de teoría de manera que no pueda volar si al hacerlo la energía toma el valor 0 o valor negativo.

class Golondrina:
  def __init__(self, energia):
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def volar_en_circulos(self):
    self.volar(0)
    
  def volar(self, kms):
    if (self.energia > 10 + kms):
        self.energia -= 10 + kms
    else:
        print("No tiene la suficiente energia")

  def esta_feliz(self):
    return self.energia > 50

# Ejercicio 3 #
# Creá una clase Notebook cuyo estado sea: marca, modelo y precio, y que tenga un método que le aplique un descuento al precio, el cual tiene que recibir un número entero (el porcentaje de descuento) y tiene que devolver cuánto valdría esa notebook si se aplicase el descuento. Por último hay que instanciar esta clase y en algunos casos aplicar este descuento.

class Notebook:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
    
    def descuento(self, porcentaje):
        return self.precio - (self.precio * porcentaje / 100)
    
    def precio_actual(self):
        print(self.precio)
    
notebook1 = Notebook("Lenovo", "IdeaPad 320", 50000)
notebook1.precio_actual()
notebook1.descuento(50)
notebook1.precio_actual()

# Ejercicio 4 #
# Definí una clase que modele un contador, el cual puede incrementar o disminuir en uno el valor que se ingresa, recordando el valor actual. También puede resetear este valor y al hacerlo se pone en cero. Además es posible indicar directamente un número nuevo que reemplace al valor actual. Este objeto debe entender los siguientes mensajes:

class Contador:
   
    def __init__(self, valor):
        self.valor = valor
    
    def inc(self):
        self.valor += 1
    
    def dis(self):
        self.valor -= 1
    
    def reset(self):
        self.valor = 0
    
    def valorActual(self):
        print(self.valor)
    
    def valorNuevo(self, nuevoValor):
        self.valor = nuevoValor

# inc()
# dis()
# reset()
# valorActual()
# valorNuevo(nuevoValor)
# Como ejemplo el resultado de ejecutar las siguientes líneas tiene que ser 12 y 25.

contador = Contador(10)
contador.inc()
contador.inc()
contador.dis()
contador.inc()
contador.valorActual()
contador.valorNuevo(27)
contador.dis()
contador.dis()
contador.valorActual()

# Ejercicio 5 #
# Modificá el ejercicio anterior de manera que sea capaz de recordar cual fue el último comando que se le dió, en forma de mensaje. Estos mensajes pueden ser: "reset", "incremento", "disminución" o "actualización" (para cuando se coloca un valor nuevo). El método para saber el último comando es ultimoComando, y el resultado de aplicarlo a la serie de comandos dicha en el ejercicio anterior debería ser "disminución".

class Contador:
       
    def __init__(self, valor):
        self.valor = valor
        self.ultimo = ''
    
    def inc(self):
        self.valor += 1
        self.ultimo = 'incremento'
    
    def dis(self):
        self.valor -= 1
        self.ultimo = 'disminucion'
    
    def reset(self):
        self.valor = 0
        self.ultimo = 'reset'
    
    def valorActual(self):
        print(self.valor)
    
    def valorNuevo(self, nuevoValor):
        self.valor = nuevoValor
        self.ultimo = 'actualizacion'
    
    def ultimoComando(self):
        print(self.ultimo)

# Ejercicio 6 #
# Implementá una clase que represente una calculadora sencilla, que permita sumar, restar y multiplicar. Este objeto debe entender los siguientes mensajes:

class Calculadora:

    def __init__(self):
        self.valor = 0
    
    def cargar(self, numero):
        self.valor = numero
    
    def sumar(self, numero):
        self.valor += numero
    
    def restar(self, numero):
        self.valor -= numero
    
    def multiplicar(self, numero):
        self.valor *= numero
    
    def valorActual(self):
        print(self.valor)

# cargar(numero)
# sumar(numero)
# restar(numero)
# multiplicar(numero)
# valorActual()
# Si se evalúa la siguiente secuencia:

calculadora = Calculadora()
calculadora.cargar(0)
calculadora.sumar(4)
calculadora.multiplicar(5)
calculadora.restar(8)
calculadora.multiplicar(2)
calculadora.valorActual()

# el resultado debe ser 24.

# Ejercicio 7 #
# Definí una clase de gorriones, de los cuales nos interesa conocer dos medidas conocidas como CSS (coeficiente de serenidad silenciosa), CSSP y CSSV (como el CSS pero “pico” y “veces”). El CSS resulta de dividir la cantidad total de kilómetros que vuela desde que se lo comienza a estudiar, por la cantidad total de gramos de comida que ingiere. El CSSP es la misma división pero considerando solamente lo que voló la vez que más voló y lo que comió la vez que más comió. El CSSV es otra vez la misma idea, respecto de la cantidad de veces que voló y comió. Si un gorrión nunca comió, los coeficientes deben ser None. Un gorrión se considera en equilibrio si su CSS está entre 0.5 y 2.


"https://github.com/AJVelezRueda/Fundamentos_de_informatica/blob/master/POO/Practica/Pr%C3%A1ctica_Objetos_Parte_2.md"

## GUÍA 5: PRACTICA POO PARTE 2 ##

# Ejercicio 1 #
# Dadas las siguientes clases responder:

# cuales son sus estados

# cuales son sus interfaces

# ¿Comparten interfaz?

# ¿Son polimórficas?

class Perro:
    def __init__(self):
        self.alimento = 0
        self.caricias = 0

    def energia(self):
        return self.alimento + (self.caricias * 10)

    def comer(self, gramos):
        self.alimento += gramos

    def alimento(self):
	    print(self.alimento)

def acariciar(self):
        self.caricias += 1

def estaDebil(self):
        return self._caricias < 2

def pasear(self, km):
	    self.alimento -= km / 4

class Gato:
    def __init__(self):
        self.alimento = 0
        self.caricias = 0

    def energia(self):
        return self.alimento + (self.caricias * 8)

    def comer(self, gramos):
        self.alimento += gramos * 1.5

    def caricias(self):
	    print(self.caricias)

def acariciar(self):
    self.caricias += 1

def estaDebil(self):
    return self._caricias < 4
    
    # Los estados son alimento y caricias.
    # Las interfaces son: energia(), comer(), caricias(), acariciar(), estaDebil() y pasear(). --> los métodos que entienden.
    # Comparten parte de su interfaz. --> Poliformismo parcial.
    # Para decir que son polimorficas necesitamos una tercer clase que use a las 2.
    
# Ejercicio 2 #
# Modificar la clase Golondrina vista en la teoría para poder preguntar si una golondrina está en equilibrio. Este equilibrio se alcanza cuando la energía se encuentra entre 150 y 300.

class Golondrina:
  def __init__(self, energia):
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self, kms):
    self.energia -= 10 + kms

  def esta_feliz(self):
    return self.energia > 50
  
  def esta_en_equilibrio(self):
    return 150 <= self.energia <= 300

# Ejercicio 3 #
# Consideremos que un ornitólogo tiene un conjunto de aves bajo estudio. Cada una de estas aves puede ser un gorrión (del ejercicio 7 de la práctica anterior), o una golondrina. Un ornitólogo somete, cada vez que lo decide, a cada una de las aves que tiene en estudio a una rutina que consiste en: hacerla comer 80 gramos, hacerla volar 70 kms, y finalmente hacerla comer otros 10 gramos. Se propone:

# implementar la clase Ornitologo, de forma tal que acepte las operaciones estudiarAve(ave), avesEnEstudio(), realizarRutinaSobreAves(), avesEnEquilibrio(). Realizar rutina es ejecutar la rutina descripta más arriba sobre cada ave que tiene en estudio. Las aves en equilibrio son aquellas aves, entre las que el ornitólogo tiene en estudio, que responden True cuando se les consulta estaEnEquilibrio().

# comprobar el código que se escribió con esta secuencia:

# definir un ornitólogo, dos golondrinas y dos gorriones,
# inicializar las aves con valores conocidos,
# decirle al ornitólogo que estudie una de las golondrinas y los dos gorriones,
# decirle al ornitólogo que realice su rutina sobre aves,
# verificar los valores de las cuatro aves definidas, para las tres que tiene en estudio el ornitólogo estos valores deberían haber cambiado, para la otra ave no.
    
# Ejercicio 4 #
# Vamos a salir de paseo (¡si la pandemia nos deja!). Para esto podemos utilizar como vehículos motos o autos, y de estos dos medios de transporte sabemos que:

# comienzan con una cantidad que podemos establecer de combustible

# los autos pueden llevar 5 personas como máximo y al recorrer una distancia consumen medio litro de combustible por cada kilómetro recorrido

# las motos pueden llevar 2 personas y consumen un litro por kilómetro recorrido;

# pueden cargar_combustible en la cantidad que digamos y al hacerlo suben su cantidad de combustible

# saben responder si entran una cantidad de personas. Esto sucede cuando esa cantidad es menor o igual al máximo que pueden llevar.

# Definí las clases Moto, Auto y MedioDeTransporte y hace que las dos primeras hereden de la tercera.

class Moto:
    def __init__(self, combustible):
        self.combustible = combustible

    def cargar_combustible(self, litros):
        self.combustible += litros

    def recorrer(self, kms):
        self.combustible -= kms

    def entran(self, personas):
        return personas <= 2
    
class Auto:
    def __init__(self, combustible):
        self.combustible = combustible

    def cargar_combustible(self, litros):
        self.combustible += litros

    def recorrer(self, kms):
        self.combustible -= kms / 2

    def entran(self, personas):
        return personas <= 5
    
class MedioDeTransporte:
    def __init__(self, combustible):
        self.combustible = combustible

    def cargar_combustible(self, litros):
        self.combustible += litros

    def recorrer(self, kms):
        self.combustible -= kms

    def entran(self, personas):
        return personas <= 5