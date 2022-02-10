# Tee funktio time, joka muuttaa parametrinä saadun sekuntiarvon muotoon tunnit:minuutit:sekunnit.
# Esimerkiksi luvulle 10000, palautetaan tieto seuraavassa muodossa "02:46:40"
# Kokeile ohjelmasi toimivuus vähintään viidellä eri arvolla.
# Tekijä: Teppo Lappalainen

def time(sek):
    """ Funktio muuttuu annetun sekunti määrän muotoon tunnit:minuutit:sekunnit

    Parameters
    ----------
    sek : int
        sekunttien määrä, joka halutaan muuttaa tunneiksi, minuuteiksi ja sekunneiksi

    Returns
    -------
    str
        paluuarvona aika merkkijonona

    """
    
    tunnit = int(sek/3600)
    minuutit = (sek - (tunnit*3600))//60
    sekunnit = sek - (tunnit*3600 + minuutit*60)
    paluuarvo = "{:02d}:{:02d}:{:02d}".format(tunnit, minuutit, sekunnit)
    return paluuarvo


print (time(10000))
print (time(61))
print (time(59))
print (time(3601))
print (time(2400))