# Tee ohjelma, joka kysyy käyttäjältä käyttäjän etu ja sukunimen. Tulosta käyttäjän etunimen ensimmäistä kirjainta niin monta kertaa kun etunimessä on kirjaimia. 
# Tämän jälkeen tulosta käyttäjän sukunimi käänteisessä järjestyksessä.
# Siis esimerkiksi jos käyttäjä antaa etunimekseen 'Kirsi' ja sukunimeksi 'Kernell' suoritus olisi:
# Anna etunimi: Kirsi
# Anna sukunimi: Kernel
# KKKKK lenreK

from typing import Text

etunimi = str(input("Anna etunimi: "))
sukunimi = str(input("Anna sukunimi: "))
a = etunimi[0]

etunimi_kirjain = len(etunimi) * a
print(etunimi_kirjain, sukunimi[:: -1])
