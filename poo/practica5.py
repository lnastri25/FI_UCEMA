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