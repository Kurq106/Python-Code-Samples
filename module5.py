# Assignment 5
# Kimberly Urquiza
# 10/22/24

def print_hello(n):
    # TODO: Print hello n times
    for _ in range(n):
        print("Hello World")

def print_hello_alt(n):
    # TODO: There is another way without using loop but just print statement
    # 5 pts Extra credit
    print("Hello World\n" * n, end='')

def print_hello_recursion(n):
    # What about we use recursion?
    # 20 pts Extra credit
    if n > 0:
        print("Hello World")
        print_hello_recursion(n - 1)

def power_list(arr):
    # TODO: This is problem 2 in the handout
    # a. Write a loop that prints each of the numbers on a new line.
    for number in arr:
        print(number)
    # b. Write a loop that prints each number and its square on a new line.
    for number in arr: 
        print(f"{number} -> {number ** 2}")

def power_list_recursion(arr, index=0):
    # TODO: This is problem 2 in the handout
    # Instead of looping, how about recursion?
    # 20 pts Extra credit
    if index < len(arr): 
        print(arr[index])
        print(f"{arr[index]} -> {arr[index] ** 2}")  # Move this line up to print the square immediately
        power_list_recursion(arr, index + 1)

def draw_polygon(sides, length, line_color, fill_color):
    """
    Draws a regular polygon with the given parameters.

    Parameters:
    sides (int): The number of sides of the polygon.
    length (int): The length of each side of the polygon.
    line_color (str): The color of the polygon's outline (as a string, e.g., 'blue').
    fill_color (str): The color to fill the inside of the polygon (as a string, e.g., 'red').
    """
    import turtle
    turtle.color(line_color)
    turtle.fillcolor(fill_color)
    turtle.begin_fill()

    for _ in range(sides):
        turtle.forward(length)  # Fixed a typo here from "foward" to "forward"
        turtle.left(360 / sides)
    
    turtle.end_fill()
    turtle.done()

def problem_4():
    """
    Consider a program that iterates the integers from 1 to 50. For multiples of three
    print “Divisible by three” instead of the number and for the multiples of five print “Divisible by
    five”. For numbers which are multiples of both three and five print “Divisible by both”.
    """
    for number in range(1, 51):
        if number % 3 == 0 and number % 5 == 0:
            print("Divisible by both")
        elif number % 3 == 0:
            print("Divisible by three")  # Fixed a typo here from "Dicisible" to "Divisible"
        elif number % 5 == 0:
            print("Divisible by five")
        else: 
            print(number)

def problem_5():
    import turtle 
    turtle.speed(10)  # Increase the drawing speed
    for i in range(36):  # draw 36 shapes
        for _ in range(4):  # Draw a square
            turtle.forward(100)
            turtle.right(90)
        turtle.right(10)  # turn to create a circular pattern

    turtle.done()  # Move this line out of the loop to avoid multiple "done" calls

def main():
    # call your functions here
    n = 100
    print_hello(n)
    print_hello_alt(n)
    print_hello_recursion(n)
    
    # Specify my number list 
    numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]  # Fixed the variable name from 'number' to 'numbers'
    power_list(numbers)
    power_list_recursion(numbers)

    sides = int(input("Enter the number of sides: "))
    length = int(input("Enter the length of the sides: "))
    line_color = input("Enter the color of the line: ")
    fill_color = input("Enter the fill color: ")
    draw_polygon(sides, length, line_color, fill_color)

    problem_4()  # Added parentheses to call the function
    problem_5()  # Added parentheses to call the function

main()
