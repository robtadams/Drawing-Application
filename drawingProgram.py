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
    print("Increase Size - Plus")
    print("Decrease Size - Minus")

    print("\n" + "Quit   - Escape")
    print("---------------------------")

    running = True
    mouseColor = [0, 0, 0]
    mouseSize = 1
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                match event.key:
                    
                    # Escape
                    case 27:
                        pygame.quit()

                    # Minus
                    case 45:
                        mouseSize -= 10
                        if mouseSize < 1:
                            mouseSize = 1
                        print("Size: " + str(mouseSize))
                        
                    # 0
                    case 48:
                        mouseColor = "black"
                        print("Color: Black")
                        
                    # 1
                    case 49:
                        mouseColor = "red"
                        print("Color: Red")

                    # 2
                    case 50:
                        mouseColor = "orange"
                        print("Color: Orange")

                    # 3
                    case 51:
                        mouseColor = "yellow"
                        print("Color: Yellow")

                    # 4
                    case 52:
                        mouseColor = "green"
                        print("Color: Green")

                    # 5
                    case 53:
                        mouseColor = "blue"
                        print("Color: Blue")

                    # 6
                    case 54:
                        mouseColor = "purple"
                        print("Color: Purple")

                    # 7
                    case 55:
                        mouseColor = "cyan"
                        print("Color: Cyan")

                    # 8
                    case 56:
                        mouseColor = "pink"
                        print("Color: Pink")

                    # 9
                    case 57:
                        mouseColor = "white"
                        print("Color: White")

                    # Plus
                    case 61:
                        mouseSize += 10
                        if mouseSize > 100:
                            mouseSize = 100
                        print("Size: " + str(mouseSize))

                    # F
                    case 102:
                        window.fill(mouseColor)

                        

                """
                if event.key == pygame.K_0:
                    mouseColor = "black"
                elif event.key == pygame.K_1:
                    mouseColor = "red"
                elif event.key == pygame.K_2:
                    mouseColor = "orange"
                elif event.key == pygame.K_3:
                    mouseColor = "yellow"
                elif event.key == pygame.K_4:
                    mouseColor = "green"
                elif event.key == pygame.K_5:
                    mouseColor = "blue"
                elif event.key == pygame.K_6:
                    mouseColor = "purple"
                elif event.key == pygame.K_7:
                    mouseColor = "cyan"
                elif event.key == pygame.K_8:
                    mouseColor = "pink"
                elif event.key == pygame.K_9:
                    mouseColor = "white"
                    
                elif event.key == pygame.K_f:
                    window.fill(mouseColor)

                elif event.key == pygame.K_PLUS or event.key == pygame.K_KP_PLUS:
                    mouseSize += 10

                elif event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:
                    mouseSize -= 10
                    if mouseSize < 1:
                        mouseSize = 1
                    
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                """

            # Left-click
            if pygame.mouse.get_pressed()[0]:
                mousePos = pygame.mouse.get_pos()
                mouseX = mousePos[0]
                mouseY = mousePos[1]
                pygame.draw.circle(window, mouseColor, mousePos, mouseSize)

        pygame.display.update()

main()
    
