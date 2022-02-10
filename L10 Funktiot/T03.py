# Tee funktio average, jolle viedään 3 parametria. 
# Average funktio palauttaa annettujen parametrien keskiarvon yhden desimaalin tarkkuudella.

def average(number1, number2, number3):
    return round(((number1 + number2 + number3)/3), 1)

number = average(10, 31, 68)
print(number)