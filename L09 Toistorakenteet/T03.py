#Tekijä: Teppo Lappalainen
#  Tee ohjelma, joka kysyy ensin käyttäjältä jonkin luvun väliltä 1-10.
# Tämän jälkeen näytä luvut yhdestä annettuun lukuun ja luvun neliön.
# Esimerkiksi jos käyttäjä antaa luvun 5:
# Anna numero väliltä 1-10: 5
# Luvun 1 neliö on 1
# Luvun 2 neliö on 4
# Luvun 3 neliö on 9
# Luvun 4 neliö on 16
# Luvun 5 neliö on 25

while True:
    number = int(input("Anna numero väliltä 1-10: "))
    if number > 0 and number <= 10:
        break

for i in range(1,number+1):
    print("Luvun {} neliö on {}".format(i, i*i))
