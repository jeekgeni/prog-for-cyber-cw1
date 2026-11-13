#set the first two numbers in the fibonacci sequence

first = 0
second = 1
#repeat the loop 20 times to print the next 20 numbers in the fibonacci sequence
for i in range(20):
#print the current number on the same line
    print(first, end=" ")
#add the previous two numbers to get the next number in the sequence
    next_number = first + second
#move the second number into first position
    first = second
#store the new number in the second position
    second = next_number
    