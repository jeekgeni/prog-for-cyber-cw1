#create function to validate IP address
def validate_ip(ip_address):

    #remove unnessecary spsces
    ip_address = ip_address.strip()

    #check if the IP address contains dots 
    if "." not in ip_address:
        return False

    #split the IP address intom seperate parts 
    ip_parts = ip_address.split(".")

    #check if there are exactly four numbers
    if len(ip_parts) != 4:
        return False

    #check each part of the IP address
    for part in ip_parts:

        #check if the part is a number
        if not part.isdigit():
            return False

        #convert the part to an integer
        num = int(part)

        #check if the number is between 0 and 255
        if num < 0 or num > 255:
            return False

    #return true if all checks pass
    return True

#ask the user to enter an IP address
while True:
    ip_address = input("Enter an IP address (or type exit to quit): ")
    if ip_address.lower() == "exit":
        break

    #check if the IP address is valid 
    if validate_ip(ip_address):
        print(f"{ip_address} is a valid IP address.")
    else:
        print(f"{ip_address} is not a valid IP address.")
