import pygame
import queue

def main():

    # Initialize Pygame
    pygame.display.init()

    # Initialize the Clock
    clock = pygame.time.Clock()

    # Set the dimensions of the window
    windowWidth = 800
    windowHeight = 600

    # Create the window
    window = pygame.display.set_mode((windowWidth, windowHeight))

    # Set the window caption and window color
    pygame.display.set_caption("Drawing Program")
    windowColor = [255, 255, 255]
    window.fill(windowColor)

    # Update the window
    pygame.display.update()

    # Print the menu for the User
    print("---------------------------")
    print("Drawing Program")
    print("Red    - 1")
    print("Orange - 2")
    print("Yellow - 3")
    print("Green  - 4")
    print("Blue   - 5")
    print("Purple - 6")
    print("Cyan   - 7")
    print("Pink   - 8")
    print("White  - 9")
    print("Black  - 0")
    
    print("\n" + "Fill   - F")
    print("Paint  - P")
    print("Increase Size - Plus")
    print("Decrease Size - Minus")

    print("\n" + "Quit   - Escape")
    print("---------------------------")

    # Initialize running, brushColor, and brushSize
    running = True                          # Run the program while True, stop the program while False
    brushColor = pygame.Color(0, 0, 0, 255) # brushColor affects the color of the paint
    brushSize = 1                           # brushSize affects the size of the brush
    brushMode = "paint"

    # While running is True...
    while running:

        # ... get an event...
        for event in pygame.event.get():

            # ... if the event is a key press...
            if event.type == pygame.KEYDOWN:
                print(event.key)

                # ... check if the key pressed is...
                match event.key:
                    # Escape
                    case 27:
                        # Stop the game
                        running = False

                    # Minus
                    case 45:
                        
                        # Decrease the size of the brush
                        brushSize -= 10

                        # Prevent the brush size from getting too small
                        if brushSize < 1:
                            brushSize = 1

                        # Inform the user of the new brush size
                        print("Size: " + str(brushSize))
                        
                    # 0
                    case 48:

                        # Set the paint to be Black
                        brushColor = pygame.Color("Black")
                        print("Color: Black")
                        
                    # 1
                    case 49:

                        # Set the paint to be Red
                        brushColor = pygame.Color("Red")
                        print("Color: Red")

                    # 2
                    case 50:

                        # Set the paint to be Orange
                        brushColor = pygame.Color("Orange")
                        print("Color: Orange")

                    # 3
                    case 51:

                        # Set the paint to be Yellow
                        brushColor = pygame.Color("Yellow")
                        print("Color: Yellow")

                    # 4
                    case 52:

                        # Set the paint to be Green
                        brushColor = pygame.Color("Green")
                        print("Color: Green")

                    # 5
                    case 53:

                        # Set the paint to be Blue
                        brushColor = pygame.Color("Blue")
                        print("Color: Blue")

                    # 6
                    case 54:

                        # Set the paint to be Purple
                        brushColor = pygame.Color("Purple")
                        print("Color: Purple")

                    # 7
                    case 55:

                        # Set the paint to be Cyan
                        brushColor = pygame.Color("Cyan")
                        print("Color: Cyan")

                    # 8
                    case 56:

                        # Set the paint to be Pink
                        brushColor = pygame.Color("Pink")
                        print("Color: Pink")

                    # 9
                    case 57:

                        # Set the paint to be White
                        brushColor = pygame.Color("White")
                        print("Color: White")

                    # Plus
                    case 61:

                        # Increase the size of the brush
                        brushSize += 10

                        # Prevent the brush from getting too big
                        if brushSize > 100:
                            brushSize = 100

                        # Inform the user of the new brush size
                        print("Size: " + str(brushSize))

                    # F
                    case 102:
                        print("Fill mode")
                        brushMode = "fill"

                    # P
                    case 112:
                        print("Paint mode")
                        brushMode = "paint"
                    

            # ... if the event is a left-mouse click...
            if pygame.mouse.get_pressed()[0]:

                # ... get the Position of the mouse
                mousePos = pygame.mouse.get_pos()

                mouseX = mousePos[0]
                mouseY = mousePos[1]

                if brushMode == "paint":

                    # Draw a circle on the window
                    # Set the circle's color to brushColor
                    # Draw the circle at the mouse's position
                    # Set the circle's size to brushSize
                    pygame.draw.circle(window, brushColor, mousePos, brushSize)

                if brushMode == "fill":

                    colorPicked = window.get_at(mousePos)
                    if colorPicked != brushColor:

                        pixelQueue = []
                        pixelQueue.append(mousePos)

                        while pixelQueue:
                            pixel = pixelQueue.pop(0)
                            #print(pixel)
                            window.set_at(pixel, brushColor)

                            # North Pixel
                            northPixel = (pixel[0], pixel[1] - 1)
                            if northPixel[1] >= 0:
                                if window.get_at(northPixel) == colorPicked:
                                    window.set_at(northPixel, brushColor)
                                    pixelQueue.append(northPixel)

                            # East Pixel
                            eastPixel = (pixel[0] + 1, pixel[1])
                            if eastPixel[0] < windowWidth:
                                if window.get_at(eastPixel) == colorPicked:
                                    window.set_at(eastPixel, brushColor)
                                    pixelQueue.append(eastPixel)

                            # South Pixel
                            southPixel = (pixel[0], pixel[1] + 1)
                            if southPixel[1] < windowHeight:
                                if window.get_at(southPixel) == colorPicked:
                                    window.set_at(southPixel, brushColor)
                                    pixelQueue.append(southPixel)

                            # West Pixel
                            westPixel = (pixel[0] - 1, pixel[1])
                            if westPixel[0] >= 0:
                                if window.get_at(westPixel) == colorPicked:
                                    window.set_at(westPixel, brushColor)
                                    pixelQueue.append(westPixel)
   
        # Update the window
        pygame.display.update()

    # Quit out of the game
    pygame.quit()

main()
    
