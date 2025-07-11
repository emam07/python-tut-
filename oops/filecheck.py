import os
folder=input('Enter the folder ')
filename = input("Enter the file to check its there or not ")

filepath= os.path.join(folder,filename)

if os.path.exists(filepath):
    print("exists")
else:
    print("not there")