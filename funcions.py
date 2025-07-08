'''here we will learn about the funcion what is it how is it how to declare it
block of code performing a particulaR task
reusable 
combacks on calling

three types of arguments 

positional = def greet (name ,city):
    print(f"hii {name} to {city}")
greet ("Raju","mumbai")

keyword= def greet1 (name ,city):
    print(f"hii {name} to {city}")

greet1(name="raju",city="mumbai")'''

 


def greet():
    print("hii" + " black clover")

greet()

def name (names):
    print("Hii",names)
name("ankit")



def get_full_name (first,last):
    full_name=f'{first} {last}'
    return full_name
name=get_full_name("Raju", "singh")

print(name)
