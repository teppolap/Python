# Kuvaus:
#   Tee funktiot: celToFah ja fahToCel
#   Funktiot ottavat parametrikseen asteluvun ja muuttavat sen joko fahrenheitit celsiuksiksi tai celsius-asteet fahrenheitiksi.
#   Muutettu astearvo palautetaan yhden desimaalin tarkkuudella.
#   Testaa kumpikin funktio kutsumalla sitä käyttäjän antamilla luvuilla.
#   Esimerkiksi testi print(celToFah(10.0)) palauttaa arvon 50.0
# Tekijä: Teppo Lappalainen

# def CelToFah(asteet):

#     vastaus = (asteet * 1.8) + 32
#     vastaus = round(vastaus, 1)
#     return vastaus

# def FahToCel(asteet):

#     vastaus = (asteet - 32)/1.8
#     vastaus = round(vastaus, 1)
#     return vastaus

# syote = float(input("Anna luku: "))
# fah = CelToFah(syote)
# cel = FahToCel(syote)
# print(fah)
# print(cel)

def celToFah(asteet):
    return round(asteet *1.8 + 32, 1)

def fahToCel(asteet):
    return round((asteet - 32) / 1.8, 1)

print(celToFah(10.0))
print(fahToCel(50.0))