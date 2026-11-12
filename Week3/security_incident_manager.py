#create a dictionary with security incident information
security_incident = {
    "Incident ID": "1001",
    "Username": "admin",
    "IP Address": "192.168.1.10",
    "Incident Type": "Failed Login Attempt",
    "Risk Level": "-High-"

}

#ask the user to enter incident details
security_incident["Username"] = input("Enter the username: ")
security_incident["IP Address"] = input("Enter IP address: ")


#display the original incident details 
print("=================")
print("SECURITY INCIDENT")
print("Username:", security_incident["Username"])
print("IP Address:", security_incident["IP Address"])
print("Incident Type:", security_incident["Incident Type"])
print("Risk Level:", security_incident["Risk Level"])


#Display the username and IP Address
print("Username:", security_incident["Username"])
print("IP Address:", security_incident["IP Address"])

#add a new new field to the dictionary called "status" 
security_incident["status"] = "Under Investigation"

#add the date the incident was recorded 
security_incident["Date Recorded"] = "10/10/2026"

#UPDATE THE RISK LEVEL
security_incident["Risk Level"] = input("Update risk level (Low, Medium or Critical): ")

#Remove a field from the dictionary
security_incident.pop("Incident Type")

#display all remaining keys and values
print("\n=============")
print("SECURITY UPDATE")
print("===============")

for key, value in security_incident.items():
    print(key, ":", value)

#display the total number of fields in the dictionary
print("\nTotal number of fields:", len(security_incident))

#Display a message based on the risk level
if security_incident["Risk Level"] == "Critical":
    print("WARNING: Critical security incident detected! Immediate action required.")
else:
    print("No critical security incidents detected. Continue monitoring.")

print("\n====================")
print("Incident record has been updated successfully.")


