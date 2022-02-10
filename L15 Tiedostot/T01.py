# Tehtävä L15T01 (2 pistettä)
# Tee ohjelma, joka kysyy käyttäjältä henkilöiden sukunimiä ja kirjoita käyttäjän antamat nimet tiedostoon (lopetusehdon voit päättää itse).
# Avaa tämän jälkeen tiedosto lukemista varten ja tulosta konsoliin tiedoston sisältö riveittäin.
# Huomioi mahdolliset poikkeukset, joita tiedoston käsittely voi aiheuttaa.
# Tekijä: Teppo Lappalainen

file = open ("sukunimet.txt", "w")


while True:
    sukunimi = input("Anna sukunimi: ")
    if sukunimi == "":
        break
    file.write(sukunimi + "\n")                    

file.close()

lines = []
file = open ("sukunimet.txt", "r")

lines = file.readlines()

for line in lines:
    print(line.split())