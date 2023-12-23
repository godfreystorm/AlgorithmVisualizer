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

    FONT = pygame.font.SysFont('comicsans', 20) # The font used for all the text.
    LARGE_FONT = pygame.font.SysFont('comicsans', 40) 
    SIDE_PADDING = 100 # padding on edges putting the chart/graph being sorted in the middle of the screen.
    TOP_PADDING = 150 # padding on the top of the screen.

    def __init__(self, width, height, lst): # Constructor for the drawing information.e.g. the width and height of the screen.
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width, height)) # Set the window to the size of the screen.
        pygame.display.set_caption("Sorting Algorithm Visulaizer") # Set the window caption.
        self.set_list(lst) # Set the list of numbers to be sorted.

    def set_list(self, lst): # Set the list of numbers to be sorted.
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        self.block_width = round((self.width - self.SIDE_PADDING) / len(lst)) # calculate the width of each block.
        self.block_height = round((self.height - self.TOP_PADDING) / (self.max_val - self.min_val)) 
        self.start_x = round(self.SIDE_PADDING / 2) # calculate the x position of each block within the screen window.

def generate_starting_list(n, min_val, max_val): # Generate a list of random numbers between min_val and max_val to use as the starting point for the chart.
    lst = []
    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)
            
    return lst

def draw(draw_info): # Actual drawing of the chart with the given draw_info object.
    draw_info.window.fill(draw_info.BACKGROUND_COLOR) # Fill the background with background color variable allowing for easy change of background color.
    
    controls = draw_info.FONT.render("R - Reset | SPACE - start sorting | A - ascending | D - descending", 1, draw_info.BLACK)
    draw_info.window.blit(controls, (draw_info.width/2 - controls.get_width()/2 , 5))
    
    sorting = draw_info.FONT.render("I - Insertion Sort | B - Bubble Sort", 1, draw_info.BLACK)
    draw_info.window.blit(sorting, (draw_info.width/2 - sorting.get_width()/2, 35))

    draw_list(draw_info)
    pygame.display.update() # Update the window to show the chart/graph.

def draw_list(draw_info): # Draw a list of random numbers between min_val and max_val, using the DrawInformation object.
    lst = draw_info.lst # Get the list of numbers to be sorted.

    for i, val in enumerate(lst): # For each number in the list, draw a rectangle with the color determined by the gradient.
        x = draw_info.start_x + i * draw_info.block_width 
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height 
        
        color = draw_info.GRADIENTS[i % 3] # Get the color of the gradient.

        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.height)) # Draw a rectangle with the color determined by the color of the gradient.


def main():
    run = True
    clock = pygame.time.Clock()

    n = 50 # number of random numbers to generate.
    min_val = 0 
    max_val = 100

    lst = generate_starting_list(n, min_val, max_val) # generate a list of random numbers between min_val and max_val.
    draw_info = DrawInformation(800, 600, lst) # create a DrawInformation object to draw the chart/graph; The grarph is a visualization of the data to be sorted.
    
    #Sorting functionalities.
    sorting = False #Starts as false so that the program will not start sorting untill user tells it to.
    ascending = True 

    while run: # Loop for pygame to run until the user clicks the close button.
        clock.tick(60) # Set the clock to 60 frames per second.

        draw(draw_info) # Draw the chart

        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: # Exit program; To allow the user to close the program with "X" icon.
                run = False

            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_r: # Statement added to constantly running pygame loop to check if the user pressed the "r" key. If they did program will reset the list of numbers/chart.
                lst = generate_starting_list(n, min_val, max_val) # regenerate the list of numbers/chart.
                draw_info.set_list(lst) # Resseting on draw_info class so it updates when we are actually drawing the chart/graph.
                sorting == False
            elif event.key == pygame.K_ESCAPE and sorting == False: # The and added so we cant start sorting when already sorting.
                sorting = True # The elif checks if user pressed the escape key. If they did, the program will start sorting.
            elif event.key == pygame.K_a and not sorting:
                ascending = True
            elif event.key == pygame.K_a and not sorting:
                ascending = False


    pygame.quit()

if __name__ == "__main__":
    main()


