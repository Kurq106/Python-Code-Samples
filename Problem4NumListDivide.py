# Kimberly Urquiza
# 11/26/2024
# Problem 4: Appending numbers divisible by 10 to a list.
# This program uses a while loop to find numbers divisible by 10 
# between 0 and 50 and appends them to a list.

def problem4():
    tens = []  # Initialize an empty list
    counter = 0  # Counter starts at 0
    while counter <= 50:  # Loop runs until counter reaches 50
        if counter % 10 == 0:  # Check if counter is divisible by 10
            tens.append(counter)  # Append the divisible number to the list
        counter += 1  # Increment the counter
    print("List of tens:", tens)  # Output the list of divisible numbers

problem4()
