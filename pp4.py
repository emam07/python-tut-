'''
This program is for taking user input and performing operation based on the input 
simple calculator u can say

'''
num1 = int(input("Enter the number for operation"))
num2 = int(input("Enter the number for operation"))
terms = str(input("Choose the operand +,-,/,* "))

if terms=="+":
    print(num1+num2)

elif terms=="-" and num1>num2:
    print(num1-num2)

elif terms=="*":
    print(num1*num2)

elif terms=="/" :
    print(num1/num2)

else:
    print("Negative value input again")
    print("invalid choice")

