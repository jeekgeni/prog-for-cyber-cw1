#import the modules needed for event ID, timestamps and IP address
import random
from datetime import datetime
import socket

#set a correct username and password for the login event
correct_username = "admin"
correct_password = "password123!"

#get the IPaddress of this computer
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]
except OSError:
    ip_address = "127.68.0.1"
finally:
    s.close()

#Ddisplay the event log heading
print("SECURITY EVENT LOG")
print("-------------------")

#keep asking the user for a username and password until they enter the correct ones
while True:
#ask the user for a username and password
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    #check if the entered username and password are correct
    if username == correct_username and password == correct_password:
        event = "Login successful!"
    else:
        event = "Login failed."

    #generate a randomm 4 -digit event ID
    event_id = random.randint(1000, 9999)

    #get the current date and time
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    #print the security event details
    print(f"Event ID: {event_id}")
    print(f"Username: {username}")
    print(f"IP Address: {ip_address}")
    print(f"Timestamp: {timestamp}")
    print(f"Event: {event}")
    print()

#stop asking for username and password if the login is successful
    if event == "Login successful!":
        print("Login successful! Access granted.")

        break
