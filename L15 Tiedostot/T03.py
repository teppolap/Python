# Tehtävä L15T03 (2 pistettä)
# Jatkoa edelliseen. Lajittele nimet aakkosjärjestykseen ennen tulostusta.
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

jnimet = nimet.items()
jarjestetty = sorted(jnimet)
print(jarjestetty)