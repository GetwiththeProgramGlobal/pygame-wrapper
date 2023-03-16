import pygame, project

if __name__ == '__main__':
    pygame.init()
    project.setup()

    shouldQuit = False
    while not shouldQuit:
        shouldQuit = project.quit(True)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                shouldQuit = True
        
        project.update()
        project.drawSprites()
        pygame.display.flip()

        project.deltaTime(True)

    pygame.quit()
