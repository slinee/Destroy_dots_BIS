# Imports ---------------

from guizero import App, Text, Waffle   #importing App,Text and Waffle from guizero library
from random import randint      # we  import randint from random

# Variables -------------

GRID_SIZE = 5      # Giving the value of 5 to "GRID_SIZE" variable
score = 0


# Functions -------------

def add_dot():      # creating a function with the name "add_dot"
    x, y = randint(0, GRID_SIZE - 1), randint(0, GRID_SIZE - 1)     #Generating random variables for x and y coordinates
    while board[x, y].dotty == True:        # Checks whether the chosen square is already a dot
        x, y = randint(0, GRID_SIZE - 1), randint(0, GRID_SIZE - 1)
    board[x, y].dotty = True        #When we make sure that x and y co-ordinate is a square we add a red dot
    board.set_pixel(x, y, "red")

    speed = 1000    # normal speed of the game (1 second)
    if score > 30:      # if player has more than 30 points the speed is increased
        speed = 200
    elif score > 20:      # if player has more than 20 points the speed is increased
        speed = 400
    elif score > 10:      # if player has more than 10 points the speed is increased
        speed = 500

    all_red = True      #assumes that all squares are red
    for x in range(GRID_SIZE):      #nested loop which checks if said before is true
        for y in range(GRID_SIZE):
            if board[x, y].color != "red":      # if some square is not red then the all_Red variable becomes false
                all_red = False
    if all_red:     # if all are red then -->
        score_display.value = "You lost! Score: " + str(score)      # You lost message and the score are displayed
    else:       # if the player didn't lose the game continues
        board.after(speed, add_dot)


def destroy_dot(x, y):      # Creating a function with the name destroy_dots and parameters x and y
    global score
    if board[x, y].dotty == True:       # If the co-ordinate is a dot then true will return if it is square then false
        board[x, y].dotty = False    # If it is a dot we change it back to square and also give it the white colour
        board.set_pixel(x, y, "white")
        score += 1
        score_display.value = "Your score is " + str(score)     # Display the score


# App -------------------

app = App("Destroy the dots")       # The name of the app is set to "Destroy the dots"

instructions = Text(app, text="Click the dots to destroy them")     # Displaying the instructions
board = Waffle(app, width=GRID_SIZE, height=GRID_SIZE, command=destroy_dot)     # The board is created
board.after(1000, add_dot)      # time is set to 1000 millisecond(1 second) and add_Dot function is also called
score_display = Text(app, text="Your score is " + str(score))       # Displaying the score

app.display()          # displaying/running the app
