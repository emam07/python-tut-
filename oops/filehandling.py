'''file=open('pp4.py','r')
content=file.write()
print(content)

file.close()
'''



file1 =open('text/files.txt','w')
content1= input("Enter the data here")

file1.write(content1)

print("Data added successfully")

file1.close()