#Security tool task

#Set password criteria
correct_password = "Cyber123!"

#Ask the user to authenticate
password = input("Enter your password: ")

while password != correct_password:
    print("Incorrect password. Please try again.")
    password = input("Enter your password: ")

print("Password accepted. You are now authenticated.")

def security_event_counter():
    correct_password = "Cyber123!"
    correct_count = 0
    incorrect_count = 0

    for attempt in range(10):
        password = input("Enter your password: ")
        if password == correct_password:
            print("Password accepted.")
            correct_count += 1
        else:
            print("Incorrect password.")
            incorrect_count += 1
    incorrect_percentage = (incorrect_count / 10) * 100
    print(f"Correct passwords: {correct_count}")
    print(f"Incorrect passwords: {incorrect_count}")
    print(f"Percentage of incorrect passwords:", incorrect_percentage, "%")
    if incorrect_percentage > 50:
        print("Warning: More than 50% of attempts were incorrect.")

def brute_force_attack_simulation():
    correct_password = "Cyber123!"
    max_attempts = 3
    attempts = 0

    while attempts < max_attempts:
        password_guess = input("Guess the password: ")
        attempts += 1

        if password_guess == correct_password:
            print("Password found.")
            print(f"Number of attempts: {attempts}")
            break   
        else:
            print("Incorrect password. Try again.")
    if attempts == max_attempts and password_guess != correct_password:
        print("Maximum attempts reached. Access denied.")

def login_authentication():
    correct_username = "admin"
    correct_password = "Cyber123!"
    failed_attempts = 0

    while failed_attempts < 3:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username == correct_username and password == correct_password:
            print("Login successful.")
            return
        else:
            failed_attempts += 1
            print(f"Incorrect username or password.")
            print(f"Failed attempts: {failed_attempts}")
    print("Account is frozen for 24 hours due to multiple failed login attempts.")
       
#display security menu
while True:
#menu options
    print("\n===== Security Tool =====")
    print("1. Security Event Counter")
    print("2. Brute Force Attack Simulation")
    print("3. Login Authentication")
    print("4. Exit")

    choice = input("Select an option (1-4): ")

    if choice == "1":
        security_event_counter()
    elif choice == "2":
        brute_force_attack_simulation()
    elif choice == "3":
        login_authentication()
    elif choice == "4":
        print("Thank you for using the Security Tool.")
        break
    else:
        print("Invalid option. Please try again.")
        