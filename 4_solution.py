# checking ripeness of fruit
fruit="Banana"
color=input("Enter fruit color: ")
color=color.capitalize()
if (color == "Green"):
    print("Banana is Unripe")
elif (color == "Yellow"):
    print("Banana is Ripe")
elif (color == "Brown"):
    print("Banana is Overripe")