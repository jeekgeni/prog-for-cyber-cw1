#create a security event messsage using string analysis 

#store the event
event = "security alert: Failed login attempt detected from IP address 192.168.1.25. The user account admin was targeted at 22:45. The server blocked the login attempt after an incorrect password was entered."

#check whether the event contains specific keywords
failed_event = "Failed" in event 
login_event = "login" in event

#split the events into words 
words = event.split()

#find an IP address 
ip_address = ""

for word in words:
    word = word.strip(".")  # Remove the full stop at the end

    if word.count(".") == 3 and word [0].isdigit():
        ip_address = word
        break


#display analysis results
print("\nSecurity Event Analysis:")
print("---------------------------")
print("Failed event:", "Yes" if failed_event else "No")
print("Login event:", "Yes" if login_event else "No")
print("IP Address:", ip_address)

#Display security message
if failed_event:
    print("Warning: A failed login attempt was detected from IP address", ip_address)

if login_event:
    print("Alert: A login activity was detected.")

if failed_event and login_event:
    print("Action: Investigation is required for the failed login attempt")
    