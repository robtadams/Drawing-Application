import pygame

def main():
    pygame.display.init()
    clock = pygame.time.Clock()

    windowWidth = 800
    windowHeight = 600

    window = pygame.display.set_mode((windowWidth, windowHeight))
    pygame.display.set_caption("Drawing Program")

    windowColor = [255, 255, 255]
    window.fill(windowColor)

    pygame.display.update()

    """Print the menu here"""
    """Red    - 1"""
    """Orange - 2"""
    """Yellow - 3"""
    """Green  - 4"""
    """Blue   - 5"""
    """Purple - 6"""
    """White  - 9"""
    """Black  - 0"""

    """Create variables for brushColor and brushSize"""

    """Create a while loop"""

    ...."""Create a for loop to get the pygame events"""
    
    ........"""Check if the user presses a KEYDOWN"""

    ............"""Match the event.key to its case"""
    ............"""case 27 = Escape"""
    ............"""case 45 = Minus """
    ............"""case 48 = 0     """
    ............"""case 49 = 1     """
    ............"""case 61 = Plus  """
                
    ........"""Check if the mouse gets pressed"""

    ............"""Get the position of the mouse"""

    ............"""Draw a circle on the window, using brushColor, the mouse's position, and brushSize"""

    ...."""Update the display"""

main()
