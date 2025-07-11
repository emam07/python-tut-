class Birds():
    def sound(self):
        print("Birds chirp")

class Crow(Birds):
    def sound (self):
        print("Caw Caw")

class Monkey(Birds):
    def sound(self):
        print("monkey doesn't sound like birds")


crow=Crow()
monkey=Monkey()
crow.sound()
monkey.sound()
