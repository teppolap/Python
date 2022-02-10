# Toteuta ohjelma, joka kysyy käyttäjältä autojen rekisterinumeroita (siis esim 'ABC-123' jne) ja tallentaa ne listaan. 
# Käyttäjä voi syöttää niin monta rekisterinumeroa kuin haluaa, syöttäminen lopetetaan tyhjällä syötteellä.
# Näytä syötetyt rekisterinumero aakkosjärjestyksessä.
# Tekijä: Teppo Lappalainen

list = []

while True:
    rekkari = input("Anna auton rekkari: ")
    list.append(rekkari)
    if rekkari == "":
        break
list.remove("")
print(list)