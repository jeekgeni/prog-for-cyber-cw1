import random
import string

#create a strong password function 
def validate_password(password):

    #check if a password is at least 10 characters long
    if len(password) < 10:
        return False

    #check that a password contains at least one uppercase letter, one lowercase letter, one digit and one special character
    has_uppercase = any(char.isupper() for char in password)    
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in string.punctuation for char in password)
    has_symbol = any(not char.isalnum() for char in password)

    #return True if all conditions are met, False otherwise                                                                                                                 
    return has_uppercase and has_digit and has_special and has_symbol

#create a valid ip address function
def validate_ip(ip_address):


    #remove unnessecary spaces
    ip_address = ip_address.strip()

    #check if the IP address contains dots 
    if "." not in ip_address:
        return False

    #split the IP address into four parts
    ip_parts = ip_address.split(".")

    #check if there are exactly four sections in the IP address
    if len(ip_parts) != 4:
        return False

    #check each part of the IP address
    for part in ip_parts:

        if not part.isdigit():
            return False

        #convert the part to an integer
        num = int(part)

        #check if the number is between 0 and 255
        if num < 0 or num > 255:
            return False

    #return true if all checks pass
    return True

#create a function to generate a random strong password
def generate_strong_password():

    #choose a random length between 10 and 16 characters
    password_length = random.randint(10, 16)

    #make sure password contains each character type
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)

    ]   
    # Add more random characters to reach chosen length
    characters = string.ascii_letters + string.digits + string.punctuation

    for i in range(password_length - 4):
        password.append(random.choice(characters))

    # shuffle the password so the character types are unpredictable
    random.shuffle(password)

    # join the characters into one password
    return ''.join(password)
