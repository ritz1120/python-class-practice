#ai mood detector
sleephours=int(input("enter sleep hours"))
moodlevel=int(input("enter mood level"))
if sleephours>7 and moodlevel>7:
               print("productive human")
elif sleephours<5:
    print("zombie mode")
else:
    print("need coffee")
#netflix password strength checker
password=int(input("enter your password"))
length=100000000
if password>=length:
    print("access granted")
else:
    print("weak password")
#free fire rank unlock system
level=int(input("enter your level"))
diamonds=int(input("enter your diamonds"))
if level>20 and diamonds>100:
    print("elite pass unlocked")
else:
    print("grind more")
#pizza billing system
print("menu:vegpizza=120,chickenpizza=180,extracheese=+40")
pizza=input("select pizza")
cheese=input("cheese option")
vegpizza=120
chickenpizza=180
extracheese=+40
if pizza==vegpizza and cheese==extracheese:
    print("160")
elif pizza=="chicken pizza" and cheese=="extra cheese":
    print("220")
elif pizza=="veg pizza" and cheese=="no cheese":
    print("120")
elif pizza=="chicken pizza" and cheese=="no cheese":
    print("180")
#lucky number chaos
number=int(input("enter your lucky number"))
if number%3<1 and number%5<1:
    print("fizzbuzz")
elif number%5<1:
    print("buzz")
elif number%3<1:
    print("fizz")
else:
    print("normal human")

    
    
    
                
        
          
  

    
             

