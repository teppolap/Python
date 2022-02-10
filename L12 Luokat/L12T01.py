# Tehtävä L12T01 (2 pistettä)
# Tee luokka Human. Luokalla on kaksi ominaisuutta name ja age. Kirjoita Human-luokka seuraavasti:
# Konstruktori alustaa Human-olion nimen ja iän parametrien kautta.
# Luokan str metodi toimii kuten on alla esitetty
# Luo kaksi Human-luokan oliota seuraavilla tiedoilla:
# Nimi: Adam, Ikä: 18
# Nimi: Eva, Ikä: 18
# tekijä: Teppo Lappalainen

from human import *

hlo1 = Human ("Adam ", 18)
hlo2 = Human ("Eva ", 18)
print(hlo1)
print(hlo2)