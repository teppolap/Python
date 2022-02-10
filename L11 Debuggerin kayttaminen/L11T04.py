# Mäkihypyssä käytetään viittä arvostelutuomaria. Kirjoita ohjelma, joka kysyy arvostelupisteet yhdelle hypylle ja tulostaa tyylipisteiden summan siten, 
# että summasta on vähennetty pois pienin ja suurin tyylipiste.
# Esimerkkitoiminta:
# Give points:19
# Give points:20
# Give points:18
# Give points:16
# Give points:20
# Total points are: 57
# Tekijä: Teppo Lappalainen


points = []

for i in range(5):
    score = int(input("Give points:"))
    points.append(score)

smallest = points[0]
biggest = points[0]

for i in points:
    if i < smallest:
        smallest = i
    if i > biggest:
        biggest = i

points.remove(smallest)
points.remove(biggest)

summa = 0

for score in points:
    summa += score
print("total points are:", summa)