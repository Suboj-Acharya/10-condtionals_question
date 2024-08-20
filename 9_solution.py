#leap year
year=int(input("Enter a year: "))
if (year % 100 == 0):
    if (year % 400 == 0):
        print("Is a leap year")
    else:
        print("Isn't a leap year")  
else:
    if (year % 4 == 0):
        print("Is a leap year")  
    else:
        print("Isn't a leap year")      