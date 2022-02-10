# Tehtävä L08T03 (1 piste)
# Tee ohjelma joka kysyy käyttäjältä kokonaisluvun.

# jos luku on 10 tai 20, palauta teksti "Luku on 10 tai 20"
# jos luku on 100 tai 200, palauta teksti "Luku on 100 tai 200"
# muuten palauta annettu luku tekstinä.

# Huom: yksikkötestiä varten sinun tulee tehdä tehtävä funktiolla!
# Tee funktio check_int(param1) joka palauttaa parametrina annetun kokonaisluvun perusteella tekstin:


def check_int(num):

    if num == 10 or num == 20:
        output = ("Luku on 10 tai 20")
    elif  num == 100 or num == 200:
        output = "Luku on 100 tai 200"
    else:
        output = str(num)
    

    return output
print(check_int(10))

