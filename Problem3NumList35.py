# Kimberly Urquiza
# 11/26/2024
# Problem 3: Summing user input in a list until the total is greater than 100.
# This program repeatedly asks the user for numbers, appends them to a list, 
# and sums the list until the total exceeds 100.

def problem3():
    numbers = []  # Initialize an empty list
    total = 0  # Start the total at 0
    while total <= 100:  # Loop runs until the sum exceeds 100
        num = int(input("Enter a number: "))  # Ask the user for a number
        numbers.append(num)  # Add the number to the list
        total = sum(numbers)  # Recalculate the total
    print("Numbers entered:", numbers)  # Output the list of numbers
    print("Total sum:", total)  # Output the total sum

problem3()

