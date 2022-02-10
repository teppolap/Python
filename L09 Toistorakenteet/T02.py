# tekijä: Teppo Lappalainen
#  Tee ohjelma, joka kysyy käyttäjältä kokonaislukuja. Lukuja kysytään siihen saakka kunnes käyttäjä antaa tyhjän syötteen. 
# Laske kuinka monta lukua käyttäjä antoi, laske myös annettujen lukujen summa. Näytä annettujen lukujen lukumäärä ja summa käyttäjälle.
# Esimerkkiajo:
# Anna luku: 1
# Anna luku: 2
# Anna luku: 5
# Anna luku:
# Lukuja annettu: 3
# Lukujen summa: 8

kpl = 0
sum = 0
while True: 
    luku = input("Anna luku: ")
    if luku == "":
        break 
    sum += int(luku)
    kpl += 1
print("Lukuja annettu:",kpl)
print("Lukujen summa:",sum)