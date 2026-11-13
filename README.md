# IP Address Validator 

📚Student Information📚
Name - Kiara Mullen
Campus - New College Lanarkshire/UWS
Banner ID - b01886849

## Project Description 
I have developed an IP Address Validator program as part of y Year 2 bEng Cybersecurity coursework. 
The program uses Python to check whether an IP address entered by the user is valid. It demonstrates basic programming concepts and the importance of validating network security in cybersecurity. 

## 🔧Tools Used 
🐍Python 3 
Visual Studio Code 
GitHub
Windows 

## Features
-Allows the user to enter an IP Address 
-Removes unnessecary spaces from the input
-Checks that the address contains exactly four sections
-Ensures each number is within the valid range of 0-255
-Displays whether the IP addres is valid or invalid
-Allows the user to check multiple IP Addresses until they chose to exit 


## 🚀How to run 
1 - Dowload or clone my prog-for-cyber-cw1 repository from GitHub 
2 - Open the project folder in Visual Studio Code 
3 - Open the terminal
4 - Run the python file 
    python IP-validator.py
5 - Follow on screen instructions

## How the program works 

The program uses a function called validate_ip() to check the IP Address entered by the user. 
The function:
-Removes unnesecary spaces using .strip()
- Checks that the address contains full stops 
- Checks that each section contains numbers using .isdigit()
- Converts each section into an integer 
- Checks that each section is a number between 0-255
- Returns True if all checks pass or False if the address is invalid.

A while loop allows the user to continue checkin IP Addresses until they type exit. 

# Example usage 
Valid IP Address 
Enter an IP Address (or type exit to quit): 192.168.1.1 
192.168.1.1 is a valid IP address 

Invalid IP Address 
Enter an IP address(or type exit to quit): 192.168.1.300
192.168.1.300 is not a valid IP address

Exit the program:
Enter an IP Address (or type exit to quit): exit 

# ⭐Author⭐
Kiara Mullen 
bEng Cybersecutiy Year2
UWS Motherwell  




