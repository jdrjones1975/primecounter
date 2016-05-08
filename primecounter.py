"""
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
"""
 
import pygame
import lib.func

pygame.init()

 
# Define some colors and global constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

WIDTH = 80
HEIGHT = 20

COUNT = 0
LIMIT = 999999


# create the fonts to be used
numFont = pygame.font.Font(None, 25) #sets the data fields header font

click_sound = pygame.mixer.Sound("resources/sounds/click.wav")


def main():
    """ Main function for the game. """

    # Set the width and height of the screen [width,height]
    size = [WIDTH, HEIGHT]
    screen = pygame.display.set_mode(size)

    count = COUNT
    limit = LIMIT

    tickSpeed = 20

    ones = True
    tens = False
    huns = False
    thous = False
    tenthous = False
    hunthous = False

    onesplace = 0
    tensplace = 0
    hunsplace = 0
    thousplace = 0
    tenthousplace = 0
    hunthousplace = 0

     
    pygame.display.set_caption("Prime Number Clicker")
 
    # Loop until the user clicks the close button.
    done = False

    # Loop until you hit a prime then wait until user presses space key (or big red button)
    advance = True
     
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    # -------- Main Program Loop -----------
    while not done:
        # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    advance = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                click_sound.play()
                posX = (pygame.mouse.get_pos()[0])
                if posX > 0 and posX < 1*(WIDTH/6):
                    if hunthousplace == 9:
                        hunthousplace = 0
                        texthunthous = numFont.render(str(hunthousplace), True, WHITE)
                        count = count - 900000
                    else:
                        hunthousplace += 1
                        texthunthous = numFont.render(str(hunthousplace), True, WHITE)
                        count = count + 100000
                        
                if posX > 1*(WIDTH/6) and posX < 2*(WIDTH/6):
                    if tenthousplace == 9:
                        tenthousplace = 0
                        texttenthous = numFont.render(str(tenthousplace), True, WHITE)
                        count = count - 90000
                    else:
                        tenthousplace += 1
                        texttenthous = numFont.render(str(tenthousplace), True, WHITE)
                        count = count + 10000
                        
                if posX > 2*(WIDTH/6) and posX < 3*(WIDTH/6):
                    if thousplace == 9:
                        thousplace = 0
                        textthous = numFont.render(str(thousplace), True, WHITE)
                        count = count - 9000
                    else:
                        thousplace += 1
                        textthous = numFont.render(str(thousplace), True, WHITE)
                        count = count + 1000

                if posX > 3*(WIDTH/6) and posX < 4*(WIDTH/6):
                    if hunsplace == 9:
                        hunsplace = 0
                        texthuns = numFont.render(str(hunsplace), True, WHITE)
                        count = count - 900
                    else:
                        hunsplace += 1
                        texthuns = numFont.render(str(hunsplace), True, WHITE)
                        count = count + 100

                if posX > 4*(WIDTH/6) and posX < 5*(WIDTH/6):
                    if tensplace == 9:
                        tensplace = 0
                        texttens = numFont.render(str(tensplace), True, WHITE)
                        count = count - 90
                    else:
                        tensplace += 1
                        texttens = numFont.render(str(tensplace), True, WHITE)
                        count = count + 10
                        
                if posX > 5*(WIDTH/6) and posX < 6*(WIDTH/6):
                    if onesplace == 9:
                        onesplace = 0
                        textone = numFont.render(str(onesplace), True, WHITE)
                        count = count - 9
                    else:
                        onesplace += 1
                        textone = numFont.render(str(onesplace), True, WHITE)
                        count = count + 1
              
        # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT
 
        # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT


        #advance the number
        if advance:
            count = count + 1
            

            if ones:
                if onesplace == 9:
                    tens = True
                onesplace = lib.func.advance(onesplace)
            if tens:
                if tensplace == 9:
                    huns = True
                tensplace = lib.func.advance(tensplace)
            if huns:
                if hunsplace == 9:
                    thous = True
                hunsplace = lib.func.advance(hunsplace)
            if thous:
                if thousplace == 9:
                    tenthous = True
                thousplace = lib.func.advance(thousplace)
            if tenthous:
                if tenthousplace == 9:
                    hunthous = True
                tenthousplace = lib.func.advance(tenthousplace)
            if hunthous:
                hunthous = lib.func.advance(hunthousplace)


            tens = False
            huns = False
            thous = False
            tenthous = False
            hunthouse = False
            
            #render the font
            textone = numFont.render(str(onesplace), True, WHITE)
            texttens = numFont.render(str(tensplace), True, WHITE)
            texthuns = numFont.render(str(hunsplace), True, WHITE)
            textthous = numFont.render(str(thousplace), True, WHITE)
            texttenthous = numFont.render(str(tenthousplace), True, WHITE)
            texthunthous = numFont.render(str(hunthousplace), True, WHITE)

            click_sound.play()
        
        #check if the number is prime
        #if the number is prime, stop the advance
        if lib.func.isPrime(count):
            advance = False

        # if the limit is reached, reset all to 0's
        if count == limit:
            count = 0
            onesplace = 0
            tensplace = 0
            hunsplace = 0
            thousplace = 0
            tenthousplace = 0
            hunthousplace = 0
                
        # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT
 
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
 
        # First, clear the screen to white. Don't put other drawing commands
        # above this, or they will be erased with this command.
        screen.fill(BLACK)

        # lib.func.drawLines(screen, WIDTH, HEIGHT)

        screen.blit(textone, [5*(WIDTH/6), 1])
        screen.blit(texttens, [4*(WIDTH/6), 0])
        screen.blit(texthuns, [3*(WIDTH/6), 2])
        screen.blit(textthous, [2*(WIDTH/6), 1])
        screen.blit(texttenthous, [1*(WIDTH/6), 1])
        screen.blit(texthunthous, [0*(WIDTH/6), 2])
        

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
 
        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
 
        # Limit to 60 frames per second
        clock.tick(tickSpeed)
 
    # Close the window and quit.
    # If you forget this line, the program will 'hang'
    # on exit if running from IDLE.
    pygame.quit()
 
if __name__ == "__main__":
    main()
