# Tee ohjelma, jossa yrität muuttaa listan sellaista arvoa, jota ei ole olemassa. 
# Alusta siis lista, jossa on neljä elementtiä ja sen jälkeen yritä muuttaa viidettä elementtiä. 
# Tarkista millaisen poikkeuksen saat. Korjaa ohjelma niin ettei se kaadu.
# Tekijä: Teppo Lappalainen

try:
    numbers = [ 1, 2, 3, 4]
    print("Last number is ", numbers[5])
except IndexError:
    print("Wrong index used in accessing list")

