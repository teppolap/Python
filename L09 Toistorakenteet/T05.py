# Tee funktio lotto(), joka arpoo lottorivin seitsemän (7) numeroa väliltä 1-40 ja palauttaa sen muodossa '1,3,5,10,20,33,39'.  
# Käytä lukujen arpomiseen Pythonin valmista modulia random

import random

def lotto():
  indexes = [(i+1) for i in range(40)]
  numbers = []

  for x in range(7):
    index = random.randrange(0,len(indexes)-1)
    numbers.append(indexes[index])
    indexes.pop(index)
  
  #numbers.sort()
  string = ','.join(str(number) for number in numbers)
  return string
