# Kimberly Urquiza
# Date: 11/12/2024

# Problem 1
def check_equality():
    # Get user input
    input1 = input("Enter the first value: ")
    input2 = input("Enter the second value: ")
    
    # Check if they are equal
    if input1 == input2:
        print("The values are equal.")
    else:
        print("The values are not equal.")
        
check_equality()

# Problem 2 
def check_sum():
    # Get user input and convert to integers
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    # Calculate the sum
    total = num1 + num2
    
    # Check the sum
    if total > 10:
        print("The sum is greater than 10.")
    elif total < 10:
        print("The sum is less than 10.")
    else:
        print("The sum is equal to 10.")

check_sum()

# Problem 3 
def check_value_in_list(lst):
    if 5 in lst:
        print("The value 5 is in the list.")
    else:
        print("The value 5 is not in the list.")

# Example list
numbers = [1, 2, 3, 4, 5]
check_value_in_list(numbers)

# Problem 4
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Test the function
year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# Problem 5 
class Character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

    def profile(self):
        return self.nickname, self.weapons, self.weaknesses

def check_task(character):
    # Task 1: Climb a mountain – needs rope, coat, and first aid kit, cannot have slow
    if 'rope' in character.weapons and 'coat' in character.weapons and 'first aid kit' in character.weapons and 'slow' not in character.weaknesses:
        print(f"{character.nickname} can climb the mountain.")
    else:
        print(f"{character.nickname} cannot climb the mountain.")
    
    # Task 2: Cook a meal – needs pan, groceries, cannot have small
    if 'pan' in character.weapons and 'groceries' in character.weapons and 'small' not in character.weaknesses:
        print(f"{character.nickname} can cook the meal.")
    else:
        print(f"{character.nickname} cannot cook the meal.")
    
    # Task 3: Write a book – needs pen, paper, idea, cannot have confusion
    if 'pen' in character.weapons and 'paper' in character.weapons and 'idea' in character.weapons and 'confusion' not in character.weaknesses:
        print(f"{character.nickname} can write the book.")
    else:
        print(f"{character.nickname} cannot write the book.")

# Example character
player1 = Character('Dragon Slayer', ['pan', 'paper', 'idea', 'rope', 'groceries'], ['slow'])
check_task(player1)