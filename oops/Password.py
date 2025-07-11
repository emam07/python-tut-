def Check_password(password):
    if len(password)<8:
        raise Exception ("Error password is less than 8 character")
    print("password is strong")

try:
    password = input("Enter the password =")
    Check_password(password)

except Exception as e:
    print(e)

