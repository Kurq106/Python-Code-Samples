# Kimberly Urquiza
# Date
# Problem 5

import turtle

def draw_square(t, size):
    # Draws a square with the given size using forward and left
    for _ in range(4):
        t.forward(size)
        t.left(90)

def main():
    wn = turtle.Screen()
    t = turtle.Turtle()
    t.color("blue")
    
    # Initial size of the smallest square
    initial_size = 20
    
    # Draw stacked squares
    for i in range(5):
        size = initial_size + i * 20  # Increase size for each larger square
        
        # Move to the starting position for each square, stacking on top
        t.penup()
        t.goto(-size / 2, -size / 2)  # Center each square by starting at its bottom-left corner
        t.pendown()
        
        # Draw the square
        draw_square(t, size)

    wn.exitonclick()

main()
