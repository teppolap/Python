# Tee funktio calc_consumption. Sinne viedään parametreina:

# auton kulutus litraa/100km
# polttoaineen hinta euroa per litra

# kuljettu matka kilometreinä.
#   calc_consumption-funktio palauttaa tietoina kuinka monta litraa polttoainetta on kulunut matkalla,
#   sekä polttoaineeseen kuluneen rahan määrän. Kysy käyttäjältä: kulutus, polttoaineen hinta ja kuljettu matka. 
#   Sen jälkeen kutsu calc_consumption-funktiota ohjelmasta. 
#   Tarkista että funktio laskee kulutuksen ja polttoaineen hinnan oikein.

trip_lenght = float(input("Enter trip length in km:"))
fuel_price = float(input("Enter fuel price/liter:"))
fuel_consumption = float(input("Enter fuel consumption/100 km:"))


def calc_consumption(trip_lenght, fuel_price, fuel_consumption):
    fuel = trip_lenght * fuel_consumption/100
    cost = fuel * fuel_price
    return fuel, cost


fuel_used, fuel_cost = calc_consumption(trip_lenght, fuel_price, fuel_consumption)
print("Fuel: ", "%.2f" % fuel_used,"liter")
print("Cost: ","%.2f" % fuel_cost,"€")