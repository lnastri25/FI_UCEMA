from aves2 import hipo, chimuelo, maria 


print("Energía antes de entrenamiento", chimuelo.energia(20))
print("Energía antes de entrenamiento", maria.energia)
print(hipo.entrenar_equipo([chimuelo, maria]))
print("Energía luego de entrenamiento", chimuelo.energia)
print("Energía luego de entrenamiento", maria.energia)
print(hipo.entrenamiento_intensivo([chimuelo, maria]))
print(chimuelo.energia)