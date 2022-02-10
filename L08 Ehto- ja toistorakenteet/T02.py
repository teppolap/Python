# Tee ohjelma joka kysyy käyttäjältä 3 kokonaislukua ja tulostaa niistä suurimman.
# Input integer: 2
# Input another integer: 3
# One more: 1
# Max value: 3


Number1 = int(input("Input integer: "))
Number2 = int(input("Input another integer: "))
Number3 = int(input("One more: "))
max_number = max(Number1, Number2, Number3)
print("Max value:", max_number)