## Security Incident Manager 

📚Student Information📚

Name - Kiara Mullen 
Campus - New College Lanarkshire 
Banner ID - b01886849

## Project Description 
I have developed a Python program that allows a user to record and update basic security incident infromation as pary of my Year 2 bEng Cybersecurity coursework. 
The program stores incident details in a dictionary and allows the user to enter a username and IP address. It then updates the incident record, changes the risk level, removes an existing field and displays the updated information. 

# Tools Used

🐍Python 3
   Visual Studio Code 
   GitHub 
🪟Windows 

## Features 
- Stores security incident information using a Python dictionary
- Allows the user to enter a username and IP address
- Displays the original incident details
- Adds a status field to the incident record
- Records the date of the incident 
- Allows the risk level to be updated
- Removes the incident type from the dictionary 
- Displays all remaining dictionary keys and values
- Counts and displays the total number of fields 
- Displays a warning if the risk level is set to Critical

## 🚀How to run 

1. Dowload or clone my prog-for-cyber-cw1 repository from GitHub
2.  Open the project folder in Visual Studio Code
3. Open the terminal 
4. Run the Python file:
    python security-incident-manager.py
5. Follow on screen instructions to enter the incident details and risk level. 

## How the program works 

The prorgam uses a dictionary called security_incident to store the incident information.

The program:

1. Creates a dictionary containing the initial incident details
2.  Asks the user to enter a username and IP address 
3.  Displays the incident information 
4.  Adds a new field called status
5.  Adds the date the incident was recorded
6.  Allows the user to update the risk level
7.  Removes the Incident Type field using .pop()
8.  Uses a for loop to display the remaining dictionary keys and values 
9.  Uses len() to count the number of fields 
10. Uses an if/else statement to display a warning if the risk level is Critical

## Example Usage 

Enter the username: KIARA
Enter IP Address: 192.168.10.1

===========
## SECURITY INCIDENT
\\\text 

Username: KIARA 
IP Address: 192.168.10.1
Incident Type: Failed Login Attempt
Risk Level: -High-

Update risk level (Low, Medium or Critical): Critical 


===========
## SECURITY UPDATE
===========
\\\
Incident ID: 1001
Username: KIARA
IP Address: 192.168.10.1
Risk Level: Critical 
status: Under Investigation
Date Recorded: 10/10/2026

Total number of fields: 6 

WARNING: Critical security incident detected! Immediate action required.



# ⭐Author⭐ 
Kiara Mullen 
bEng Cybersecurity Year2 
UWS Motherwell 