# Tee ohjelma joka kysyy käyttäjältä kurssien arvosanoja (arvosana on kokonaisuluku 0,1,2,3,4 tai 5) ja tallentaa ne listaan. 
# Käyttäjä voi syöttää niin monta kurssiarvosanaa kuin haluaa, syöttäminen lopetetaan tyhjällä syötteellä.
# Näytä lopuksi montako arvosanaa käyttäjä antoi ja arvosanojen keskiarvo.
# Tekijä: Teppo Lappalainen
# Tehtävä A

list = []
laskuri1 = 0
laskuri2 = 0


while True:
    arvosana = input("Anna arvosana 0, 1, 2, 3, 4 tai 5: ")
    if arvosana == "":
        break
    arvosana = int(arvosana)
    laskuri1 += 1
    list.append(arvosana)
    laskuri2 += arvosana
    
keskiarvo = laskuri2 / laskuri1
print(list)
print("Annettujen arvosanojen määrä: ", laskuri1)
print("Arvosanojen keskiarvo: ", keskiarvo )