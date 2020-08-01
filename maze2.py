import turtle  # imports the graphics library turtle

screen = turtle.Screen()  # Creates the screen
screen.title("Mazeguiz")  # Set the screens title to mazeguiz


# class that will draw the four sided cells/squares
def draw_box(t, x, y, s, ):
    t.penup()  # lifts the drawing symbol
    t.goto(x, y)  # moves pointer to "new center"
    t.pendown()  # draws visibly
    # loop to draw the square
    for i in range(0, 4):
        board.forward(s)
        board.right(90)


board = turtle.Turtle()  # places pointer on screen

start_x = -120  # Sets starting point for the x-axis
start_y = 0  # Sets starting point for the x-axis
box_size = 40  # Sets pixel size for each cell

# Sets the N*M of the rectangular array of cells
n = 4
m = 4

# loop that draws all the small squares
for i in range(0, n):  # Height
    for j in range(0, m):  # width
        draw_box(board, start_x + j * box_size, start_y + i * box_size, box_size)

turtle.done()  # positions the screen so that it doesnt disappear
