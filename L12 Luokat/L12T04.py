# Tee edellisen tehtävän Car-luokkaa apuna käyttäen seuraava: luo satunnaisesti vähintään viisi erilaista auto-oliota seuraavista automerkeistä
# (brand) 'Audi', 'BMW', 'Ford', 'Opel', 'Skoda', 'Volvo' ja 'VW'. Autojen model-ominaisuuden voit jättää halutessasi tyhjäksi. 
# Generoi satunnaisesti niille hinta väliltä 1000-10000. Lisää luodut auto-oliot cars-nimiseen list-rakenteeseen. 
# Huom! Käytä apuna randint-funktiota satunnaisuuden toteuttamisessa.
# tekijä: Teppo Lappalainen


from random import *

class Car:
  def __init__(self, brand, model, price):
    self.brand = brand
    self.model = model
    self.price = price

  def __str__(self):
    return self.brand + " " + self.model + " " + str(self.price)


car_brands = ['Audi', 'BMW', 'Ford', 'Opel', 'Skoda', 'Volvo', 'VW']
cars = []

for i in range(5):
    rand = randint(0, len(car_brands) - 1)
    brand = car_brands[rand]
    cars.append(Car(brand, "", randint(1000, 10000)))