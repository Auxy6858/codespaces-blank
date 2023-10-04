Pi = float(3.142)
REPEAT = True
while REPEAT == True:
  Userchoice = input("Do you want to run the program (y/n) ")
  if Userchoice.lower() == "y":
    UserRadius = float(input("What's the radius of the circle?\n"))
    CircleArea = float(UserRadius*UserRadius*Pi)
    print("The area is ", str(CircleArea))
  elif Userchoice.lower() == "n":
    break
  else:
    print("\n")
