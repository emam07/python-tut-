'''this is for not using file.close () again and again

with open('text/data.txt','w') as file:
    content=input("Enter the data here ")
    file.write(content)
    print("data saved successfully")

for append now we do and check    


'''
try:
    with open('text/data.txt','a') as file1:
        content1=input("enter the data to append ")
        file1.write(content1)
except ValueError:
    print("enter a string ")

except SyntaxError:
    print("enter valid syntax")
        
print("data saved")