# movie ticket pricing
# 12 FOR ADULTS(18 OR ABOVE) AND 8 For Child,2 dollars discount every wednesday
user_age=int(input("Enter your age: "))
day=input("Today's Day: ")
if (user_age >= 18):
    price=12
    if (day.upper() =="WEDNESDAY"):
        price=price-2
else:
    price=8
    if (day.upper() =="WEDNESDAY"):
        price=price-2
print(f"Your ticket bill is {price} dollars")        