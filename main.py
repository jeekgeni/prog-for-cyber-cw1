#import security tools 
import security_tools

#ask the user to enter a password 
password = input ("Enter a password:")

#check if the password is strong
if security_tools.validate_password(password):
    print("The password is strong.")
else:
    print("The password does not meet the requirements. Please choose a stronger password.")
    #suggest a randomly generated strong password
    suggested_password = security_tools.generate_strong_password()
    print("Suggested strong password:", suggested_password)

#ask the user to enter an IP address
ip_address = input("Enter an IP address: ")

#check if the IP address is valid
if security_tools.validate_ip(ip_address):
    print("Valid IP address.")
else:
    print("Invalid IP address. Please enter a valid IP address.")