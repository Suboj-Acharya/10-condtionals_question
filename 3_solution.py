# grade calculator
#90 -100(A),80-89(B),70-79(C),60-69(D),<60(F)
your_score=int(input("Enter your score: "))
if (your_score <= 100):
    if (your_score >= 90):
        print("Your grade is \"A\"")
    elif (your_score >= 80):
        print("Your grade is \"B\"")
    elif (your_score >= 70):
        print("Your grade is \"C\"")
    elif (your_score >= 60):
        print("Your grade is \"D\"")
    else:
        print("Your grade is \"F\"")
else:
    print("Try again")        