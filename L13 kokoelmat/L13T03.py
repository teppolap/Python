# Toteuta ohjelma, johon voi tallentaa kymmenen eri auton tiedot. 
# Kustakin autosta tiedetään rekisterinumero (esim ABC-123) ja autonmerkki (esim Skoda). Keksi itse erilaisia rekisterinumeroita ja automerkkejä. 
# Tallenna tiedot valitsemaasi kokoelmaan. 
# Tulosta sen jälkeen autojen tiedot ensin aakkosjärjestyksssä automerkin mukaan, ja sen jälkeen aakkosjärjestyksessä rekisterinumeron mukaan.
# Tekijä: Teppo Lapppalainen

list = []

for i in range(10):
    auto = input("Anna auton rekkari ja merkki: ")
    list.append(auto)
    

print(list)
