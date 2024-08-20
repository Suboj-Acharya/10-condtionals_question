# Transportation Mode Selection
#<3 walk ,3-15 take bike ,> 15 take car
distance=int(input("Enter distance between you and the destination: "))
if(distance < 3):
    print("Take a walk")
elif(distance <= 15):
    print("Take Bike")
elif(distance > 15):
    print("Take Car")