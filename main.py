import pygame
import random
pygame.init()

class DrawInformation: # Constructor for the drawing information.e.g. the width and height of the screen.
    BLACK = 0,0,0
    WHITE = 255,255,255
    GREEN = 0,255,0
    RED = 255,0,0
    BACKGROUND_COLOR = WHITE

    GRADIENTS = [ # The list of gradients to be used in the chart/graph. Colors selceted with intension of allowing user to easily indentify differences.
        (128,128,128),
        (160, 160, 160),
        (192, 192, 192)
    ]

    SIDE_PADDING = 100 # padding on edges putting the chart/graph being sorted in the middle of the screen.
    TOP_PADDING = 150 # padding on the top of the screen.

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visulaizer")
        self.set_list(lst)

    def set_list(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        self.block_width = round((self.width - self.SIDE_PADDING) / len(lst))
        self.block_height = round((self.height - self.TOP_PADDING) / (self.max_val - self.min_val))
        self.start_x = round(self.SIDE_PADDING / 2)

def generate_starting_list(n, min_val, max_val):
    lst = []
    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)
            
    return lst

def draw(draw_info): 
    draw_info.window.fill(draw_info.BACKGROUND_COLOR) # Fill the background with background color variable allowing for easy change of background color.
    pygame.display.update() # Update the window to show the chart/graph.

def draw_list(draw_info):
    lst = draw_info.lst

    for i val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height 
        
        color = 


def main():
    run = True
    clock = pygame.time.Clock()

    n = 50 # number of random numbers to generate.
    min_val = 0 
    max_val = 100

    lst = generate_starting_list(n, min_val, max_val) # generate a list of random numbers between min_val and max_val.
    draw_info = DrawInformation(800, 600, lst) # create a DrawInformation object to draw the chart/graph; The grarph is a visualization of the data to be sorted.

    while run: # Loop for pygame to run until the user clicks the close button.
        clock.tick(60)

        draw(draw_info) 

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: # Exit program; To allow the user to close the program with "X" icon.
                run = False

    pygame.quit()

if __name__ == "__main__":
    main()


