"https://mumuki.io/fundamentos-informatica-ucema/chapters/682-programacion-con-objetos" # --> Mumuki

# Por suerte el equipo de sobrevivientes pudo frenar el apocalipsis zombi. El problema es que quedaron con hambre, ¡solucionémoslo!

# Para ello cambiemos de escenario y vayamos a un restaurante . En este peculiar restaurante de comida italiana se dan algunos conflictos porque al equipo de chefs les gusta mucho lo picante y a sus ayudantes no tanto. 

## Del equipo de cocina sabemos que:

# cada chef tiene un atributo plato_del_dia;
# las instancias de Chef pueden picantear ese plato solo si no está demasiado picante, en caso de estarlo arrojan una excepción que dice El plato ya está demasiado picante;
# las instancias de AyudanteDeCocina no tienen atributos ya que pueden suavizar cualquier plato que reciban como argumento.

## Mientras que de los platos podemos contar lo siguiente:

# las Pastas tienen un atributo ajies que inicialmente es 0;
# están demasiado picantes cuando tienen más de 10 ajies;
# al ser picanteadas aumenta en 5 su cantidad de ajies y al ser suavizadas pierden 1. No te preocupes por si al suavizar queda una cantidad negativa de ajies, no vamos a considerar ese escenario;
# las Pizzas tienen condimento que inicialmente es "adobo";
# se considera que una pizza está demasiado picante si su condimento es "cayena";
# al suavizar una pizza su condimento pasa a ser "orégano" y al picantearla, "cayena".
# Los constructores en ambos platos solo deben tener self como parámetro porque sus atributos siempre se inicializan con el mismo valor. 

# Definí las clases necesarias para poder hacer lo siguiente:

class Chef:
    def __init__(self, plato):
        self.plato_del_dia = plato
    
    def picantear(self):
        if isinstance(self.plato_del_dia, Pasta):
            if self.plato_del_dia.ajies <= 10:
                self.plato_del_dia.ajies += 5
                return self.plato_del_dia
            else:
                raise Exception("El plato ya está demasiado picante")
        else:
            self.plato_del_dia.condimento = "cayena"
            return self.plato_del_dia
          
# isinstance se utiliza para comprobar si un objeto es una instancia de la clase Pasta o de la clase Pizza. 
# Esto es útil en los métodos picantear y suavizar de las clases Chef y AyudanteDeCocina, respectivamente, 
# ya que cada uno de estos métodos requiere diferentes acciones en función del tipo de plato que se está manipulando. 
# Si el objeto es una instancia de la clase Pasta, entonces se puede aumentar o disminuir la cantidad de ajíes. 
# Si es una instancia de la clase Pizza, entonces se puede cambiar el condimento.

class Chef:
  def __init__ (self, plato_del_dia):
    self.plato_del_dia = plato_del_dia
  
  def picantear (self):
    if self.plato_del_dia.muy_picante():
      raise Exception ("El plato ya está demasiado picante")
    else:
      self.plato_del_dia.picante()

    
class AyudanteDeCocina:
  def suavizar (self, plato):
    plato.suavizar()
    
class Pizza:
  def __init__ (self):
    self.condimento = "adobo"

  def muy_picante (self):
    return self.condimento == "cayena"
    
  def suavizar(self):
    self.condimento = "orégano"
    
  
  def picante(self):
    self.condimento = "cayena"
    
class Pasta:
  def __init__ (self):
    self.ajies = 0
   
  def muy_picante (self):
    return self.ajies > 10
    
  def picante(self):
      self.ajies += 5
  
  def suavizar(self):
      self.ajies -= 1
        
"""

fideos = Pasta()
muzzarella = Pizza()
jor = Chef(fideos)
luchi = AyudanteDeCocina()
jor.picantear()
luchi.suavizar(fideos)
jor.plato_del_dia = muzzarella
luchi.suavizar(muzzarella)
jor.picantear()

"""

# ¡Dame una pista!
# Al definir las clases Pasta y Pizza tenés la libertad de elegir cómo hacer para picantear, suavizar o saber si están demasiado picantes. ¡Pero recordá que es importante delegar adecuadamente! 

## ---------- ## 

# Antes de pasar al siguiente dominio, deberíamos dar el alta a los animales, para que vuelvan a su rutina habitual. 

# Para poder recibir el alta, el animal tiene que estar feliz. Sabemos que:

# los gatos están felices si tienen más de 30 de energia;
# los caballos siempre están felices;
# las golondrinas solo están felices cuando están en "Lihuel Calel".
#Definí en la clase EstudianteDeVeterinaria el método puede_dar_el_alta que reciba a un animal como argumento y nos indique si cumple los requisitos. 
# Para poder saber eso también es necesario que definas el método esta_feliz en cada clase de animal.

# ¡Dame una pista!
# No te olvides del return en el método puede_dar_el_alta. 

class EstudianteDeVeterinaria:
    def alimentar(self, animal, cantidad_gramos):
        animal.comer(cantidad_gramos)
        
    def rehabilitar(self, animal):
        animal.recibir_rehabilitacion()
        
    def puede_dar_el_alta(self,animal):
        return animal.esta_feliz() # Le estamos dando un mensaje al objeto.
        
    
class Gato:
  def __init__(self,una_energia, una_edad):
    self.energia = una_energia
    self.edad = una_edad

  def comer(self,gramos):
    self.energia += gramos

  def cumplir_anios(self):
    self.edad += 1
    
  def recibir_rehabilitacion(self):
    self.comer(400)
    
  def esta_feliz(self):
    return self.energia > 30
    
class Caballo:
  def __init__(self,una_energia, una_raza):
    self.energia = una_energia
    self.raza = una_raza

  def comer(self,gramos):
    self.energia += gramos * 2

  def galopar(self,kms):
    self.energia -= kms
    
  def recibir_rehabilitacion(self):
    self.galopar(3)
    self.comer(3000)
    self.galopar(5)
    
  def esta_feliz(self):
    return True

class Golondrina:
  def __init__(self,una_energia, una_ciudad):
    self.energia = una_energia
    self.ciudad = una_ciudad

  def comer(self,gramos):
    self.energia += gramos / 2

  def volar_hacia(self,destino):
    self.ciudad = destino
    self.energia /=  2 
    
  def recibir_rehabilitacion(self):
    self.volar_hacia("Lihuel Calel")
    
  def esta_feliz(self):
    return self.ciudad == "Lihuel Calel"