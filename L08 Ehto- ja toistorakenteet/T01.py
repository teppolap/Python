# Tehtävä L08T01 (2 pistettä)
#Tekijä: Teppo Lappalainen
# Tee ohjelma jossa kysytään käyttäjältä tämän ikä.

# jos ikä on alle 13 vuotta, tulosta "child"
# jos ikä on 13-19 vuotta, tulosta "teen"
# jos se on 20-65 vuotta, tulosta "adult"
# muussa tapauksessa tulosta "senior".

# Huom: yksikkötestiä varten sinun tulee tehdä tehtävä funktiolla!
# Tee funktio kerro3() joka kertoo käyttäjästä  tämän iän perusteella seuraavaa:

# jos ikä on alle 13 vuotta, palauta "child"
# jos ikä on 13-19 vuotta, palauta "teen"
# jos se on 20-65 vuotta, palauta "adult"
# muussa tapauksessa palauta "senior"


def kerro3(ika):
    tulos = "unknown"
    if ika < 13:
        tulos = ("child")
    elif ika < 20:
        tulos = ("teen")
    elif ika < 66:
        tulos = ("adult")
    else :
        tulos = ("senior")

    return tulos
print(kerro3(25))