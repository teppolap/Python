# Tee kokoelma, jossa on 5 merkkijonoa.
# Kysy käyttäjältä indeksi mihin kohtaan taulukkoa käyttäjä haluaa syöttää uuden tekstin.
# Kysy käyttäjältä uusi teksti ja laita se taulukkoon käyttäjän antamaan indeksiin.
# Tulosta taulukon sisältö.
# Korjaa ohjelma niin ettei se kaadu, jos käyttäjä syöttää indeksin, joka on taulukon ulkopuolella.
# Kerro käyttäjälle mikäli indeksi ei ole kelvollinen ja pyydä syöttämään se uudestaan.
# Tekijä: Teppo Lappalainen

list = [1, 2, 3, 4, 5]
print(list)

while True:
    index = int(input("Mihin kohtaan taulukkoa haluat syottaa uuden numeron:"))
    if index > 0 and index <= 5:
        break
    else: 
        print("Indeksi ei ole kelvollinen")

numero = int(input("Anna korvaava numero: "))

list[index] = numero
print(list)