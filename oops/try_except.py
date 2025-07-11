'''this is used to catch hold of the run time error in the program which can be avoided '''
try:
    num= int(input("enter the number to divide"))

    result=10/num

    print(f'result :{result}')

except ZeroDivisionError:
    print("you can not divide by 0")

except ValueError:
    print("cannot divide by string")






try:
    file=open('lambda.py')
    content=file.read()
    print(content)

except FileNotFoundError:
    print("File not found")

finally:
    file.close()
    print("file operation complete")