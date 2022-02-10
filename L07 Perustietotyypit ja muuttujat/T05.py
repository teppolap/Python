bank_balance = 2000
print("Bank account balance:", bank_balance, "€")
euros_to_add = input("How many euros will be added to the balance? ")
cents_to_add = input("How many cents will be added to the balance? ")
bank_balance = int(bank_balance) +  int(euros_to_add) +  int(cents_to_add)/100
print("Bank account balance:", bank_balance, "€")