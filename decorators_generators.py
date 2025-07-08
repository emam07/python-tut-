'''these are added inside a funtion to add extra feautures to the main funtion without changing the main function


def greet(func):
    print("Hii there how are u")
    func()
    def wrapper():
        print("I hope u are doing fine")
    return wrapper

@greet 
def say_hello():
    print("hellooo")
say_hello()

'''


def count_down(num):
    while num>0:
        yield num
        num -=1
    
for number in count_down(7):
    print(number)