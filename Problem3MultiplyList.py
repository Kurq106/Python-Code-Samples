# Kimberly Urquiza
# Date
# Problem 3: Multiply all numbers in a list [5, 2, 7, -1].

def multiply_list(arr):
    # Multiplies all elements in arr and returns the result
    result = 1
    for num in arr:
        result *= num
    return result

# Test
arr = [5, 2, 7, -1]
print("The product of elements in", arr, "is:", multiply_list(arr))
