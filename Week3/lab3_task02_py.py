#password policy validator code

allowed_symbols = "!@#$%"
while True:
    password = input("Enter your password:")

#add password rules 
    has_min_length = len(password) >= 10
    has_uppercase = any(c.isupper() for c in password)
    has_lowercase = any(c.islower() for c in password)
    has_two_digits = sum(c.isdigit() for c in password)>=2
    has_symbol = any(c in allowed_symbols for c in password)
    has_no_spaces = " " not in password

    if(has_min_length and has_uppercase and has_lowercase
        and has_two_digits and has_symbol and has_no_spaces):
        print("Password has been accepted")
        break
    else:
        print("Password does not meet the criteria.Please try again.")
        if not has_min_length:
            print("Password must be at least 10 characters long.")  
        if not has_uppercase:
            print("Password must contain at least one uppercase letter.")
        if not has_lowercase:
            print("Password must contain at least one lowercase letter.")
        if not has_two_digits:
            print("Password must contain at least two digits.")
        if not has_symbol:
            print("Password must contain at least one symbol from the following: !,@,#,$,%)")
        if not has_no_spaces:
            print("Password must not contain spaces.")
            
