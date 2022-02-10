# Toteuta funktio isthiszero(num). Funktiolla välitetään yksi parametri. Funktio palauttaa true jos parametrin arvo on nolla. 
# Funktio palauttaa false, jos parametri on luku mutta ei nolla. Funktio nostaa TypeError-poikkeuksen, jos parametri ei ole luku. 
# Kokeile kutsua  ohjelmasta funktioita eri arvoilla. Toteuta kutsuvalla ohjelmalle try - except. Mitä havaitset? 
# Vastaukset tehtävän alkuun kommentteina.
# Tekijä: Teppo Lappalainen

#Vastaus: Ohjelma ei enään tunnista lopussa antamaani parametriä number kun laitoin expect ValueError

try:
    number = int(input("Anna arvo: "))
except ValueError:
    def isthiszero(number):
        if number == 0:
            print("True")
        else:
            print("false")
        return number
    isthiszero(number)