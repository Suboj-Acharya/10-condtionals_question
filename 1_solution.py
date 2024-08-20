# classifying a person based on age
# <13 child , 13-20 teenager , 20-60 adult , >60 senior citizen
user_age=int(input("Enter your age: "))
if (user_age < 13):
    print("Chlid")
elif (user_age < 20):
    print("Teenager")
elif (user_age < 60):
    print("Adult")
else:
    print("Senior Citizen")