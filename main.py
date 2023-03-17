# RUN ME!!!!

import pygame, project

if __name__ == '__main__':
    pygame.init()
    project.setup()

    while not project.quit(True):

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                project.quit()
        
        project.update()
        project.drawSprites()
        pygame.display.flip()

        project.deltaTime(True)

    pygame.quit()
