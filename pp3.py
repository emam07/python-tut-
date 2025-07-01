'''conditional statements learning from 
:- if, else, elif, for, while, do while, break, continue.'''
from datetime import datetime, time
now = datetime.now().time()
print(now)
name= str( input("Enter your name:"))
age = int(input ("Enter your age:"))

if(name=="Harry" or name=="James"):
    print(name + " Potter" )
elif name=="Emamul":
    print(name + " Khan")
elif name=="Jhon":
    print(name + " F Kennedy")
else: 
    print(name)
voting_start = time(9, 0)   # 9:00 AM
voting_end = time(18, 0) 
if voting_start > now:
    print("You are early")
elif now >=voting_end:
    print("You are late")

elif age<18 :
    print ("You are underage")

if voting_start<=now <= voting_end and age>=18:
    print("you can cast vote")

else :
    print("Some error occured")

