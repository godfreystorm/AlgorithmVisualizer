import pygame
import random
pygame.init()

class DrawInformation:
    BLACK = 0,0,0
    WHITE = 255,255,255
    GREEN = 0,255,0
    RED = 255,0,0
    GREY = 128,128,128
    BACKGROUND_COLOR = WHITE

    SIDE_PADDING = 100 # padding on edges putting the chart/graph being sorted in the middle of the screen
    TOP_PADDING = 150 # padding on the top of the screen

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height

        self.window = pygame.display.pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visulaizer")
        self.et_list(lst)

    def set_list(self, lst):
        self.lst = lst
        self.min_vlaue = min(lst)
        self.max_value = max(lst)

        self.block_width = round((self.width - self.SIDE_PADDING) / len(lst))
        self.block_height = round((self.height - self.TOP_PADDING) / (self.max_value - self.min_vlaue))
        sels.start_x = round(self.SIDE_PADDING / 2)

    



