# Kimberly Urquiza
# 11/26/2024
# Problem 2: Creating a list with numbers from 0 to 10 using a while loop.
# This program uses a while loop to append numbers from 0 to 10 to a list.

def problem2():
    L = []  # Initialize an empty list
    counter = 0  # Counter starts at 0
    while counter <= 10:  # Loop runs while counter is 10 or less
        L.append(counter)  # Append the current counter value to the list
        counter += 1  # Increment the counter
    print("List L:", L)  # Output the final list

problem2()
