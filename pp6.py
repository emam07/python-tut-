'''break statement use case'''

for i in range (1,10):
    if(i==7):
        break
print ("break works fine ", i)
'''continue statement use case'''
for i in range (1,10):
    if(i==6):
        continue
    print(i)
'''simply pass to the next iteration and just so that u can replace it with break or continue in future
'''
for num in range(1,10):
    if(num==4):
        pass
print("will be done tomorrow",num) 