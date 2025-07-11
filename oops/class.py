'''the class is the blueprint for creating a object, 
an object is the actual thing using the blueprint it is made

'''
class car():
    def start(self):
        print("the car is started and running")
    
    def stop(self):
        print("the car is stopped using brake")


car1=car()

car2=car()

'''car1.start()
car1.stop()

car2.start()
car2.start()'''


class Car():
    def set_details(self, brand, color):
        self.brand= brand
        self.color=color

car1=Car()
car1.set_details("Jeep" ,"Gun Metal")

car2=Car()
car2.set_details("BMW","pink")

print(car1.brand,car1.color)

print(car2.brand,car2.color)