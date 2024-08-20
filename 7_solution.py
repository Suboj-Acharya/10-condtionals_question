# Coffee customization
coffee_size=input("Enter coffee size you prefer: ")
coffee_size=coffee_size.capitalize()
extrashot=(input("Do you want extrashot ? .\nType \"True\" if yes and \"False\" if no: "))
extrashot=extrashot.capitalize()
if (extrashot == "True"):
    coffee=coffee_size +" coffee with an extrashot of espresso"
else:
    coffee=coffee_size+" coffee only"
    
print(coffee)