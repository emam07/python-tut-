''' automatically run when an object is created'''

class Car():
    def __init__(self ,brand,color):
        self.brand=brand
        self.color=color
    
car1=Car("tesla","red")
print(car1.color)