import pygame, project

if __name__ == '__main__':
    pygame.init()
    Project.setup()

    shouldQuit = False
    while not shouldQuit:
        shouldQuit = Project.quit(True)

        for event in pygame.event.get():
            if event.type == pygame.QUIT or Project.keyDown("ESCAPE"): 
                shouldQuit = True
        
        Project.update()
        Project.drawSprites()
        pygame.display.flip()

        Project.deltaTime(True)

    pygame.quit()
