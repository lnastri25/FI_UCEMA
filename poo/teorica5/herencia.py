from aves2 import hipo, chimuelo, maria

print("Energia antes de entrenamiento:", chimuelo.energia)
print("Energia antes de entrenamiento:", maria.energia)
print(hipo.entrenar_equipo([chimuelo, maria]))
print("Energia luego del entrenamiento:", chimuelo.energia)
print("Energia luego del entrenamiento:", maria.energia)
print(hipo.entrenamiento_intensivo([chimuelo, maria]))
print(chimuelo.energia)

""""
1) Ahora hacé las modificaciones en las clases Golondrina y Dragones para que un Entrenador pueda entrenar tanto a aves como dragones.

2) Creá una clase de AvesNoVoladoras, que come_alpiste y como su nombre indica no puede volar_en_circulos pero si correr_en_circulos disminuyendo su energía en 25.

3) ¿Las AvesNoVoladoras son polimórficas con las aves Golondrinas desde el punto de vista del Entrenedor?¿Cómo podemos solucionar este inconveniente?
"""