class Human:

    #määritellään kontruktori
    def __init__ (self, name="", age=0):
        self.name = name
        self.age = age

    #Nimi: Adam, Ikä: 18

    def __str__(self):
        return self.name + str(self.age)

    name = ""
    age = 0
