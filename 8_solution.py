# Password checker
# if password<6char (weak) ,6-10 (normal),>10 (strong)
password=input("Enter your password: ")
m=len(password)
if (m <6):
    print("Your password is weak .I recommend you to change your passsword.")
elif (m <= 10):
    print("Your password is normal .")
else:
    print("Your password is strong .")