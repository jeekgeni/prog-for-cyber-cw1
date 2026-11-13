#ask user to input a number between 1-100

number = int(input("Enter a positive integer between 1 and 100: "))

#check if the number is outside the allowed range
if number < 1 or number > 100:
    print("Error: Number must be between 1 and 100.")
#if the number is in range, check if it is even
elif number % 2 == 0:
    print("The number is even.")

#if neither condition above is true, the number must be odd
else:
    print("The number is odd.")
