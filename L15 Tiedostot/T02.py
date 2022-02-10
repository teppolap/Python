# Tehtävä L15T02 (2 pistettä)
# Luo jollakin editorilla (esim Notepadilla) tekstitiedosto 'nimet.txt', johon lisäät vähintään kymmenen naisten ja kymmenen miesten etunimeä.
# Tee ohjelma, joka lukee em. tekstitiedostosta nimet ja kertoo montako nimeä löytyy ja montako kertaa kukin nimi esiintyy.
# Huomioi myös muut mahdolliset poikkeukset joita tiedoston käsittely voi aiheuttaa.
# Tekijä: Teppo Lappalainen

lines = []
nimet = {"tyhja": 0}
file = open ("nimet.txt", "r")

lines = file.readlines()


for line in lines:
    nimet[str(line.split())] = 0

for line in lines:
    nimet[str(line.split())] += 1

nimet.pop("tyhja")

print("Kaikki rivit yhtensä: " + str(lines.__len__()))
print("Kaikki samanlaiset nimirivit poistettu: " + str(nimet.__len__()))
print(nimet)