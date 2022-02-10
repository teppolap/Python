#   Tee ohjelma, joka kysyy oppilaitten nimiä niin kauan kunnes käyttäjä antaa tyhjän syötteen. 
#   Ohjelma kertoo tämän jälkeen montako nimeä annettiin ja näyttää ne yhtenä rivinä pilkulla erotettuna.
#   Esimerkkiajo:
#   Enter student name:Minna
#   Enter student name:Matti
#   Enter student name:Kirsi
#   Enter student name:Arto
#   Enter student name:
#   Student count: 4
#   Minna, Matti, Kirsi, Arto
# Tekijä: Teppo Lappalainen


laskuri = 0 # Laskuri laskee syötettyjen nimien määrän
nimet = '' # tähän merkkijonoon kasataa kaikki syötetyt nimet pilkulla erotettuna

while True: 
    nimi = input("Enter student name:")
    if nimi == "":
        break
    if laskuri > 0:
        nimet += ', '

    laskuri += 1
    nimet += nimi


print("Student count:", laskuri)
print(nimet)
