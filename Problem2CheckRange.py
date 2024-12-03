# Kimberly Urquiza
# Date
# Problem 2: Check if a number is in the range (1,10) and print the result.

def check_range(n):
    # Checks if n is in the range 1 to 10
    if n in range(1, 10):
        print(n, "is in the range")
    else:
        print(n, "is not in the range")

# Test
n = 7
check_range(n)
