num = int(input("Enter the range"))
num2= int(input("Enter the no. to skip"))

lists=[]

if num2%2==0:
    print("even no")
else:
    print("odd no")
for i in range(num):
    if(i%2==0):
        lists.append(i)
    else:
        print(f"The possible odd no. in range {num} is {i}")
print(f"The possible even no. in range {num} is {lists}")


for i in range(num):
    if (i==num2):
        continue
    print(i)
