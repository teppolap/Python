points = int(input("Insert your points: "))
if 0 <= points <= 1: 
    grade = 0
elif 2 <= points <= 3:
    grade = 1
elif 4 <= points <= 5:
    grade = 2
elif 6 <= points <= 7:
    grade = 3
elif 8 <= points <= 9:
    grade = 4
elif 10 <= points <= 12:
    grade = 5 
print("Grade:", grade)  