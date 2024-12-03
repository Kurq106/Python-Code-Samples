# Kimberly Urquiza
# Date
# Problem 4: Return a list with only unique elements from the original list [1, 3, 3, 3, 6, 2, 3, 5].

def get_unique(arr):
    # Returns a new list with unique elements from arr
    unique_list = []
    for item in arr:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Test
arr = [1, 3, 3, 3, 6, 2, 3, 5]
print("Unique elements in", arr, "are:", get_unique(arr))

