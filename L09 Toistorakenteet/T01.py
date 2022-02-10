# tekijä: Teppo Lappalainen
# Tee ohjelma, joka kysyy käyttäjältä viikon kunkin päivän sademäärän. Sademäärä annetaan kokonaislukuna, 
# jollei kyseisenä päivänä ole satanut käyttäjä antaa luvuksi 0. Laske ja näytä viikon kokonaissademäärä.
# Esimerkkiajo:
# Insert number (rainfall): 1  
# Insert number (rainfall): 3  
# Insert number (rainfall): 5  
# Insert number (rainfall): 0  
# Insert number (rainfall): 0  
# Insert number (rainfall): 1  
# Insert number (rainfall): 5  
# Rainfall sum is 15  

sum = 0
for i in range(7):
    sade = int(input("Insert number (rainfall): "))
    sum += sade 
    continue
print("Rainfall sum is ", sum)