#Pet food reccomendation
pet=input("Enter your pet species: ")
age=int(input("Enter your pet age: "))
pet=pet.capitalize()
if (pet == "Dog"):
    if (age < 2):
        print("Give puppy food. ")
    else:
        print("Give dog food. ")    
if (pet == "Cat"):
    if (age > 5):
        print("Give senior cat food. ")
    else:
        print("Give kitten food. ")    