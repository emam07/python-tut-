email= str(input("Enter your email"))

if '@' in email:
    print("valid email",email)
else:
    print("invalid email",email)


print(email.upper())
print(email.lower())


name=input("enter ur name ").capitalize()
print(name)