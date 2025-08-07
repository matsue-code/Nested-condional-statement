print("select your ride:")
print("1. Bike")
print("2. Car")
choice = int(input("enter your choice: "))
if(choice == 1):
    print("whats type of bike?")
    print("1.scooty\n")
    print("2.scooter\n")
    choice2=int(input("enter your choice2:" ))
    if choice2==1:
     print("you have select scooty")
    else:
       print("you have selected scooter")
elif(choice==2):
   print("what type of car")
   print("1. sedan")
   print("2.suv")
   choice3=int(input("enter your choice3: "))
   if choice3==1:
      print("you have selected a sedan")
   else:
      print("you have selected an suv")
else:
   print("wrong choice")

   

