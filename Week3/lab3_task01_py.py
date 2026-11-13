#ask user to enter password
password = input("Enter your password")
print("Password length:", len(password))

#check uppercase letters, lowercase letters. numbers, symbols
uppercase = 0 
lowercase = 0 
numbers = 0 
symbols = 0 

for char in password:
    if char.isupper():
        uppercase += 1
    elif char.islower():
        lowercase +=1
    elif char.isdigit():
        numbers +=1
    else: symbols +=1
print("Uppercase:", uppercase) 
print ("Lowercase:", lowercase) 
print("Numbers:", numbers) 
print("Symbols:", symbols)

