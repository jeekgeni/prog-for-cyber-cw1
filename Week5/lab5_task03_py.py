#security incident manager using dictionaries

#create a dictionary containing security incident details

incident = {
    "username": "Jane Doe",
    "IP address": "192.168.1.100",
    "event type": "Malware Detection",
    "risk level": "High",

}

#display username and IP address
print("\n =========== SECURITY INCIDENT DETAILS ===========")
print("username:", incident["username"])
print("IP Address:", incident ["IP address"])

#add a field called status 
incident["status"] = "Under Investigation"

print("\n=========== INCIDENT STATUS UPDATED ===========")
print("Updated incident:", incident)

#update the risk level
incident["risk level"] = "Critical"

print("\n=========== RISK LEVEL UPDATED ===========")
print("Updated risk level:", incident["risk level"])

del incident["event type"]
print("Updated incident after deleting event type:", incident)

#display all remaining keys and values in the dictionary
print("All dictionary keys and values:")
for key, value in incident.items():
    print(key, ":", value)

#display all keys
print("\n=========== DICTIONARY KEYS ===========")
for key in incident.keys():
    print("Dictionary key:", key)

#display all values
print("\n=========== DICTIONARY VALUES ===========")
print("Dictionary values:", incident.values())

#display total number of key value pairs in the dictionary
print("\n=========== TOTAL RECORDS ===========")
print("Total number of key-value pairs:", len(incident))

print("\n=========== END OF INCIDENT REPORT ===========")
